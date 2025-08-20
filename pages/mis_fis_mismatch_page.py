from utils.db import Database
from playwright.sync_api import Page

class MISFISMismatchPage:
    def __init__(self, page: Page):
        self.page = page

    def fix_mismatch_and_close(self, day_close_page) -> bool:
        """
        If MIS-FIS mismatch exists, fix DB directly, ensure Day Close is enabled, then click it.
        """
        try:
            mismatch_link = self.page.locator("#initiateResponseBody > tr:nth-child(3) > td:nth-child(2) >> a")

            if mismatch_link.count() > 0 and mismatch_link.is_visible(timeout=3000):
                print("🔗 MIS-FIS mismatch detected. Running DB fix...")

                # DB fix
                db = Database()
                disable_query = """
                    UPDATE mis_fis_coa_map SET domain_status_id=2 
                    WHERE particulars IN (
                        'Principal OS- Summery',
                        'Interest OS- Summery',
                        'Members Compulsory Savings',
                        'Term Savings',
                        'Members Amar Hishab Savings',
                        'Membership Fee',
                        'Insurance Premium-MF',
                        'Advance for Insurance Settlement (MF)',
                        'Members Voluntary Savings'
                    );
                """
                enable_query = disable_query.replace("2", "1")

                db.execute(disable_query)

                # Ensure Day Close is ready
                day_close_page.go_to_day_close()
                day_close_page.click_initiate()  # Re-initiate if needed

                # Click Day Close
                day_close_page.click_day_close()

                db.execute(enable_query)
                db.close()

                print("✅ MIS-FIS mismatch fixed and Day Close executed.")
                return True
            else:
                print("ℹ️ MIS-FIS mismatch link not found. Skipping DB fix.")
                return False

        except Exception as e:
            print(f"❌ Error during MIS-FIS mismatch fix: {e}")
            return False
