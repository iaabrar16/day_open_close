from playwright.sync_api import Page

class DayOpenPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_day_open(self): #day open button
        self.page.locator('//*[@id="module-accounting"]/a').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span').click()

    def click_initiate(self):
        try:
            initiate_btn = self.page.locator('//*[@id="initiate"]')
            if initiate_btn.is_visible(timeout=2000):
                initiate_btn.click()
                print("✅ Initiate clicked.")

                # Click confirm button with role 'button' and name 'Yes'
                confirm_btn = self.page.get_by_role("button", name="Yes")
                if confirm_btn.is_visible(timeout=3000):
                    confirm_btn.click()
                    print("✅ Confirm accepted.")

                    # Wait for the specific modal and press Enter if appears
                    modal = self.page.locator('/html/body/div[4]')
                    if modal.wait_for(state='visible', timeout=5000):
                        # print("ℹ️ Modal detected — pressing Enter.")
                        # self.page.keyboard.press("Enter")
                        self.page.reload()
                        print("ℹ️ Modal detected — page reload.")
                        
                    else:
                        print("⚠️ Modal not detected after confirm.")
                else:
                    print("⚠️ Confirm button not found.")
            else:
                print("ℹ️ Initiate button not visible.")
        except Exception as e:
            print(f"❌ Error in click_initiate: {e}")




    # def click_initiate(self): # initiate button
    #     if self.page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
    #         self.page.locator('//*[@id="initiate"]').click()
    #         print("✅ Initiate clicked.")



    def click_day_open(self):
        try:
            day_open_btn = self.page.locator('//*[@id="dayOpen"]')
            if day_open_btn.is_visible(timeout=3000):
                day_open_btn.click()
                print("✅ Day Open clicked.")
            else:
                print("ℹ️ Day Open button not found or not visible.")
        except Exception as e:
            print(f"❌ Error in click_day_open: {e}")


    # def click_day_open(self): 
    #     if self.page.locator('//*[@id="dayOpen"]').is_visible(timeout=3000):
    #         self.page.locator('//*[@id="dayOpen"]').click()
    #         print("✅ Day Close clicked.")
            
