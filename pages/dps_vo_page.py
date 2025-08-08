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
            new_tab.wait_for_load_state("load", timeout=8000)
        except:
            print(f"⚠️ {label} tab did not fully load.")

        # Retry button
        try:
            retry_button = new_tab.locator('//*[@id="button-block"]/input[2]')
            retry_button.wait_for(state="visible", timeout=5000)
            retry_button.click()
            print(f"✅ Retry (Select All) clicked in {label}.")
        except Exception as e:
            print(f"⚠️ Retry button not clickable in {label}: {e}")

        # Save button
        try:
            save_button = new_tab.locator('//*[@id="saveButtonId"]')
            save_button.wait_for(state="visible", timeout=5000)
            save_button.click()
            print(f"✅ Save clicked in {label}.")
        except Exception as e:
            print(f"⚠️ Save button not clickable in {label}: {e}")

        new_tab.close()
        print(f"✅ {label} tab closed.")

    def process_all_links_in_order(self):
        links = self.page.locator('//*[@id="initiateResponseBody"]/tr/td[2]/a')
        count = links.count()

        if count == 0:
            print("⚠️ No links found in initiateResponseBody.")
            return False

        processed_any = False

        for i in range(count):
            link = links.nth(i)
            try:
                if link.is_visible(timeout=3000):
                    text = link.inner_text().strip()
                    label = f"Link #{i+1} ({text})"
                    self.click_and_process_link(link, label)
                    processed_any = True
                else:
                    print(f"⚠️ Link #{i+1} not visible.")
            except Exception as e:
                print(f"❌ Error processing link #{i+1}: {e}")

        return processed_any
