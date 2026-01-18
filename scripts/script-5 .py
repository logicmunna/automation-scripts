from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument('--log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    print("Website Open Done")

    state_city_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#stateCity-wrapper')))
    driver.execute_script("arguments[0].scrollIntoView(true);",state_city_section)
    time.sleep(2)

    state_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "state")))
    state_dropdown.click()
    state_option= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Haryana']")))
    state_option.click()

    city_dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'city')))
    city_dropdown.click()
    city_option= wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Karnal"]')))
    city_option.click()
    time.sleep(2)

    driver.refresh()

    state_city_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#stateCity-wrapper')))
    driver.execute_script("arguments[0].scrollIntoView(true);",state_city_section)
    time.sleep(2)

    state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
    state_input.send_keys("NCR")
    time.sleep(1)
    state_input.send_keys(Keys.ENTER)

    city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
    city_input.send_keys("Delhi")
    time.sleep(1)
    city_input.send_keys(Keys.ENTER)

    driver.refresh()
    time.sleep(2)

    state_city_section = wait.until(EC.presence_of_element_located((By.ID, 'stateCity-wrapper')))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",state_city_section)
    time.sleep(2)

    state_container = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#state")))
    state_container.click()

    uttar_pradesh = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Uttar Pradesh']")))
    uttar_pradesh.click()
    time.sleep(1)

    city_container = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#city")))
    city_container.click()
    
    lucknow = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Lucknow']")))
    lucknow.click()
    time.sleep(2)
    
    print("\n All methods executed successfully!")
    time.sleep(1)   

except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
    print("Browser Closed")
