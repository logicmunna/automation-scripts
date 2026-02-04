from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import traceback
from openpyxl import Workbook
import os

o=Options()
o.add_argument("--log-level=3")
o.add_experimental_option("excludeSwitches", ["enable-logging"])

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.amazon.com/")
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue shopping"]'))).click()
    except:
        pass
    wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search")]'))).send_keys("Samsung Phone")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))).click()
    time.sleep(3)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="brandsRefinements"]//span[text()="Samsung"]'))).click()
    time.sleep(3)

    phones=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'puis-line-clamp')]//span")))
    prices=wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="a-price-whole"]')))

    listphones=[]
    listprices=[]

    for price in prices:
        listprices.append(price.text)

    for phone in phones:
        listphones.append(phone.text)

    final = zip(listphones, listprices)

    print("Part 1")

    wb = Workbook()
    wb['Sheet'].title = "Samsung Phones"
    ws = wb.active
    ws.append(["Phone Name", "Price"])

    for i in list(final):
        ws.append(i)

    wb.save("FinalRecords.xlsx")
    print("Part 2")
    print("Excel file location:", os.path.abspath("FinalRecords.xlsx"))


except Exception as e:
    print("Exception occurred:", str(e))
    traceback.print_exc()

finally:
    time.sleep(2)
    driver.quit()
