# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    کلاس پایه برای تمام Page Object ها.
    شامل متدهای عمومی برای تعامل با عناصر صفحه.
    """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://planingo.ai/" # URL اصلی سایت

    def open_url(self, url_path=""):
        """صفحه مورد نظر را باز می‌کند."""
        self.driver.get(self.base_url + url_path)

    def find_element(self, locator, timeout=10):
        """یک عنصر را پیدا کرده و برمی‌گرداند با انتظار مشخص."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")

    def find_elements(self, locator, timeout=10):
        """لیستی از عناصر را پیدا کرده و برمی‌گرداند."""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            raise TimeoutException(f"Elements with locator {locator} not found within {timeout} seconds.")

    def click(self, locator, timeout=10):
        """روی یک عنصر کلیک می‌کند."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text, timeout=10):
        """متنی را در یک فیلد ورودی تایپ می‌کند."""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """متن یک عنصر را برمی‌گرداند."""
        element = self.find_element(locator, timeout)
        return element.text

    def get_title(self):
        """عنوان صفحه فعلی را برمی‌گرداند."""
        return self.driver.title

    def is_element_visible(self, locator, timeout=5):
        """بررسی می‌کند آیا یک عنصر قابل مشاهده است."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, partial_url, timeout=10):
        """منتظر می‌ماند تا URL حاوی یک بخش مشخص شود."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(partial_url)
            )
            return True
        except TimeoutException:
            return False