# pages/main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    """
    Page Object برای صفحه اصلی https://planingo.ai/
    """
    # --- Locators ---
    # این لوکیتورها باید با دقت از سایت استخراج شوند.
    # برای مثال، لوکیتور دکمه "Get Started Free"
    # با استفاده از Inspect Element در مرورگر می‌توانید لوکیتور مناسب (ID, Name, XPath, CSS_SELECTOR) را پیدا کنید.

    # مثال‌هایی از لوکیتورها (نیاز به بررسی و اصلاح دقیق دارند):
    LOGO_LINK = (By.XPATH, "//a[@aria-label='Planingo']")  # لوگوی سایت
    NAV_FEATURES_LINK = (By.LINK_TEXT, "Features")
    NAV_PRICING_LINK = (By.LINK_TEXT, "Pricing")
    NAV_BLOG_LINK = (By.LINK_TEXT, "Blog")
    NAV_CONTACT_US_LINK = (By.LINK_TEXT, "Contact Us")
    LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Login']")  # دکمه ورود
    SIGN_UP_BUTTON = (By.XPATH, "//a[normalize-space()='Sign Up for Free']")  # دکمه ثبت نام رایگان

    HERO_TITLE = (By.XPATH, "//h1[contains(text(),'AI-Powered Project Planning')]")  # عنوان اصلی صفحه
    GET_STARTED_FREE_BUTTON_HERO = (By.XPATH,
                                    "//a[contains(@class, 'bg-primary-600') and contains(text(), 'Get Started Free')]")  # دکمه اصلی در بخش هیرو

    # --- Actions ---
    def __init__(self, driver):
        super().__init__(driver)  # فراخوانی سازنده کلاس پدر (BasePage)

    def open(self):
        """صفحه اصلی را باز می‌کند."""
        super().open_url()  # از متد open_url در BasePage استفاده می‌کند

    def get_hero_section_title_text(self):
        """متن عنوان اصلی بخش هیرو را برمی‌گرداند."""
        return self.get_text(self.HERO_TITLE)

    def click_get_started_free_hero_button(self):
        """روی دکمه 'Get Started Free' در بخش هیرو کلیک می‌کند."""
        self.click(self.GET_STARTED_FREE_BUTTON_HERO)

    def click_login_button(self):
        """روی دکمه Login کلیک می‌کند."""
        self.click(self.LOGIN_BUTTON)

    def click_signup_button(self):
        """روی دکمه Sign Up کلیک می‌کند."""
        self.click(self.SIGN_UP_BUTTON)

    def click_features_link(self):
        self.click(self.NAV_FEATURES_LINK)

    def click_pricing_link(self):
        self.click(self.NAV_PRICING_LINK)

    # ... متدهای دیگر برای تعامل با سایر عناصر صفحه اصلی