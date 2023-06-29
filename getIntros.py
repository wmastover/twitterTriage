import time 
from selenium.webdriver.common.by import By
from saveAsCSV import saveAsCSV
from readCSV import readCSV
from getGPTResponse import getOneLine
from emailAlerts import sendEmail
from Triage import triage

#go through an autotrader search and get the   

def getArticleBody(driver, element):

    def getAllText(element):
        if element.text:
            yield element.text
        for child in element.find_elements(By.XPATH, "./*"):
            yield from getAllText(child)

    text_content = list(getAllText(element))
    final_list = []
    for fragment in text_content:
            if fragment not in final_list:
                final_list.append(fragment)
            
    print(final_list)
    formatted_text = f"""\n""".join(final_list)
    return final_list[0].replace("\n", "")



def getIntros(driver, followers):
    
    filename = "outreachList.csv"

    accounts = readCSV(followers)
    
    try:
        usersOutreach = readCSV(filename)
    except: 
        usersOutreach = []

    # count used to send updates every 1000 accounts
    count = 0
    for index, account in enumerate(accounts):
        
        # skip any accounts that are already done
        if account[1] != "done":

            count = count + 1
            # send alerts
            if count == 1000:
                subject = str(index) + " Accounts Triaged"
                sendEmail(subject, " ", "outreachList.csv")
                count = 0 


            print(account[0])
            print("is not done")

            driver.get(account[0])

            time.sleep(5)

            userName = account[0].replace("https://twitter.com/","")

            try:
                
                # If this fails, try block will exit, hacky but it workds
                DMElement = driver.find_element(By.XPATH, '//div[@data-testid="sendDMFromProfile"]')          
                
                timeline = driver.find_element(By.XPATH, '//div[starts-with(@aria-label, "Timeline:")]')

                # get list of elements containing the tweet information
                tweetsList = timeline.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')

                # get user description / bio
                userDescriptionContainer = driver.find_element(By.XPATH, './/div[@data-testid="UserDescription"]')

                userDescription = getArticleBody(driver, userDescriptionContainer)

                passed = triage(userDescription)

                if passed:
                        

                    # create tweets section of query
                    queryText =  f"""

                            User Name: {userName}

                            User Description: {userDescription}

                    """

                    for x in tweetsList:
                        
                        # get the username from the tweet (incase its an RT)
                        try:
                            tweetUser = x.find_element(By.XPATH, './/div[@data-testid="User-Name"]//a').get_attribute("href")

                            # get the text of the tweet
                            tweetText = x.find_element(By.XPATH, './/div[@data-testid="tweetText"]//span').text

                        except:
                            tweetText = ""
                            tweetUser = ""

                        
                        # check if the user
                        if tweetUser == account[1]:
                            
                            queryText =  queryText + f"""

                            User Tweet: {tweetText}

                            """

                        
                    oneLine = getOneLine(queryText)

                    accounts[index][1] = "done"
                    saveAsCSV(accounts, followers)

                    usersOutreach.append([account[0], userDescription, oneLine])
                    saveAsCSV(usersOutreach, filename)
                    
                else:
                    accounts[index][1] = "done"
                    saveAsCSV(accounts, followers)

                    
   
            except Exception as e:
                print(f"An error occurred: {e}")
                accounts[index][1] = "done"
                saveAsCSV(accounts, followers)
        else:
            print(account[0])
            print("= to done")
    
    sendEmail("List Finished", "please add a new list of accounts to triage, finished list attached", "outreachList.csv")

    
            
