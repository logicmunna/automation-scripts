#import necessary libaries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.facebook.com/")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Create new account']"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys("Sunny")
    wait.until(EC.presence_of_element_located((By.NAME, "lastname"))).send_keys("Kowshal")
    day = Select(wait.until(EC.element_to_be_clickable((By.ID, "day"))))
    day.select_by_visible_text("10")
    month = Select(wait.until(EC.element_to_be_clickable((By.ID, "month"))))
    month.select_by_value("7")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "year")))).select_by_visible_text("1995")
    gender_male = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "reg_email__"))).send_keys("sunny@gmail.com")
    wait.until(EC.presence_of_element_located((By.ID, "password_step_input"))).send_keys("Sunn y@1 ]234")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='websubmit' and @type='submit']"))).click()
    time.sleep(5)
    
except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()

finally:
    driver.quit()
    print("Browser closed.")
