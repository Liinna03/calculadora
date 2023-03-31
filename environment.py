from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--no-sandbox")  # bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("headless")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    url_test = context.config.userdata.get("url_iu")
    context.driver.get(url_test)


def after_scenario(context, scenario):
    context.driver.close()