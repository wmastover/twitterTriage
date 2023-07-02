from langdetect import detect
import re
import emoji


def check_keywords(input_string):
    keywords = ['VC', 'Angel', 'investor']
    found_keywords = []

    for word in keywords:
        if word.lower() in input_string.lower():
            found_keywords.append(word)

    if len(found_keywords) > 0:
        return(True)
    else:
        return(False)
    



def isEnglish(input_string):
    # Demojize emojis and remove them
    input_string = emoji.demojize(input_string)
    input_string = re.sub(r':[^:]*:', '', input_string)
    
    # Remove numbers surrounded by spaces
    input_string = re.sub(r'\s+\d+\s+', ' ', input_string)
    
    # Remove words that start with @
    input_string = re.sub(r'\s?@\w+', '', input_string)
    
    # Remove hashtags
    input_string = re.sub(r'#\w+', '', input_string)
    
    # Remove emails
    input_string = re.sub(r'\S+@\S+', '', input_string)

    # Detect the language of the cleaned string
    try:
        language = detect(input_string)
    except:
        language = "unknown"

    # Return True if the detected language is English, False otherwise
    return language == 'en'


def triage(bio):

    keyWordFound =  check_keywords(bio)
    
    if keyWordFound:
        return(False)

    else:
        correctLanguage = isEnglish(bio)

        if correctLanguage:
            print("passed Triage")
            return(True)
    
        else:
            print("failed Triage, adding to list")

            return(False)
        
