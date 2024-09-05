from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.webdriver.common.by import By
# Use undetected ChromeDriver
def setup_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    
    # Enable headless mode if needed
    #options.add_argument("--headless")
    
    # Allow running less secure apps
    options.add_argument("--disable-logging")
    options.add_argument("--disable-gpu")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Create the WebDriver instance
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver


def check(username):
    print(f"[google] Process started for username: {username}...")
    driver=setup_driver()
    
    try:
        # Open Gmail about page
        url = "https://www.google.com/intl/en-US/gmail/about/"
        driver.minimize_window()
        driver.get(url)
        
        
        # Find and click the "Sign in" button
        print("[google] Navigating the page...")
        a_tag_element = driver.find_element(By.XPATH, '/html/body/header/div/div/div/a[2]')
        driver.get(a_tag_element.get_attribute('href'))

        # Enter the username in the email field
        print("[google] Wait......")
        email_field = driver.find_element(By.ID, "identifierId")
        email_field.send_keys(username)

        #click next
        driver.find_element(By.ID, "identifierNext" ).click()
        
        # Wait for the result page to load and check for username availability
        time.sleep(5)
        print("[google] Checking...")
        res = driver.find_element(By.ID, "headingText").text
        
        # Determine if the username exists
        if(res is not None):
            print(res)
            if (res == "Welcome"):
                print(f"[google]{username} is found.")
            else:
                print(f"{username} is not found.")
        else:
            print("Try again...")   
        time.sleep(10)
        
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except TimeoutException as e:
        print(f"Operation timed out: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        print("[google] Process completed.")


            
# Example usage
if __name__ == "__main__":
    username="dinkudeepak9391"  # Replace with desired username
    check(username)