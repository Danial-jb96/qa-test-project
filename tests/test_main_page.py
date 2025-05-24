# tests/test_main_page.py
import pytest
from pages.main_page import MainPage


# from selenium.webdriver.common.by import By # اگر در تست‌ها لوکیتور مستقیم استفاده می‌کنید

class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup_page(self, driver):
        self.main_pg = MainPage(driver)
        self.main_pg.open()

    def test_01_page_title_and_logo(self):
        """تست عنوان صفحه و نمایش لوگو."""
        expected_full_title = "Planingo - Your Free AI Travel Planner for Personalized Itineraries"
        actual_title = self.main_pg.get_title()
        assert actual_title == expected_full_title, \
            f"Expected full title to be '{expected_full_title}' but got '{actual_title}'"

        assert self.main_pg.is_element_visible(
            self.main_pg.LOGO_LINK), "Planingo logo in nav is not visible."  # از لوکیتور اصلاح شده استفاده می‌کنیم

    def test_02_hero_section_elements_present(self):
        """تست وجود عناصر کلیدی در بخش هیرو."""
        # بررسی عنوان اصلی Hero
        assert self.main_pg.is_element_visible(self.main_pg.HERO_TITLE), "Hero title is not visible."

        hero_title_text = self.main_pg.get_hero_title_text()
        expected_hero_text_part = "Travel Better with PlaninGo"  # بخشی از متن که انتظار داریم
        assert expected_hero_text_part in hero_title_text, \
            f"Hero title text mismatch. Expected to contain '{expected_hero_text_part}', got '{hero_title_text}'"

        # بررسی تب Trip Planner (به جای دکمه Get Started Free قبلی)
        assert self.main_pg.is_element_visible(self.main_pg.TRIP_PLANNER_TAB), \
            "'Trip Planner' tab is not visible."
        # می‌توانید وجود دکمه Search را هم بررسی کنید
        assert self.main_pg.is_element_visible(self.main_pg.SEARCH_BUTTON_TRIP_PLANNER), \
            "'Search' button in Trip Planner form is not visible."

    def test_03_navigation_to_login_page(self):  # این تست به "Sign in" تغییر می‌کند
        """تست ناوبری به صفحه ورود از طریق دکمه نویگیشن."""
        self.main_pg.click_nav_login_button()  # این متد باید لوکیتور Sign in را کلیک کند
        # URL صفحه لاگین را باید بررسی کنید که چیست
        assert self.main_pg.wait_for_url_contains("/login", timeout=10) or \
               self.main_pg.wait_for_url_contains("/signin", timeout=10), \
            "URL did not change to login/signin page after clicking nav sign in button."

    # تست SIGN_UP_BUTTON_NAV فعلا باید کامنت یا حذف شود چون لوکیتورش مشخص نیست
    # def test_04_navigation_to_signup_page_from_nav(self): ...

    # تست HERO_GET_STARTED_FREE_BUTTON هم باید تغییر کند یا حذف شود
    # def test_05_navigation_to_signup_page_from_hero(self): ...

    def test_06_navigation_to_features_page(self):
        """تست ناوبری به صفحه Features."""
        self.main_pg.click_nav_features_link()
        assert self.main_pg.wait_for_url_contains("/features", timeout=10), \
            "URL did not change to features page."

    def test_07_navigation_to_pricing_page(self):
        """تست ناوبری به صفحه Pricing."""
        self.main_pg.click_nav_pricing_link()
        assert self.main_pg.wait_for_url_contains("/pricing", timeout=10), \
            "URL did not change to pricing page."

    def test_08_navigation_to_blogs_page(self):  # به Blogs تغییر نام یافت
        """تست ناوبری به صفحه Blogs."""
        self.main_pg.click_nav_blog_link()  # این متد باید لوکیتور Blogs را کلیک کند
        assert self.main_pg.wait_for_url_contains("/blog", timeout=10), \
            "URL did not change to blog page."  # یا /blogs، باید چک شود

    def test_09_navigation_to_creators_page(self):  # به Creators تغییر نام یافت
        """تست ناوبری به صفحه Creators."""
        self.main_pg.click_nav_contact_us_link()  # این متد حالا باید Creators را کلیک کند
        assert self.main_pg.wait_for_url_contains("/creators", timeout=10), \
            "URL did not change to creators page."  # URL را چک کنید

    def test_11_footer_privacy_policy_link(self):
        """تست کلیک روی لینک Privacy Policy در فوتر."""
        self.main_pg.click_footer_privacy_policy()
        assert self.main_pg.wait_for_url_contains("/privacy-policy", timeout=10), \
            "URL did not change to privacy policy page."
        assert "Privacy Policy" in self.main_pg.get_title(), "Privacy Policy page title is incorrect."