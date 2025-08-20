from playwright.sync_api import Page, TimeoutError
import re

class MonthClosePage:
    def __init__(self, page: Page):
        self.page = page

    def get_month_from_message(self) -> str | None:
        """Detect the depreciation warning and extract the month name."""
        try:
            message_locator = self.page.locator(
                "//td[contains(text(),'Depreciation not calculated for the month')]"
            )
            message_locator.wait_for(state="visible", timeout=5000)
            message_text = message_locator.inner_text()

            match = re.search(r'month (\w+)', message_text)
            if match:
                month = match.group(1)
                print(f"ℹ️ Detected month in message: {month}")
                return month
            else:
                print("⚠️ Month not found in message text.")
                return None
        except TimeoutError:
            print("ℹ️ No depreciation month-close message found.")
            return None

    def click_month_close_link(self):
        """Open the month-close link in new tab and perform the close actions."""
        try:
            link_locator = self.page.locator('//*[@id="initiateResponseBody"]/tr[2]/td[2]/a')
            link_locator.wait_for(state="visible", timeout=8000)
            print("✅ Month close link is visible. Clicking...")

            with self.page.context.expect_page() as new_page_info:
                link_locator.click()

            new_tab = new_page_info.value
            print("✅ New tab for month close opened.")

            # Step 1: Click main "Save" button
            month_close_btn = new_tab.locator('//*[@id="pageContent"]/div[2]/div[1]/div[2]/button')
            month_close_btn.wait_for(state="visible", timeout=10000)
            month_close_btn.click()
            print("✅ Save button clicked.")

            # Step 2: Click depreciation schedule button
            schedule_btn = new_tab.locator('//*[@id="assetDepreciationScheduleList"]/tbody/tr[1]/td[9]/button')
            schedule_btn.wait_for(state="visible", timeout=10000)
            schedule_btn.click()
            print("✅ Depreciation schedule button clicked.")

            # Optional: wait for confirmation toast or success message
            # new_tab.wait_for_selector("//*[contains(text(),'Success')]", timeout=10000)

            new_tab.close()
            print("✅ Month close tab closed successfully.")

        except TimeoutError as e:
            print(f"❌ Timeout while handling month close process: {e}")
        except Exception as e:
            print(f"❌ Unexpected error during month close process: {e}")


    def click_business_month_close_navigation(self):
        try:
            self.page.locator('//*[@id="wrapper"]/ul/li[1]').click()
            self.page.wait_for_timeout(500)

            self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[2]/div/span').click()
            self.page.wait_for_timeout(500)

            self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[2]/ul/li[2]/a').click()
            self.page.wait_for_timeout(500)

        except Exception as e:
            print(f"❌ Error during business month close navigation: {e}")

    def check_month_close_popup_and_navigate(self):
        try:
            popup_text_locator = self.page.locator('xpath=//div[contains(@class, "sweet-alert") and contains(@style, "display: block")]//p[text()="Month not closed yet"]')
            if popup_text_locator.is_visible(timeout=5000):
                print("⚠️ Popup detected: Month not closed yet")
                
                # Better locator for OK button:
                ok_button = self.page.locator('button.confirm', has_text='OK')
                ok_button.wait_for(state="visible", timeout=5000)
                ok_button.click()
                print("✅ Popup OK button clicked to close popup.")
            else:
                print("ℹ️ No 'Month not closed yet' popup detected.")
        except Exception as e:
            print(f"❌ Error handling month not closed popup: {e}")

    def month_close_button(self):
        try:
            month_close_btn = self.page.locator('//*[@id="monthClose"]')
            month_close_btn.wait_for(state="visible", timeout=8000)
            month_close_btn.click()
            print("✅ Month Close button clicked successfully.")
        except Exception as e:
            print(f"❌ Error clicking Month Close button: {e}")



    def execute_month_close_if_needed(self):
        """Run the month-close process only if depreciation message is detected."""
        month = self.get_month_from_message()
        if month:
            self.click_month_close_link()
            self.month_close_page.check_month_close_popup_and_navigate()
            self.month_close_page.click_business_month_close_navigation()
            self.day_open.click_initiate()
            self.month_close_page.month_close_button()
        else:
            print("ℹ️ No month close action needed.")
