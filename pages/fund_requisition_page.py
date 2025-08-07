import random
from playwright.sync_api import Page

class FundRequisitionPage:
    def __init__(self, page: Page):
        self.page = page

    def create_requisition(self):
        self.page.locator('//*[@id="wrapper"]/ul/li[5]/div').click()
        self.page.locator('//*[@id="wrapper"]/ul/li[5]/ul/li[3]/a').click()
        self.page.locator('//*[@id="createNew"]').click()
        random_number = "01" + "".join(str(random.randint(0, 9)) for _ in range(9))
        self.page.locator('//*[@id="mobileNo"]').fill(random_number)
        self.page.locator('//*[@id="actualRequisitionAmount"]').fill("100000")
        self.page.locator('//*[@id="submit1"]').click()
