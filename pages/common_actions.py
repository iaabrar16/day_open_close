from playwright.sync_api import Page



def click_reinitiate_buttons(page: Page):
    button1 = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[3]/button')
    if button1.is_visible(timeout=3000):
        button1.click()
        print("✅ First Reinitiate button clicked.")
    else:
        print("❌ First Reinitiate button not visible.")

    button2 = page.locator('//*[@id="initiateResponseBody"]/tr[2]/td[3]/button')
    if button2.is_visible(timeout=3000):
        button2.click()
        print("✅ Rebroadcast button clicked.")
    else:
        print("❌ Rebroadcast button not visible.")

    button3 = page.locator('//*[@id="initiateResponseBody"]/tr[3]/td[3]/button')
    if button3.is_visible(timeout=3000):
        button3.click()
        print("✅ Third Reinitiate button clicked.")
    else:
        print("❌ Third Reinitiate button not visible.")


def handle_office_busy(page, username, password):
    try:
        # Detect the "Business day is not opened / Office Busy" message
        busy_msg = page.locator("//h4[contains(text(),'Business day is not opened')]")
        if busy_msg.is_visible(timeout=3000):
            print("⚠️ Office Busy detected — logging out and retrying login.")

            from pages.day_close_page import DayClosePage
            from pages.day_open_page import DayOpenPage

            day_close = DayClosePage(page)
            day_close.go_to_day_close()
            page.wait_for_timeout(3000)
            day_close.click_initiate()
            day_close.click_day_close()

            day_open = DayOpenPage(page)
            day_open.go_to_day_open()
            day_open.click_initiate()
            day_open.click_day_open()

            page.locator('//*[@id="module-accounting"]/a').click()
            page.locator('//*[@id="wrapper"]/ul/li[7]').click()
            page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/a').click()
            page.locator('//*[@id="pageContent"]/div/div[1]/div[2]/a').click()
            page.wait_for_timeout(2000)

        else:
            print("ℹ️ No Office Busy message detected.")
            return False

    except Exception as e:
        print(f"❌ Error in handle_office_busy: {e}")
        return False
