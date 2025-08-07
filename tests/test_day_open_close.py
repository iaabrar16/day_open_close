from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.day_open_page import DayOpenPage
from pages.day_close_page import DayClosePage
from pages.fund_requisition_page import FundRequisitionPage
from pages.common_actions import click_reinitiate_buttons
from pages.dps_vo_page import DPSVOPage


def test_day_close_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        page.goto("https://env46.erp.bracits.net/")

        login = LoginPage(page)
        login.login("16250", "abc123$")
        login.select_office()


        day_close = DayClosePage(page)
        day_open = DayOpenPage(page)



        # After login and office selection
        # business_date_text = page.locator('//*[@id="sessionBusinessDateReload"]/span').inner_text().strip()
        # print("🔍 Business Date Text:", business_date_text)


        page.wait_for_selector('//*[@id="sessionBusinessDateReload"]/a', timeout=15000)
        status_text = page.locator('//*[@id="sessionBusinessDateReload"]/a').inner_text().strip().upper()
        print("🔁 Current Status:", status_text)

        if "OPEN" in status_text:
            print("🔁 Status is DAY OPEN — navigating to Day Close.")
            day_close.add_currency_denomination()
            day_close.go_to_day_close()
            day_close.click_initiate()

            # Handle pending links before clicking Day Close
            dps_vo_page = DPSVOPage(page)
            dps_vo_page.handle_first_available_link()
            click_reinitiate_buttons(page)
            day_close.click_day_close()
            
        else:
            print("🔁 Status is DAY CLOSE — navigating to Day Open.")
            day_open.go_to_day_open()
            day_open.click_initiate()
            day_open.click_day_open()



        # # Check toast
        page.wait_for_timeout(2000)
        if page.locator('//*[@id="toast-container"]/div/div').is_visible(timeout=3000):
            toast_text = page.locator('//*[@id="toast-container"]/div/div').inner_text().strip()
            print("⚠️ Toast:", toast_text)

            if "fund requisition" in toast_text.lower():
                fund_page = FundRequisitionPage(page)
                fund_page.create_requisition()
                day_close.go_to_day_close()
                day_close.click_initiate()
                day_close.click_day_close()


        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/screenshot.png")
        browser.close()
