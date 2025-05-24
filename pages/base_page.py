# pages/base_page.py
import time  # برای ایجاد تاخیر کوتاه جهت مشاهده هایلایت
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://planingo.ai/"

    def open_url(self, url_path=""):
        self.driver.get(self.base_url + url_path)

    def _highlight(self, element, effect_time=0.3, color="red", border_px=3):
        """عنصر را با یک کادر رنگی هایلایت می‌کند."""
        original_style = element.get_attribute("style")  # استایل فعلی را ذخیره می‌کنیم

        # اعمال استایل هایلایت
        self.driver.execute_script(
            f"arguments[0].style.border='{border_px}px solid {color}'; arguments[0].style.boxShadow='0 0 10px {color}';",
            element
        )

        if effect_time > 0:
            time.sleep(effect_time)  # تاخیر برای مشاهده هایلایت

        # برگرداندن استایل به حالت اولیه (مهم برای جلوگیری از تاثیر روی تست‌های بعدی)
        # self.driver.execute_script("arguments[0].style.border=arguments[1]; arguments[0].style.boxShadow=arguments[2];",
        #                            element,
        #                            original_style.split('border:')[1].split(';')[0] if 'border:' in original_style else '',
        #                            original_style.split('box-shadow:')[1].split(';')[0] if 'box-shadow:' in original_style else '')
        # ساده‌تر: فقط استایل‌هایی که اضافه کردیم را پاک می‌کنیم اگر بخواهیم دقیق‌تر باشیم.
        # برای سادگی، فعلا فرض می‌کنیم که بعد از تعامل، استایل یا صفحه تغییر می‌کند.
        # یک راه حل ساده‌تر برای برگرداندن استایل، اگر فقط border اضافه کرده باشیم:
        self.driver.execute_script("arguments[0].style.border=arguments[1]; arguments[0].style.boxShadow=arguments[2];",
                                   element,
                                   original_style.split('border:')[1].split(';')[
                                       0].strip() if 'border:' in original_style else "none",
                                   original_style.split('box-shadow:')[1].split(';')[
                                       0].strip() if 'box-shadow:' in original_style else "none"
                                   )
        # اگر original_style خالی بود، یعنی هیچ استایل inlineی نداشت، پس border و boxShadow را none می‌کنیم.
        if not original_style:
            self.driver.execute_script("arguments[0].style.border='none'; arguments[0].style.boxShadow='none';",
                                       element)

    def find_element(self, locator, timeout=10, highlight=False):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            if highlight:
                self._highlight(element)
            return element
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")

    def find_elements(self, locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            raise TimeoutException(f"Elements with locator {locator} not found within {timeout} seconds.")

    def click(self, locator, timeout=10, highlight_before_click=True):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            if highlight_before_click:
                self._highlight(element, effect_time=0.2)  # زمان کمتر برای کلیک
            element.click()
        except ElementNotInteractableException:
            # گاهی اوقات المنت توسط چیز دیگری پوشانده شده، جاوااسکریپت کلیک می‌تواند کمک کند
            print(f"Element {locator} not interactable, trying JS click.")
            element = self.find_element(locator, highlight=False)  # فقط پیداش کن
            if highlight_before_click:
                self._highlight(element, effect_time=0.2)
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not clickable within {timeout} seconds.")

    def type_text(self, locator, text, timeout=10, highlight_before_type=True):
        element = self.find_element(locator, timeout)  # اول پیداش کن
        if highlight_before_type:
            self._highlight(element)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10, highlight_before_get=True):
        element = self.find_element(locator, timeout)
        if highlight_before_get:
            self._highlight(element, effect_time=0.1, color="blue")  # رنگ متفاوت برای get_text
        return element.text

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator, timeout=5, highlight_if_visible=True):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            if highlight_if_visible:
                self._highlight(element, effect_time=0.2, color="green")
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, partial_url, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(partial_url)
            )
            return True
        except TimeoutException:
            return False