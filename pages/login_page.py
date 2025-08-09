from playwright.sync_api import Page, TimeoutError

class LoginPage:
    def __init__(self, page: Page):
        self.page = page


    def login(self, username: str, password: str):
        self.page.locator('//*[@id="username"]').fill(username)
        self.page.locator('//*[@id="password"]').fill(password)
        self.page.locator('//*[@id="kc-login"]').click()

    def select_office(self, office_xpath='//*[@id="418"]/div[2]'):
        self.page.locator('//*[@id="officeIdDiv_arrow"]').click()
        self.page.locator(office_xpath).click()
        self.page.locator('//*[@id="search-form"]/div[3]/span[1]/input').click()


