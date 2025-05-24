# tests/test_main_page.py
import pytest
from pages.main_page import MainPage


# @pytest.mark.usefixtures("driver") # این دیگر لازم نیست اگر driver را به هر تست پاس می‌دهیم
class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup_page(self, driver):
        """این فیکسچر برای هر تست در این کلاس، MainPage را آماده می‌کند."""
        self.main_pg = MainPage(driver)
        self.main_pg.open()  # صفحه اصلی را در ابتدای هر تست باز می‌کند

    def test_01_page_title_and_logo(self):
        """تست عنوان صفحه و نمایش لوگو."""
        expected_title_keyword = "Planingo"
        actual_title = self.main_pg.get_title()
        assert expected_title_keyword in actual_title, \
            f"Expected title to contain '{expected_title_keyword}' but got '{actual_title}'"

        assert self.main_pg.is_logo_visible(), "Planingo logo is not visible."

    def test_02_hero_section_content(self):
        """تست محتوای بخش هیرو (عنوان و زیرعنوان)."""
        expected_hero_title = "AI-Powered Project Planning"
        actual_hero_title = self.main_pg.get_hero_title_text()
        assert expected_hero_title in actual_hero_title, \
            f"Hero title mismatch. Expected to contain '{expected_hero_title}', got '{actual_hero_title}'"

        expected_hero_subtitle_keyword = "Streamline your project management"
        actual_hero_subtitle = self.main_pg.get_hero_subtitle_text()
        assert expected_hero_subtitle_keyword in actual_hero_subtitle, \
            f"Hero subtitle mismatch. Expected to contain '{expected_hero_subtitle_keyword}', got '{actual_hero_subtitle}'"

        assert self.main_pg.is_element_visible(self.main_pg.HERO_GET_STARTED_FREE_BUTTON), \
            "Hero 'Get Started Free' button is not visible."
        assert self.main_pg.is_element_visible(self.main_pg.HERO_WATCH_DEMO_BUTTON), \
            "Hero 'Watch Demo' button is not visible."

    def test_03_navigation_to_login_page(self):
        """تست ناوبری به صفحه ورود از طریق دکمه نویگیشن."""
        self.main_pg.click_nav_login_button()
        assert self.main_pg.wait_for_url_contains("/login", timeout=10), \
            "URL did not change to login page after clicking nav login button."
        # برای اطمینان بیشتر، می‌توانید یک عنصر از صفحه لاگین را هم چک کنید
        # مثلا: assert self.main_pg.is_element_visible((By.ID, "email_input_field_on_login_page"))

    def test_04_navigation_to_signup_page_from_nav(self):
        """تست ناوبری به صفحه ثبت نام از طریق دکمه نویگیشن."""
        self.main_pg.click_nav_signup_button()
        assert self.main_pg.wait_for_url_contains("/register", timeout=10), \
            "URL did not change to register page after clicking nav sign up button."
        # بررسی کنید URL صفحه ثبت نام در Planingo چیست (ممکن است /signup یا /register باشد)
        # با بررسی سایت، URL به /register می‌رود.

    def test_05_navigation_to_signup_page_from_hero(self):
        """تست ناوبری به صفحه ثبت نام از طریق دکمه 'Get Started Free' در بخش Hero."""
        self.main_pg.click_hero_get_started_button()
        assert self.main_pg.wait_for_url_contains("/register", timeout=10), \
            "URL did not change to register page after clicking hero 'Get Started Free' button."

    def test_06_navigation_to_features_page(self):
        """تست ناوبری به صفحه Features."""
        self.main_pg.click_nav_features_link()
        assert self.main_pg.wait_for_url_contains("/features", timeout=10), \
            "URL did not change to features page."
        # می‌توانید عنوان صفحه Features یا یک عنصر خاص آن را بررسی کنید
        # assert "Features" in self.main_pg.get_title()

    def test_07_navigation_to_pricing_page(self):
        """تست ناوبری به صفحه Pricing."""
        self.main_pg.click_nav_pricing_link()
        assert self.main_pg.wait_for_url_contains("/pricing", timeout=10), \
            "URL did not change to pricing page."
        # assert "Pricing" in self.main_pg.get_title()

    def test_08_navigation_to_blog_page(self):
        """تست ناوبری به صفحه Blog."""
        self.main_pg.click_nav_blog_link()
        assert self.main_pg.wait_for_url_contains("/blog", timeout=10), \
            "URL did not change to blog page."
        # assert "Blog" in self.main_pg.get_title()

    def test_09_navigation_to_contact_us_page(self):
        """تست ناوبری به صفحه Contact Us."""
        self.main_pg.click_nav_contact_us_link()
        assert self.main_pg.wait_for_url_contains("/contact", timeout=10), \
            "URL did not change to contact us page."
        # assert "Contact" in self.main_pg.get_title()

    # @pytest.mark.skip(reason="Watch Demo opens a video modal, needs specific handling for modal.")
    # def test_10_watch_demo_button_opens_modal(self):
    #     """تست کلیک روی دکمه Watch Demo و باز شدن مدال ویدیو."""
    #     self.main_pg.click_hero_watch_demo_button()
    #     # در اینجا باید بررسی کنید که مدال ویدیو باز شده است.
    #     # این بستگی به ساختار HTML مدال دارد.
    #     # مثال: video_modal_locator = (By.XPATH, "//div[@id='video-modal-id']")
    #     # assert self.main_pg.is_element_visible(video_modal_locator, timeout=5), \
    #     #     "Video modal did not appear after clicking 'Watch Demo'."
    #     # سپس باید راهی برای بستن مدال هم داشته باشید تا تست‌های بعدی مختل نشوند.

    def test_11_footer_privacy_policy_link(self):
        """تست کلیک روی لینک Privacy Policy در فوتر."""
        self.main_pg.click_footer_privacy_policy()
        assert self.main_pg.wait_for_url_contains("/privacy-policy", timeout=10), \
            "URL did not change to privacy policy page."
        assert "Privacy Policy" in self.main_pg.get_title(), "Privacy Policy page title is incorrect."

# برای اجرای تست‌ها:
# در ترمینال با محیط مجازی فعال:
# pytest
# یا
# pytest -v (برای نمایش جزئیات بیشتر)
# یا برای گزارش HTML:
# pytest --html=report.html --self-contained-html