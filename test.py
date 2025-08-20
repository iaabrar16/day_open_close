from playwright.sync_api import sync_playwright
import random, time
from pyperclip import copy



def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        page = browser.new_page()
        
        # Navigate to the login page
        #page.goto("https://env54.erp.bracits.net/")
        page.goto("https://env46.erp.bracits.net/")

        # Fill in the login form and submit
        page.locator('//*[@id="username"]').fill("16250")
        page.locator('//*[@id="password"]').fill("abc123$")
        page.locator('//*[@id="kc-login"]').click()

        # Select the office
        page.locator('//*[@id="officeIdDiv_arrow"]').click()
        page.locator('//*[@id="418"]/div[2]').click()
        page.locator('//*[@id="search-form"]/div[3]/span[1]/input').click()


        # Close the modal
        # modal = page.locator('//*[@id="modals"]')
        # # Wait until the modal is visible
        # modal.wait_for(state="visible", timeout=3000)
        # # Press Enter to close the modal
        # page.keyboard.press("Enter")

        # Navigate to the Currency Denomination page
        page.locator('//*[@id="module-accounting"]/a').click()
        page.locator('//*[@id="wrapper"]/ul/li[7]').click()
        page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/a').click()
        page.locator('//*[@id="pageContent"]/div/div[1]/div[2]/a').click()

        page.wait_for_selector('//*[@id="totalBalance"]', timeout=10000)
        balance = page.locator('//*[@id="totalBalance"]').inner_text()
        print("Balance:", balance)
        # Copy the balance to clipboard
        copy(balance)
        # Click the input field, then paste using Ctrl+V
        page.locator('//*[@id="currentPaymentAmount1"]').click()
        page.keyboard.press('Control+V')

        page.locator('//*[@id="create2"]').click()
        page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
        page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()

        # Navigate to the Day Close page
        page.locator('//*[@id="wrapper"]/ul/li[1]').click()
        page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
        page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()
        # page.locator('xpath=//*[@id="initiate"]').click()
        # print("✅ hello 1.")
        # page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
        # page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()

        page.wait_for_timeout(2000)  # Give some time for toast to appear

        #basic day close



        #if any toast issue
        # Check for the toast message
        toast_locator = page.locator('//*[@id="toast-container"]/div/div')

        if toast_locator.is_visible():
            toast_text = toast_locator.inner_text().strip()

            # Navigate to the fund requisition page
            if toast_text == "Your weekly fund requisition not created. Please before day close you must submit fund requisition.":
                print("❗ Weekly fund requisition toast appeared:", toast_text)
                page.locator('//*[@id="wrapper"]/ul/li[5]/div').click()
                page.locator('//*[@id="wrapper"]/ul/li[5]/ul/li[3]/a').click()
                page.locator('//*[@id="createNew"]').click()
                random_number = "01" + "".join(str(random.randint(0, 9)) for _ in range(9))
                page.locator('//*[@id="mobileNo"]').fill(random_number)
                page.locator('//*[@id="actualRequisitionAmount"]').fill("100000")  # Example amount, adjust as needed
                page.locator('//*[@id="updateAndSubmit"]').click()
                page.locator('//*[@id="wrapper"]/ul/li[1]').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()
            
                # Wait for and click "initiate" button
            if page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
                page.locator('//*[@id="initiate"]').click()
                print("✅ hello 2.")
                # page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                # page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()
                page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
                page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()
                
            # Wait for and click "dayClose" button
            if page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
                page.locator('//*[@id="dayClose"]').click()

            elif "ব্যর্থ ভাউচার" in toast_text and "প্রক্রিয়াধীন ভাউচার" in toast_text:
                print("❗ ব্যর্থ ভাউচার")
                page.locator('//*[@id="btn_login"]').click()
                page.locator('//*[@id="login_container"]/li[3]/a').click()
                # Fill in the login form and submit
                page.locator('//*[@id="username"]').fill("tuhin")
                page.locator('//*[@id="password"]').fill("abc123$")
                page.locator('//*[@id="kc-login"]').click()
                # page.locator('//*[@id="module-mf"]/a').click()
                # page.locator('//*[@id="wrapper"]/ul/li[7]').click()
                # page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/div/span').click()
                # page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/ul/li[1]/a/span').click()
                # # page.locator('//*[@id="wrapper"]/ul/li[7]/ul/li[2]/ul/li[1]/a/span').click()
                # with page.context.expect_page() as new_page_info:
                #     page.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/div/span[1]/span[2]').click()
                # new_tab = new_page_info.value
                # new_tab.wait_for_load_state()
                # new_tab.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/ul/div/a/span').click()
                page.goto("https://env69.erp.bracits.net/otc/app/loanProposal/create")
                page.wait_for_load_state()
                # Wait for and click the menu toggle
                page.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/div/span[1]/span[2]').wait_for(state="visible", timeout=5000)
                page.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/div/span[1]/span[2]').dblclick()

                # Wait for and click the dropdown menu item
                page.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/ul/div/a/span').wait_for(state="visible", timeout=5000)
                page.locator('//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/nav/div[3]/ul/div/a/span').click()

                page.locator('//*[@id="root"]/div/div/div[2]/div/main/div/div[2]/div[2]/div/div[1]/table/thead/tr/th[1]/div/div/label/input').check()
                page.locator('//*[@id="root"]/div/div/div[2]/div/main/div/div[2]/button').wait_for(state="visible", timeout=5000)
                page.locator('//*[@id="root"]/div/div/div[2]/div/main/div/div[2]/button').click()


                # Handle the confirm alert by accepting it
                page.on("dialog", lambda dialog: dialog.accept())

                # Click the button that triggers the alert
                page.locator('xpath=/html/body/div[9]/div/div/div/div[2]/button[2]').click()


                page.locator('xpath=//*[@id="dropdown-toggle-1-TF9mFdcjhT"]/div/div').click()

                menu_item = page.locator('xpath=//*[@id="base-menu-2-CRBdiSOAvg"]/li[2]')
                menu_item.wait_for(state="visible", timeout=5000)
                menu_item.click()


                page.goto("https://env46.erp.bracits.net/")

                # Fill in the login form and submit
                page.locator('//*[@id="username"]').fill("16250")
                page.locator('//*[@id="password"]').fill("abc123$")
                page.locator('//*[@id="kc-login"]').click()

                # Select the office
                page.locator('//*[@id="officeIdDiv_arrow"]').click()
                page.locator('//*[@id="418"]/div[2]').click()
                page.locator('//*[@id="search-form"]/div[3]/span[1]/input').click()


                # Navigate to the Day Close page
                page.locator('//*[@id="wrapper"]/ul/li[1]').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()
                page.locator('xpath=//*[@id="initiate"]').click()
                print("✅ hello 3.")
                page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
                page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()   
                
                #another solve(MongoDB)

            else:
                print("⚠️ Some other toast appeared:", toast_text)
        else:
            print("✅ No toast appeared. Proceeding as normal.")
            
                        # toast issue solved

 # dps ,vo collection status, vo savings collection status issue 
            # Check for DPS pending link and handle it        
            dps = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[2]/a[1]')

            if dps.is_visible(timeout=3000):
                print("✅ Test1")
                with page.context.expect_page() as new_page_info:
                    dps.click()
                    print("✅ Test1 clicked")
                new_tab = new_page_info.value
                print("✅ DPS pending tab opened.")

                retry_button = new_tab.locator('//*[@id="button-block"]/input[2]')
                if retry_button.is_visible(timeout=3000):
                    retry_button.click()
                else:
                    print("⚠️ Retry button not visible in DPS pending tab.")

                save_button = new_tab.locator('//*[@id="saveButtonId"]')
                if save_button.is_visible(timeout=3000):
                    save_button.click()
                    new_tab.close()
                else:
                    print("⚠️ Save button not visible in DPS pending tab.")
                    new_tab.close()
            else:
                print("⚠️ DPS link not visible on main page.")



         # VO Collection Status
  
        vo_collection_status = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[2]/a[1]')
        vo_savings_collection_status = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[2]/a[2]')
       
        if vo_collection_status.is_visible(timeout=3000):
            with page.context.expect_page() as new_page_info:
                vo_collection_status.click()
            new_tab = new_page_info.value
            print("✅ VO Collection Status tab opened.")

            new_tab.locator('//*[@id="button-block"]/input[2]').click()
            
            save_button = new_tab.locator('//*[@id="saveButtonId"]')
            if save_button.is_visible(timeout=3000):
                save_button.click()
                new_tab.close()
            else:
                print("⚠️ Save button not visible in VO Collection tab.")
                new_tab.close()
            
            


        # VO Savings Collection Status
        if vo_savings_collection_status.is_visible(timeout=3000):
            with page.context.expect_page() as new_page_info:
                vo_savings_collection_status.click()
            new_tab = new_page_info.value
            print("✅ VO Savings Collection Status tab opened.")

            new_tab.locator('//*[@id="button-block"]/input[2]').click()
            
            save_button = new_tab.locator('//*[@id="saveButtonId"]')
            if save_button.is_visible(timeout=3000):
                save_button.click()
                new_tab.close()
            else:
                print("⚠️ Save button not visible in VO Collection tab.")
                new_tab.close()

                        # dps ,vo collection status, vo savings collection status issue solved

            # reinitiate_button1 = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[3]/button')
            # if reinitiate_button1.is_visible(timeout=3000):
            #     reinitiate_button1.click()
            #     print("✅ First button clicked.")
            # else:
            #     print("❌ First button not visible.")

            # # Wait for the second button to be visible, then click
            # reinitiate_button2 = page.locator('//*[@id="initiateResponseBody"]/tr[3]/td[3]/button')
            # if reinitiate_button2.is_visible(timeout=3000):
            #     reinitiate_button2.click()
            #     print("✅ Second button clicked.")
            # else:
            #     print("❌ Second button not visible.")
            #       # Wait for and click "initiate" button
            # if page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
            #     page.locator('//*[@id="initiate"]').click()
            #     print("✅ hello 4")
            #     # page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
            #     # page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()
            #     page.locator('xpath=/html/body/div[11]/div[7]/div/button').wait_for(timeout=5000)
            #     page.locator('xpath=/html/body/div[11]/div[7]/div/button').click()

            # # Wait for and click "dayClose" button
            # if page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
            #     page.locator('//*[@id="dayClose"]').click()


            reinitiate_button1 = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[3]/button')
            if reinitiate_button1.is_visible(timeout=3000):
                reinitiate_button1.click()
                print("✅ First button clicked.")
            else:
                print("❌ First button not visible.")

            # Wait for the second button to be visible, then click
            reinitiate_button2 = page.locator('//*[@id="initiateResponseBody"]/tr[3]/td[3]/button')
            if reinitiate_button2.is_visible(timeout=3000):
                reinitiate_button2.click()
                print("✅ Second button clicked.")
            else:
                print("❌ Second button not visible.")
            # Wait for and click "initiate" button
            if page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
                page.locator('//*[@id="initiate"]').click()
                print("✅ hello 5.")
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()

            # Wait for and click "dayClose" button
            if page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
                page.locator('//*[@id="dayClose"]').click()





        else:

            reinitiate_button1 = page.locator('//*[@id="initiateResponseBody"]/tr[1]/td[3]/button')
            if reinitiate_button1.is_visible(timeout=3000):
                reinitiate_button1.click()
                print("✅ First button clicked.")
            else:
                print("❌ First button not visible.")

            # Wait for the second button to be visible, then click
            reinitiate_button2 = page.locator('//*[@id="initiateResponseBody"]/tr[3]/td[3]/button')
            if reinitiate_button2.is_visible(timeout=3000):
                reinitiate_button2.click()
                print("✅ Second button clicked.")
            else:
                print("❌ Second button not visible.")
            # Wait for and click "initiate" button
            if page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
                page.locator('//*[@id="initiate"]').click()
                print("✅ hello 5.")
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()

            # Wait for and click "dayClose" button
            if page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
                page.locator('//*[@id="dayClose"]').click()

            # Wait for and click "initiate" button
            if page.locator('//*[@id="initiate"]').is_visible(timeout=3000):
                page.locator('//*[@id="initiate"]').click()
                print("✅ hello 6.")
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/div/span').click()
                page.locator('xpath=//*[@id="wrapper"]/ul/li[1]/ul/li[1]/ul/li[2]/a/span').click()

            # Wait for and click "dayClose" button
            if page.locator('//*[@id="dayClose"]').is_visible(timeout=3000):
                page.locator('//*[@id="dayClose"]').click()


        page.wait_for_timeout(2000)
        page.screenshot(path="screenshot.png")
        browser.close()