from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())), options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.quit()

obj1 = ChromeDriverManager()
print(obj1)
path = obj1.install()
print(path)
driver = webdriver.Chrome(service=(Service(path)), options=options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.quit()
