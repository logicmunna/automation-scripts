from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('--log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

ser = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=options)

driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    print("Website Open Done")
    
    sports= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')))
    sports.click()
    time.sleep(1)
    
    reading= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]')))
    reading.click()
    time.sleep(1)
    
    music= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]')))
    music.click()
    time.sleep(1)
    
    #Mandatory Fields
    driver.find_element(By.ID, "firstName").send_keys("Mashfi")
    driver.find_element(By.ID, "lastName").send_keys("Ahamed")
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="gender-radio-1"]'))).click()
    
    driver.find_element(By.ID, "userNumber").send_keys("0123456789")
    
    
    
    submit= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit')))
    
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",submit)
    time.sleep(1)
    
    try:
        submit.click()
    except:
        driver.execute_script("arguments[0].click();", submit)
    
    success_message = wait.until(EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    assert "Thanks for submitting the form" in success_message.text , "Form submission failed"

    
except Exception as e:
    print("Error:", e)

finally:
    time.sleep(3)
    driver.quit()
    print("Browser Closed ")