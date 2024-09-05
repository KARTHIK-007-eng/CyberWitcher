import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
import tor
def get_undetected_webdriver():
    """
    Initializes and returns an undetected Chrome WebDriver instance configured to use the Tor network as a SOCKS5 proxy.
    """
    options = uc.ChromeOptions()

    # Set up Tor as a SOCKS5 proxy
    tor_proxy = "socks5://127.0.0.1:9050"
    options.add_argument(f"--proxy-server={tor_proxy}")
    
    # Optional: Disable WebRTC to prevent IP leaks
    options.add_argument("--disable-webrtc")
    
    # options.add_argument("--headless")
    driver = uc.Chrome(options=options)

    return driver

def check_gmail( email):
    driver=get_undetected_webdriver()
    driver.get("https://mail.google.com/")

    # Locate the email input field, input the email, and submit
    email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)

    # Wait for the page to load
    time.sleep(randint(1,4))

    # Locate the password input field, input the password, and submit
    password_input = driver.find_element(By.TAG_NAME, 'h1')
    if(password_input=="Welcome" or "Verify" in password_input):
        print("your email address is found on gmail....")
    else:
        print("Email address is not found....")
    # Wait for login to complete
    time.sleep(5)

def main():
    
    email=str(input("Enter your email >>> "))
    if email is None:
        print("Please set your EMAIL and PASSWORD as environment variables.")
        return

    

    try:
        tor.start_tor()
        time.sleep(randint(1,4))
        check_gmail( email)
        time.sleep(randint(1,5))
        tor.stop_tor()
    except:
        print("Error occurred while checking Gmail")
        
#C:\Users\dinku\OneDrive\Desktop\Tor Browser\Browser\TorBrowser\Tor

if __name__ == "__main__":
    main()
