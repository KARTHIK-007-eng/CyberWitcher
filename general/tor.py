import subprocess
import platform
import time
import signal
import os
from proxy import proxy
import fake_agent
from random import choice
import requests
import time


tor_process = None
agent=fake_agent.fake_agent().user_agents


#it used to start the port
def start_tor():
    global tor_process
    os_name = platform.system()

    try:
        if os_name == "Linux":
            # Start Tor on Linux
            tor_process = subprocess.Popen(['sudo','apt','install','tor'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            tor_process = subprocess.Popen(['sudo','systemctl','start','tor'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            print("Tor has been started on Linux.")
        elif os_name == "Windows":
            path=str(input("Enter your tor file path >>>> "))
            # Start Tor on Windows (adjust path if needed)
            if(os.path.exists(path)):
                tor_path = f"{path}\\tor.exe"  # Adjust path if needed
                tor_process = subprocess.Popen([tor_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("Tor has been started on Windows.")
            else:
                print("Tor file not found.")
                exit()
        else:
            print("Unsupported operating system.")
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: Enter your correct path {e}")




#it is used to stop listening the port
def stop_tor():
    global tor_process
    if tor_process:
        try:
            if platform.system() == "Windows":
                # Terminate Tor on Windows
                tor_process.terminate()  # This is equivalent to sending a SIGTERM
            else:
                os.kill(tor_process.pid, signal.SIGTERM) 
            tor_process.wait() 
            print("Tor has been stopped.")
        except Exception as e:
            print(f"An error occurred while stopping Tor: {e}")
    else:
        print("No Tor process found to stop.")
    

#it conform port is listening
def check_listening():
    try:
        # Run the 'netstat -an | findstr 9050' command
        time.sleep(7)
        if(platform.system()=="Windows"):
            process = subprocess.Popen('netstat -an | findstr 9050', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            process = subprocess.Popen('netstat -an | grep 9050', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        stdout, stderr = process.communicate()

        if stdout:
            print("Port 9050 is in use:")
            print(stdout)
        else:
            print("Port 9050 is not in use.")

        if stderr:
            print("Errors:")
            print(stderr)

    except Exception as e:
        print(f"An error occurred: {e}")


#get the site name
def site_name(url):
    arr=url.split(".")
    return arr[1]


#send a request through tor proxy
def tor_request(url):
    
    try:
        response = requests.get(url, proxies=proxy, headers={'User-Agent': choice(agent)})
        if response.status_code == 200:
            print("Request successful")
            return response.status_code
        else:
            print(f"Received status code: {response.status_code}")
            return response.status_code
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return None


#tor_driver it helps to hide your identity
def tor_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    options = Options()
    
    # Enable headless mode if needed
    #options.add_argument("--headless")
    
    # Allow running less secure apps
    tor_proxy = "socks5://127.0.0.1:9050"
    options.add_argument(f"--proxy-server={tor_proxy}")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-gpu")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"--user-agent={choice(agent)}")
    # Create the WebDriver instance
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver


if __name__ == "__main__":
    start_tor()
    tor_driver()
    time.sleep(10)
    check_listening()
    print(tor_request(r"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/"))
    time.sleep(10)  # Adjust the time as needed for testing
    stop_tor()



#C:\Users\dinku\OneDrive\Desktop\Tor Browser\Browser\TorBrowser\Tor