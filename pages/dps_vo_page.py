class DPSVOPage:
    def __init__(self, page):
        self.page = page

    def click_and_process_link(self, link_element, label):
        print(f"✅ {label} link is visible and clicked.")
        with self.page.context.expect_page() as new_page_info:
            link_element.click()
        new_tab = new_page_info.value
        print(f"✅ {label} tab opened.")

        retry_button = new_tab.locator('//*[@id="button-block"]/input[2]')
        if retry_button.is_visible(timeout=3000):
            retry_button.click()
            print(f"✅ Retry button clicked in {label}.")
        else:
            print(f"⚠️ Retry button not visible in {label}.")

        save_button = new_tab.locator('//*[@id="saveButtonId"]')
        if save_button.is_visible(timeout=3000):
            save_button.click()
            print(f"✅ Save button clicked in {label}.")
        else:
            print(f"⚠️ Save button not visible in {label}.")

        new_tab.close()
        print(f"✅ {label} tab closed.")

    def handle_first_available_link(self):
        # Get all links inside initiateResponseBody tr > td[2] > a (all anchors)
        links = self.page.locator('//*[@id="initiateResponseBody"]/tr/td[2]/a')
        count = links.count()

        if count == 0:
            print("⚠️ No links found in the initiateResponseBody table.")
            return False

        # Iterate over all links in order, pick the first visible one and process
        for i in range(count):
            link = links.nth(i)
            if link.is_visible(timeout=3000):
                text = link.inner_text()
                href = link.get_attribute("href")
                label = f"Link #{i+1} ({text})"
                self.click_and_process_link(link, label)
                return True

        print("⚠️ No visible links found to process.")
        return False

    def process_all_links_in_order(self):
        # This method tries to process links one by one in order.
        # If you want to click all available links one after another.

        links = self.page.locator('//*[@id="initiateResponseBody"]/tr/td[2]/a')
        count = links.count()

        if count == 0:
            print("⚠️ No links found in the initiateResponseBody table.")
            return

        for i in range(count):
            link = links.nth(i)
            if link.is_visible(timeout=3000):
                text = link.inner_text()
                href = link.get_attribute("href")
                label = f"Link #{i+1} ({text})"
                self.click_and_process_link(link, label)
            else:
                print(f"⚠️ Link #{i+1} not visible.")

