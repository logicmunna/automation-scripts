from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

ser = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=options)

driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    
    # Form Fillup Code Here
    first_name= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#firstName")))
    first_name.send_keys("Ifat Jahan")
    last_name= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='lastName']")))
    last_name.send_keys("Jihad")
    
    email= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#userEmail")))
    email.send_keys("sunnyhossain@example.com")
    
    gender= wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']")))
    gender.click()
    
    phone_number= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#userNumber")))
    phone_number.send_keys("1231231230")
    
    dob= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'date')]")))
    dob.click()
    year_select= wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@class, 'year')]")))
    year_dropdown= Select(year_select)
    year_dropdown.select_by_visible_text("2000")
    month_select= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[class*='month']")))
    month_dropdown= Select(month_select)
    month_dropdown.select_by_visible_text("April")
    day_select= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and text()='16']")))
    day_select.click()
    
    subjects=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#subjectsInput")))
    for subject in ["Maths", "Physics", "Chemistry"]:
        subjects.send_keys(subject)
        subjects.send_keys(Keys.ENTER)
    
    hobby1= wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='hobbies-checkbox-1']/following-sibling::label")))
    hobby2= wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Reading']")))
    hobby2.click()
    hobby1.click()
    
    photo= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="uploadPicture"]')))
    photo.send_keys(r"d:\Downloads\ifat.jpg")
    
    address= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#currentAddress")))
    address.send_keys("Simla Vila, Gandhi Road, Kurgaon-99001")
    
    state= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Select State')]")))
    state.click()
    state_update= wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Uttar Pradesh")]')))
    state_update.click()
    
    city= wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Select City")]')))
    city.click()
    city_update= wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Lucknow")]')))
    city_update.click()
    
    submit= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit")))
    submit.click()
    
    submitted_text= wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "modal-title") or contains(@class, "h4")]')))
    assert submitted_text.text == "Thanks for submitting the form", "Form submission failed"
    print("Form Submitted Successfully:", submitted_text.text)

except Exception as e:
    print("Error:", e)
    
finally:
    time.sleep(3)
    driver.quit()