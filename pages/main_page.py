# pages/main_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # --- Locators for Planingo.ai Main Page (Please verify and update these) ---
    LOGO_LINK = (By.XPATH, "//a[@aria-label='Planingo']")

    # Navigation Links
    NAV_BAR = (By.XPATH, "//header//nav")  # برای اطمینان از اینکه لینک‌های داخل نوبار اصلی هستند
    NAV_FEATURES_LINK = (By.XPATH, "//nav//a[normalize-space()='Features']")
    NAV_PRICING_LINK = (By.XPATH, "//nav//a[normalize-space()='Pricing']")
    NAV_BLOG_LINK = (By.XPATH, "//nav//a[normalize-space()='Blog']")
    NAV_CONTACT_US_LINK = (By.XPATH, "//nav//a[normalize-space()='Contact us']")  # "us" با حرف کوچک است در سایت

    # Authentication Buttons in Nav
    LOGIN_BUTTON_NAV = (By.XPATH, "//nav//a[normalize-space()='Login']")
    SIGN_UP_BUTTON_NAV = (By.XPATH, "//nav//a[normalize-space()='Sign Up for Free']")

    # Hero Section
    HERO_TITLE  = (By.XPATH, "//h1[contains(normalize-space(.), 'Travel Better with PlaninGo')]")
    HERO_SUBTITLE = (By.XPATH, "//p[contains(text(), 'Streamline your project management with AI-driven insights')]")
    HERO_GET_STARTED_FREE_BUTTON = (By.XPATH,
                                    "//div[h1[contains(text(),'AI-Powered Project Planning')]]//a[contains(text(),'Get Started Free')]")  # دکمه زیر عنوان اصلی
    HERO_WATCH_DEMO_BUTTON = (
    By.XPATH, "//div[h1[contains(text(),'AI-Powered Project Planning')]]//a[contains(text(),'Watch Demo')]")

    # Footer Links (Example - you can add more)
    FOOTER_PRIVACY_POLICY_LINK = (By.XPATH, "//footer//a[normalize-space()='Privacy Policy']")

    # --- Actions for Main Page ---
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open_url()
        # ممکن است بخواهید منتظر بارگذاری کامل یک عنصر کلیدی بمانید
        self.find_element(self.HERO_TITLE, timeout=15)  # منتظر عنوان اصلی بمان

    def get_hero_title_text(self):
        return self.get_text(self.HERO_TITLE)

    def get_hero_subtitle_text(self):
        return self.get_text(self.HERO_SUBTITLE)

    def click_hero_get_started_button(self):
        self.click(self.HERO_GET_STARTED_FREE_BUTTON)

    def click_hero_watch_demo_button(self):
        # این دکمه یک پاپ‌آپ ویدیو باز می‌کند، تست آن نیاز به مدیریت پاپ‌آپ دارد
        # فعلا فقط کلیک می‌کنیم
        self.click(self.HERO_WATCH_DEMO_BUTTON)
        # برای بستن پاپ آپ ویدیو (اگر iframe نباشد و دکمه بستن داشته باشد)
        # close_button_locator = (By.XPATH, "...") # لوکیتور دکمه بستن ویدیو
        # self.click(close_button_locator)
        # یا اگر iframe است، باید به iframe سوییچ کنید.

    def click_nav_login_button(self):
        self.click(self.LOGIN_BUTTON_NAV)

    def click_nav_signup_button(self):
        self.click(self.SIGN_UP_BUTTON_NAV)

    def click_nav_features_link(self):
        self.click(self.NAV_FEATURES_LINK)

    def click_nav_pricing_link(self):
        self.click(self.NAV_PRICING_LINK)

    def click_nav_blog_link(self):
        self.click(self.NAV_BLOG_LINK)

    def click_nav_contact_us_link(self):
        self.click(self.NAV_CONTACT_US_LINK)

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO_LINK)

    def click_footer_privacy_policy(self):
        # ممکن است نیاز به اسکرول به پایین صفحه باشد تا لینک فوتر دیده شود
        element = self.find_element(self.FOOTER_PRIVACY_POLICY_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # کمی صبر برای اتمام اسکرول
        self.click(self.FOOTER_PRIVACY_POLICY_LINK)