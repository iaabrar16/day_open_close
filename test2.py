from playwright.sync_api import sync_playwright

def test_otc_savings_collection():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://erpstaging.brac.net/")

        # Login
        page.locator('xpath=//*[@id="username"]').fill('21267')
        page.locator('xpath=//*[@id="password"]').fill('abc123$')
        page.locator('xpath=//*[@id="kc-login"]').click()

        # Handle modal popups
        close_button_locator = page.locator('xpath=//*[@id="modals"]/div[1]/button')
        while True:
            try:
                close_button_locator.wait_for(state='visible', timeout=5000)
                close_button_locator.click()
                page.wait_for_timeout(500)
            except:
                break
        print("All modals closed.")

        # Wait for any loading overlay to disappear
        overlay_locator = page.locator('div#overlay.active')
        if overlay_locator.is_visible():
            print("Overlay is present. Waiting...")
            overlay_locator.wait_for(state='hidden', timeout=30000)
        print("Overlay cleared.")

        # Navigate to the MF module section
        page.locator('xpath=//*[@id="module-mf"]/a').click()

        # Navigate to Savings collection section
        page.locator('xpath=/html/body/div[1]/div/div[5]/div[1]/div/ul/li[9]/div').click()
        page.locator('xpath=/html/body/div[1]/div/div[5]/div[1]/div/ul/li[9]/ul/li[1]/div/span').click()

        # Navigate to OTC page
        with context.expect_page() as new_page_info:
            page.locator("a[href='/otc/app/savings/individualSavingsCollection']").click()

        otc_page = new_page_info.value
        otc_page.bring_to_front()

        # savings dropdown click
        otc_page.locator(
            'xpath=//*[@id="root"]/div/div/div[2]/div/main/div/form/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/div'
        ).click()


        # Select option from the dropdown menu
        otc_page.locator("div.select__menu-list >> text=Progoti").click()

        # Fill the input after selecting Progoti
        otc_page.locator(
            'xpath=//*[@id="root"]/div/div/div[2]/div/main/div/form/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/input'
        ).fill("10503")

        # keep browser open to see result
        page.wait_for_timeout(5000)
        browser.close()
