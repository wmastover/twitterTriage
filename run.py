from getIntros import getIntros
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from twitterLogon import twitterLogon
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from emailAlerts import sendEmail
import time

def run():

    # Mac OS Version

    chromedriver = ChromeDriverManager().install()
    driver = webdriver.Chrome(chromedriver )

    # Raspberry Pi Version
    
    # webdriver_options = Options()
    # webdriver_service = Service('/usr/lib/chromium-browser/chromedriver')
    # driver = webdriver.Chrome(service=webdriver_service, options=webdriver_options)


    driver.get("https://twitter.com/login")

    twitterLogon("wmabetting@gmail.com", "FrontdoorWill",  "Frontdoor2023", driver)

    getIntros(driver, "followers.csv")


while True:      
    try: 
        sendEmail("Restart", "We have just relaunched the triage system", "")
        run()

    except:
        print("crash")
        sendEmail("Crash Report", "Top level crash, waiting 30 seconds then relaunching", "")
        time.sleep(30)
