from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import traceback

o=Options()
o.add_argument("--log-level=3")
o.add_experimental_option("excludeSwitches", ["enable-logging"])

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.goibibo.com/")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@role="presentation"]'))).click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'from')]"))).click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='From']"))).send_keys("ban")
    # time.sleep(3)
    # listItems= wait.until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@role="listbox"]//li')))
    # print("Total suggestions:", len(listItems))
    
    # for list in listItems:
    #     if "Bangladesh" in list.text:
    #         print(list.text)
    #         list.click()
    #         break
        
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'To')][1]"))).click()
    # wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='To']"))).send_keys("Ger")
    # time.sleep(3)
    # liItems= wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))
    # print("Total To Suggestions:", len(liItems))
    
    # for list in liItems:
    #     if "Frankfurt" in list.text:
    #         print(list.text)
    #         list.click()
    #         break
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Departure']"))).click()
    
    target_month="March 2026"
    terget_day="15"
    
    while True:
        month_text=wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='DayPicker-Caption']"))).text
        if target_month==month_text:
            break
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Next Month']"))).click()
        
        days = driver.find_elements(
        By.XPATH,"//div[@class='DayPicker-Body'][1]//div[contains(@class,'DayPicker-Day') and not(contains(@class,'outside'))]")

        print("Valid days:", len(days))


    
    
    
    

except Exception as e:
    print("Exception occurred:", str(e))
    traceback.print_exc()

finally:
    time.sleep(2)
    driver.quit()
