class DPSVOPage:
    def __init__(self, page):
        self.page = page

    def click_and_process_link(self, link_element, label):
        print(f"✅ {label} link is visible and clicked.")

        with self.page.context.expect_page() as new_page_info:
            link_element.click()

        new_tab = new_page_info.value
        print(f"✅ {label} tab opened.")

        try:
            # Wait until tab fully loads
            new_tab.wait_for_load_state("load", timeout=8000)
        except:
            print(f"⚠️ {label} tab did not fully load.")

        # Wait for retry button (select all)
        try:
            retry_button = new_tab.locator('//*[@id="button-block"]/input[2]')
            retry_button.wait_for(state="visible", timeout=5000)
            retry_button.click()
            print(f"✅ Retry (Select All) button clicked in {label}.")
        except Exception as e:
            print(f"⚠️ Retry (Select All) button not visible/clickable in {label}: {e}")

        # Wait for save button
        try:
            save_button = new_tab.locator('//*[@id="saveButtonId"]')
            save_button.wait_for(state="visible", timeout=5000)
            save_button.click()
            print(f"✅ Save button clicked in {label}.")
        except Exception as e:
            print(f"⚠️ Save button not visible/clickable in {label}: {e}")

        new_tab.close()
        print(f"✅ {label} tab closed.")

    def handle_first_available_link(self):
        links = self.page.locator('//*[@id="initiateResponseBody"]/tr/td[2]/a')
        count = links.count()

        if count == 0:
            print("⚠️ No links found in the initiateResponseBody table.")
            return False

        for i in range(count):
            link = links.nth(i)
            if link.is_visible(timeout=3000):
                text = link.inner_text()
                label = f"Link #{i+1} ({text})"
                self.click_and_process_link(link, label)
                return True

        print("⚠️ No visible links found to process.")
        return False

    def process_all_links_in_order(self):
        links = self.page.locator('//*[@id="initiateResponseBody"]/tr/td[2]/a')
        count = links.count()

        if count == 0:
            print("⚠️ No links found in the initiateResponseBody table.")
            return

        for i in range(count):
            link = links.nth(i)
            if link.is_visible(timeout=3000):
                text = link.inner_text()
                label = f"Link #{i+1} ({text})"
                self.click_and_process_link(link, label)
            else:
                print(f"⚠️ Link #{i+1} not visible.")
