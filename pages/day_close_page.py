from time import time
from playwright.sync_api import Page
import pyperclip
from pages.common_actions import handle_office_busy


class DayClosePage:
    def __init__(self, page: Page):
        self.page = page

    def add_currency_denomination(self):
        self.page.locator('//*[@id="module-accounting"]/a').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[7]').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/a').click()
        self.page.locator('//*[@id="pageContent"]/div/div[1]/div[2]/a').click()

        
        # ✅ Office Busy check at start of every loop
        handle_office_busy(self.page, "16250", "abc123$") 

        self.page.wait_for_selector('//*[@id="totalBalance"]', timeout=10000)
        balance = self.page.locator('//*[@id="totalBalance"]').inner_text()
        print("Balance:", balance)

        # Copy balance to clipboard
        pyperclip.copy(balance)

        # Click the input field, then paste with Ctrl+V
        self.page.locator('//*[@id="currentPaymentAmount1"]').click()
        self.page.keyboard.press('Control+V')

        self.page.locator('//*[@id="create2"]').click()
        self.page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
        self.page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()



    def go_to_day_close(self): #day close button
        self.page.locator('//*[@id="module-accounting"]/a').click() #accounting
        self.page.locator('//*[@id="wrapper"]/ul/li[1]').click()    #admin
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click() #general settings
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click() #day close
        
    def click_initiate(self):
        try:
            initiate_btn = self.page.locator('//*[@id="initiate"]')
            if initiate_btn.is_visible(timeout=3000):
                initiate_btn.click()
                print("✅ Initiate clicked.")

                confirm_btn = self.page.locator('xpath=/html/body/div[11]/div[7]/div/button')
                if confirm_btn.is_visible(timeout=3000):
                    confirm_btn.click()
                    print("✅ Confirm accepted.")
                else:
                    print("⚠️ Confirm button not found.")
            else:
                print("ℹ️ Initiate button not found or not visible.")
        except Exception as e:
            print(f"❌ Error in click_initiate: {e}")

    # def click_initiate(self): # initiate button
    #     if self.page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
    #         self.page.locator('//*[@id="initiate"]').click()
    #         print("✅ Initiate clicked.")
    #         self.page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
    #         self.page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()
            

    def click_day_close(self):
        try:
            locator = self.page.locator('//*[@id="dayClose"]')
            if locator.is_visible(timeout=3000):
                locator.click()
                print("✅ Day Close clicked.")
            else:
                print("ℹ️ Day Close button not found — skipping.")
        except Exception as e:
            print(f"⚠️ Error while trying to click Day Close: {e}")



    # def click_day_close(self): 
    #     if self.page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
    #         self.page.locator('//*[@id="dayClose"]').click()
    #         print("✅ Day Close clicked.")
            



