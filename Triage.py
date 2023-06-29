

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
    


import nltk
import re
import emoji
from nltk.corpus import words
from emailAlerts import sendEmail

# Ensure NLTK corpus is downloaded
nltk.download('words')

def isEnglish(input_string):
    # Define set of English words
    english_words = set(words.words())
    
    # Demojize emojis and remove them
    input_string = emoji.demojize(input_string)
    input_string = re.sub(r':[^:]*:', '', input_string)
    
    # Remove numbers surrounded by spaces
    input_string = re.sub(r'\s+\d+\s+', ' ', input_string)
    
    # Remove words that start with @
    input_string = re.sub(r'\s?@\w+', '', input_string)

    print(input_string)
    # Use regex to remove non-alphabetic characters and split into words
    words_in_input = re.findall(r'\b\w+\b', input_string.lower())
    
    # Count the number of words in the string
    total_words = len(words_in_input)
    
    # Count the number of English words in the string
    english_word_count = sum(word in english_words for word in words_in_input)
    
    # Return True if the majority of words are English, False otherwise
    return english_word_count / total_words > 0.3 if total_words > 0 else False


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
            print("failed Triage, sending email")
            body = "foreign language detected in bio:  \n\n" + bio
            sendEmail("foriegn language detection check", body, "")

            return(False)
        
