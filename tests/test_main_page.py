# tests/test_main_page.py
import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("driver")  # این دکوراتور fixture 'driver' از conftest.py را به تست تزریق می‌کند
class TestMainPage:

    def test_page_title(self, driver):
        """تست عنوان صفحه اصلی."""
        main_pg = MainPage(driver)
        main_pg.open()
        expected_title_partial = "Planingo"  # بخشی از تایتل یا تایتل کامل
        actual_title = main_pg.get_title()
        assert expected_title_partial in actual_title, \
            f"Expected title to contain '{expected_title_partial}' but got '{actual_title}'"

    def test_hero_section_elements_present(self, driver):
        """تست وجود عناصر کلیدی در بخش هیرو."""
        main_pg = MainPage(driver)
        main_pg.open()

        # بررسی عنوان اصلی
        hero_title = main_pg.get_hero_section_title_text()
        assert "AI-Powered Project Planning" in hero_title, \
            f"Hero title text is incorrect. Found: '{hero_title}'"

        # بررسی دکمه "Get Started Free"
        assert main_pg.is_element_visible(main_pg.GET_STARTED_FREE_BUTTON_HERO), \
            "Get Started Free button in hero section is not visible."

    def test_navigate_to_login_page(self, driver):
        """تست ناوبری به صفحه ورود."""
        main_pg = MainPage(driver)
        main_pg.open()
        main_pg.click_login_button()

        # منتظر می‌مانیم تا URL تغییر کند و حاوی 'login' شود
        assert main_pg.wait_for_url_contains("/login", timeout=10), \
            "URL did not change to login page."

        # (اختیاری) می‌توانید یک عنصر منحصر به فرد از صفحه ورود را هم بررسی کنید
        # login_page = LoginPage(driver) # اگر LoginPage را ساخته باشید
        # assert login_page.is_login_form_visible(), "Login form is not visible on login page"
        # برای اینکار باید LoginPage و لوکیتورهایش را هم تعریف کنید

    def test_navigate_to_features_page(self, driver):
        """تست ناوبری به صفحه Features."""
        main_pg = MainPage(driver)
        main_pg.open()
        main_pg.click_features_link()

        assert main_pg.wait_for_url_contains("/features", timeout=10), \
            "URL did not change to features page."
        # (اختیاری) بررسی یک عنصر در صفحه Features
        # features_page = FeaturesPage(driver)
        # assert features_page.is_some_feature_element_visible()

# برای اجرای تست‌ها، در ترمینال PyCharm (با محیط مجازی فعال) دستور زیر را وارد کنید:
# pytest
# یا برای گزارش HTML:
# pytest --html=report.html
#pytest
#pytest --html=report.html --self-contained-html