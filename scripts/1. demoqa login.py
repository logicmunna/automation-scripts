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
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demoqa.com/login")
    
    username= wait.until(EC.presence_of_element_located((By.ID, "userName")))
    username.clear()
    username.send_keys("testuser")
    
    password= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
    password.send_keys("Test@123")
    
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='login']")))
    login_button.click()

    time.sleep(5)
    print(driver.current_url)
    assert "profile" in driver.current_url, "Login failed or did not redirect to profile page."
    
except Exception as e:
    print("Error:", e)
    
finally:
    time.sleep(3)
    driver.quit()