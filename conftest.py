# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# from webdriver_manager.firefox import GeckoDriverManager # اگر از فایرفاکس استفاده می‌کنید

@pytest.fixture(scope="session")  # 'session' یعنی درایور برای کل تست‌ها یکبار ساخته و در انتها بسته می‌شود
def driver():
    # تنظیمات Chrome WebDriver با استفاده از webdriver-manager
    # به طور خودکار آخرین نسخه درایور کروم را دانلود و کش می‌کند
    service = ChromeService(ChromeDriverManager().install())

    # گزینه‌های کروم (اختیاری، اما مفید)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # باز شدن مرورگر به صورت تمام صفحه
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    # options.add_argument("--headless") # اجرای تست‌ها بدون باز شدن پنجره مرورگر (برای CI/CD)
    # options.add_argument("--no-sandbox") # اگر در محیط لینوکس یا Docker اجرا می‌کنید
    # options.add_argument("--disable-dev-shm-usage") # اگر در محیط لینوکس یا Docker اجرا می‌کنید

    # راه‌اندازی WebDriver
    # web_driver = webdriver.Chrome(service=service, options=options)

    # اگر می‌خواهید از فایرفاکس استفاده کنید:
    # service = FirefoxService(GeckoDriverManager().install())
    # web_driver = webdriver.Firefox(service=service)

    # ساده‌ترین حالت برای کروم:
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield web_driver  # درایور را برای استفاده در تست‌ها فراهم می‌کند

    # این قسمت بعد از اتمام تمام تست‌ها اجرا می‌شود
    web_driver.quit()