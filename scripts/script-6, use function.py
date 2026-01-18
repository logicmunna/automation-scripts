from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import traceback

# function 1, browser setup
def setup_driver():
    options= Options()
    options.add_argument('--log-level=3')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(r"C:\chromedriver\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    return driver

# function 2, Scroll to State-City Section
def scroll(driver, wait):
    section = wait.until(EC.presence_of_element_located((By.ID, "stateCity-wrapper")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",section)


def select_and_click(wait, state_name, city_name):
    wait.until(EC.element_to_be_clickable((By.ID, "state"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{state_name}']"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "city"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{city_name}']"))).click()

def type_state_city(wait,state_text, city_text):
    state_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-3-input")))
    state_input.send_keys(state_text)
    state_input.send_keys(Keys.ENTER)
    
    city_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
    city_input.send_keys(city_text)
    city_input.send_keys(Keys.ENTER)


driver= setup_driver()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    print("Website opened")

    # function calls
    scroll(driver, wait)
    select_and_click(wait, "Haryana", "Karnal")

    driver.refresh()
    scroll(driver, wait)
    type_state_city(wait, "NCR", "Delhi")

    driver.refresh()
    scroll(driver, wait)
    select_and_click(wait, "Uttar Pradesh", "Lucknow")

    print("All state-city selections completed successfully")

except Exception as e:
    print("Error occurred:", e)
    traceback.print_exc()

finally:
    driver.quit()
    print("Browser closed")
