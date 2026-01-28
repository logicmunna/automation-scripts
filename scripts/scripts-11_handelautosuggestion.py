from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")

wait.until(EC.presence_of_element_located((By.ID, "tags"))).send_keys("S")
listItems = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@id="ui-id-1"]//li')))

print("Total suggestions:", len(listItems))
for item in listItems:
    print(item.text)
    if item.text == "Selenium":
        print("record found")
        item.click()
        break

time.sleep(2)
driver.quit()