from playwright.sync_api import Page

class DayOpenPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_day_open(self): #day open button
        self.page.locator('//*[@id="module-accounting"]/a').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span').click()

    def click_initiate(self): # initiate button
        if self.page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
            self.page.locator('//*[@id="initiate"]').click()
            print("✅ Initiate clicked.")

    def click_day_open(self): 
        if self.page.locator('//*[@id="dayOpen"]').is_visible(timeout=3000):
            self.page.locator('//*[@id="dayOpen"]').click()
            print("✅ Day Close clicked.")
            
