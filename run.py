from codeLibraries.getIntros import getIntros
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from codeLibraries.twitterLogon import twitterLogon
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from codeLibraries.emailAlerts import sendEmail
import time

def run():

    # Mac OS Version
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"')  # Mimic a non-headless browser
    chrome_options.add_argument('window-size=1800x1000')  # Specify window size
    chrome_options.add_argument('--disable-extensions')  # Disable extensions
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration


    chromedriver = ChromeDriverManager().install()
    driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)

    # Raspberry Pi Version
    # webdriver_options = Options()
    # webdriver_options.add_argument("--headless")
    # chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"')  # Mimic a non-headless browser
    # chrome_options.add_argument('window-size=1800x1000')  # Specify window size
    # chrome_options.add_argument('--disable-extensions')  # Disable extensions
    # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
    # webdriver_service = Service('/usr/lib/chromium-browser/chromedriver')
    # driver = webdriver.Chrome(service=webdriver_service, options=webdriver_options)


    driver.get("https://twitter.com/login")

    twitterLogon("wmabetting@gmail.com", "FrontdoorWill",  "Frontdoor2023", driver)

    getIntros(driver, "./data/followers.csv")


while True:      
    try: 

        sendEmail("Restart", "We have just relaunched the triage system", "")
        run()

    except Exception as e:
     
        print("crash top level:   " + str(e))

        body = "Top level crash, waiting 30 seconds then relaunching: \n\n" + str(e) 

        sendEmail("Crash Report", body, "")
        time.sleep(30)
