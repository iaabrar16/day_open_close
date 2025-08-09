from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.day_open_page import DayOpenPage
from pages.day_close_page import DayClosePage
from pages.fund_requisition_page import FundRequisitionPage
from pages.common_actions import click_reinitiate_buttons, handle_office_busy
from pages.dps_vo_page import DPSVOPage
from pages.month_close_page import MonthClosePage


from datetime import datetime, timedelta

def test_day_open_close_till_date(last_date_str="25-06-2025"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # page.goto("https://env46.erp.bracits.net/")
        page.goto("https://erpstaging.brac.net/")

        login = LoginPage(page)
        login.login("16250", "abc123$")
        login.select_office()

  
        # Close the modal
        modal = page.locator('//*[@id="modals"]')
        # Wait until the modal is visible
        modal.wait_for(state="visible", timeout=3000)
        # Press Enter to close the modal
        page.keyboard.press("Enter")

        day_close = DayClosePage(page)
        day_open = DayOpenPage(page)
        fund_page = FundRequisitionPage(page)
        dps_vo_page = DPSVOPage(page)
        month_close_page = MonthClosePage(page)

        # Convert last_date_str to datetime object
        last_date_str = "01-07-2025"
        last_date = datetime.strptime(last_date_str, "%d-%m-%Y")

        while True:           

            # Get current business date from page
            business_date_text = page.locator('//*[@id="sessionBusinessDateReload"]/span').inner_text().strip()
            # Example: "Accounting Date : 20-06-2025"
            current_date_str = business_date_text.split(":")[-1].strip()
            current_date = datetime.strptime(current_date_str, "%d-%m-%Y")

            print(f"🔍 Current Business Date: {current_date_str}")

            if current_date >= last_date:
                print(f"✅ Reached the last date {last_date_str}. Stopping automation.")
                break

            # Now check day status and run open/close flow as you have
            page.wait_for_selector('//*[@id="sessionBusinessDateReload"]/a', timeout=15000)
            status_text = page.locator('//*[@id="sessionBusinessDateReload"]/a').inner_text().strip().upper()
            print("🔁 Current Status:", status_text)

            if "OPEN" in status_text:
                print("🔁 Status is DAY OPEN — navigating to Day Close.")
                day_close.add_currency_denomination()
                day_close.go_to_day_close()
                day_close.click_initiate()
                click_reinitiate_buttons(page)
                month_close_page.execute_month_close_if_needed()

                page.wait_for_timeout(3000)

                if dps_vo_page.process_all_links_in_order():
                    click_reinitiate_buttons(page)
                    page.wait_for_timeout(3000)
                    day_close.click_initiate()
                    day_close.click_day_close()

                # Toast check in Day Close flow
                page.wait_for_timeout(2000)
                if page.locator('//*[@id="toast-container"]/div/div').is_visible(timeout=3000):
                    toast_text = page.locator('//*[@id="toast-container"]/div/div').inner_text().strip()
                    print("⚠️ Toast:", toast_text)

                    if "fund requisition" in toast_text.lower():
                        fund_page.create_requisition()
                        day_close.go_to_day_close()
                        day_close.click_initiate()
                        day_close.click_day_close()

            else:
                print("🔁 Status is DAY CLOSE — navigating to Day Open.")
                day_open.go_to_day_open()
                day_open.click_initiate()
                day_open.click_day_open()
                # day_close.go_to_day_close()
                # month_close_page.execute_month_close_if_needed()
                # click_reinitiate_buttons(page)
                month_close_page.check_month_close_popup_and_navigate()
                month_close_page.click_business_month_close_navigation()
                day_open.click_initiate()
                month_close_page.month_close_button()

            # Wait a little before next iteration (optional)
            page.wait_for_timeout(3000)

            # Refresh page or reload to update business date and status for next iteration
            page.reload()


        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/screenshot.png")
        browser.close()
