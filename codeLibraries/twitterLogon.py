import time
from selenium.webdriver.common.by import By



def twitterLogon(email, username, password, driver):

    try:

        print("twitter logon started")

        driver.get("https://twitter.com/login")
        time.sleep(10)

        emailLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone, email, or username')]/ancestor::label[1]")

        emailInput = emailLabel.find_element( By.XPATH, ".//input[1]")

        emailInput.send_keys(email)

        time.sleep(1)

        nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

        nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

        nextButton.click()

        time.sleep(5)

        try:
            title = driver.find_element(By.XPATH, "//span[contains(text(), 'Enter your phone number or username')]")
            
            print("enter phone number or username found")

            usernameInput = driver.find_element(By.TAG_NAME, "input")

            usernameInput.send_keys(username)

            time.sleep(1)

            nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

            nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

            nextButton.click()



        except:
            print("phone number / username not requested")

        time.sleep(5)

        passwordLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Password')]/ancestor::label[1]")

        passwordInput = passwordLabel.find_element( By.XPATH, ".//input[1]")

        passwordInput.send_keys(password)

        time.sleep(1)

        LoginButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")

        LoginButton = LoginButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

        LoginButton.click()

        time.sleep(5)

        AcceptAllText = driver.find_element(By.XPATH, "//span[contains(text(), 'Accept all cookies')]")

        AcceptAllButton = AcceptAllText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

        AcceptAllButton.click()

        time.sleep(3)

        print("twitter logon ended")

    
    except Exception as e:
    # Code to handle the ValueError

        print("twitter logon failed")

        print(f"Twitter logon Error occurred: {str(e)}")
        
        