#Import necessary libaries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

#Function Definitaions
def setup_driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(r"C:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def go_to_login_page(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Login page loaded")
    
def enter_username(driver, username):
    username_field= wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(0.5)
    
def enter_password(driver, password):
    password_field= wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(0.5)
    
def click_submit_button(driver):
    submit_button= wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()
    print("Login form submitted")
    time.sleep(1)
    
def verify_successful_login(driver, wait):
    try:
        success_message= wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "post-title")))
        message_text = success_message.text.strip()
        
        if "Logged In Successfully" in message_text:
            print(message_text)
        else:
            print(message_text)
            return False
        
        current_url = driver.current_url
        if "logged-in-successfully" in current_url:
            print(current_url)
        else:
            print(current_url)
        
        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        if logout_button.is_displayed():
            print("Logout button is displayed")
        else:
            print("Logout button is not displayed")
            return False
        return True
    except Exception as e:
        print(f"Login verification failed: {e}")
        return False
    
def verify_failed_login(driver, wait):
    try:
        error_message= wait.until(EC.visibility_of_element_located((By.ID, "error")))
        
        if error_message.is_displayed():
            print(f"Error message displayed: {error_message.text.strip()}")
        else:
            print("Error message not displayed")
            return False
        
        if "invalid" in error_message.text.lower():
            print("Error message text is correct")
        else:
            print(f"Unexpected error message text: {error_message.text.strip()}")
            return False
        
        current_url = driver.current_url
        if "practice-test-login" in current_url:
            print(f"Same page URL after failed login: {current_url}")
        else:
            print(f"Unexpected URL after failed login: {current_url}")
            return False
        return True
    
    except Exception as e:
        print(f"Failed login verification error: {e}")
        return False
    
def test_valid_login(driver, wait):
    print("\n" + "="*50)
    print("টেস্ট ১: সঠিক Credential দিয়ে Login")
    print("="*50)
    
    go_to_login_page(driver)
    enter_username(driver, "student")
    enter_password(driver, "Password123")
    click_submit_button(driver)
        
    if verify_successful_login(driver, wait):
        print("Valid login test passed")
        return True
    else:
        print("Valid login test failed")
        return False
    
def test_invalid_password(driver, wait):
    print("\n"+"="*50)
    print("টেস্ট ২: ভুল Password দিয়ে Login")
    print("="*50)
    
    go_to_login_page(driver)
    enter_username(driver, "student")
    enter_password(driver, "WrongPassword")
    click_submit_button(driver)
    
    if verify_failed_login(driver, wait):
        print("Invalid password test passed")
        return True
    else:
        print("Invalid password test failed")
        return False
    
def test_invalid_username(driver, wait):
    print("\n"+"="*50)
    print("টেস্ট ৩: ভুল Username দিয়ে Login")
    print("="*50)
    
    go_to_login_page(driver)
    enter_username(driver, "wronguser")
    enter_password(driver, "Password123")
    click_submit_button(driver)
    
    if verify_failed_login(driver, wait):
        print("Invalid username test passed")
        return True
    else:
        print("Invalid username test failed")
        return False
    
driver = setup_driver()
wait = WebDriverWait(driver,15)



test_results = []



try:
    result1 = test_valid_login(driver, wait)
    test_results.append(("Valid Login Test", result1))
    time.sleep(2)
    
    result2 = test_invalid_password(driver, wait)
    test_results.append(("Invalid Password Test", result2))
    time.sleep(2)
    
    result3 = test_invalid_username(driver, wait)
    test_results.append(("Invalid Username Test", result3))
    time.sleep(2)
    
    print("\nFinal Test Results:")
    
    for test_name, result in test_results:
        status = "PASSED" if result else "FAILED"
        print(f"{test_name}: {status}")
    
    
    all_passed = all(result for _, result in test_results)
    if all_passed:
        print("\nAll login tests passed successfully.")
    else:
        print("\nSome tests failed:")
        
    time.sleep(3)
    
except Exception as e:
    print(f"\nError occurred: {e}")
    traceback.print_exc()
    
finally:
    driver.quit()
    print("Browser closed.")
        

    
    










