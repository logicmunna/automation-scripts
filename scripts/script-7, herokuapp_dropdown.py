# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import traceback


# Function Definitions
def setup_driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(r"C:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def human_wait(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

def get_dropdown(driver, wait, locator_type, locator_value):
     element = wait.until(EC.presence_of_element_located((locator_type, locator_value)))
     return Select(element)
 
def select_by_index(dropdown, index):
    dropdown.select_by_index(index)
    
def select_by_value(dropdown, value):
    dropdown.select_by_value(value)

def select_by_text(dropdown, text):
    dropdown.select_by_visible_text(text)
    
def get_selected_option(dropdown):
    return dropdown.first_selected_option.text

def get_all_options(dropdown):
    return [option.text for option in dropdown.options]

def select_random_option(dropdown):
    options = dropdown.options[1:]
    random_option = random.choice(options)
    dropdown.select_by_visible_text(random_option.text)


# Main Script
driver = setup_driver()
wait = WebDriverWait(driver,10)

try:
    driver.get("https://the-internet.herokuapp.com/dropdown")
    print("Website loaded")
    human_wait()
    
    dropdown = get_dropdown(driver, wait, By.ID, "dropdown")
    
    all_options = get_all_options(dropdown)
    print(f'Available options: {all_options}')
    human_wait()
    
    # Select by index
    select_by_index(dropdown, 1)
    print(f'Selected: {get_selected_option(dropdown)}')
    human_wait()
    
    #select by value
    select_by_value(dropdown, "2")
    print(f'Selected: {get_selected_option(dropdown)}')
    human_wait()
    
    # Select by visible text
    select_by_text(dropdown, "Option 1")
    print(f'Selected: {get_selected_option(dropdown)}')
    human_wait()
    
    # Select random option
    select_random_option(dropdown)
    print(f'Selected: {get_selected_option(dropdown)}')
    human_wait()
    
    #All methods test
    test_methods= [
        ("Index", lambda: select_by_index(dropdown, 1)),
        ("Value", lambda: select_by_value(dropdown, "2")),
        ("Text", lambda: select_by_text(dropdown, "Option 1")),
        ("Random", lambda: select_random_option(dropdown))
        
    ]
    
    for method_name, method_func in test_methods:
        method_func()
        print(f"{method_name}: {get_selected_option(dropdown)}")
        human_wait(0.5, 1.5)
        
    print("All tests completed successfully.")
    time.sleep(3)
    
except Exception as e:
    print(f'Error occurred: {e}')
    traceback.print_exc()
    
finally:
    driver.quit()
    print("Browser closed.")