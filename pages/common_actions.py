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
        print("✅ Second Reinitiate button clicked.")
    else:
        print("❌ Second Reinitiate button not visible.")

    button3 = page.locator('//*[@id="initiateResponseBody"]/tr[3]/td[3]/button')
    if button3.is_visible(timeout=3000):
        button3.click()
        print("✅ Third Reinitiate button clicked.")
    else:
        print("❌ Third Reinitiate button not visible.")
