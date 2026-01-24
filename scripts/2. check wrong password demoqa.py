from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--log-level=3')


options.add_experimental_option("excludeSwitches", ["enable-logging"])

ser = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=options)



driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/login")
    
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userName']"))).send_keys("testuser")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='password']"))).send_keys("wrong_password")
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login"))).click()
    
    
    try:
        wait.until(EC.url_contains("profile"))
        print("Login succeeded")
    
    except:
        error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#name"))).text
        print(error_msg)
        assert error_msg == "Invalid username or password!", "Unexpected error message."
    
except Exception as e:
    print("Error:", e)
    
finally:
    time.sleep(3)
    driver.quit()