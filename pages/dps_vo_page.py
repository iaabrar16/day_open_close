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
            new_tab.wait_for_load_state("load", timeout=25000)
        except:
            print(f"⚠️ {label} tab did not fully load.")

        # Retry / Select All button handling
        try:
            # Prefer CSS with has-text for better reliability
            new_tab.wait_for_selector('button:has-text("Select All")', timeout=8000)
            retry_button = new_tab.locator('button:has-text("Select All")')
            retry_button.click()
            print(f"✅ Retry/Select All clicked in {label}.")
        except Exception as e1:
            print(f"⚠️ Retry/Select All button not found or clickable in {label} using has-text: {e1}")
            try:
                # fallback xpath locator
                new_tab.wait_for_selector('xpath=//*[@id="button-block"]/input[2]', timeout=8000)
                retry_button = new_tab.locator('xpath=//*[@id="button-block"]/input[2]')
                retry_button.click()
                print(f"✅ Retry/Select All clicked in {label} using xpath fallback.")
            except Exception as e2:
                print(f"⚠️ Retry/Select All button not clickable in {label} fallback xpath: {e2}")

        # Save / Retry button handling
        try:
            new_tab.wait_for_selector('button:has-text("Retry")', timeout=8000)
            save_button = new_tab.locator('button:has-text("Retry")')
            save_button.click()
            self.page.wait_for_timeout(2000)
            print(f"✅ Save/Retry clicked in {label}.")
        except Exception as e1:
            print(f"⚠️ Save/Retry button not found or clickable in {label} using has-text: {e1}")
            try:
                new_tab.wait_for_selector('xpath=//*[@id="saveButtonId"]', timeout=8000)
                save_button = new_tab.locator('xpath=//*[@id="saveButtonId"]')
                save_button.click()
                print(f"✅ Save/Retry clicked in {label} using xpath fallback.")
            except Exception as e2:
                print(f"⚠️ Save/Retry button not clickable in {label} fallback xpath: {e2}")
           
        self.page.wait_for_timeout(3000)
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
