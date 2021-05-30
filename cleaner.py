import re
import preprocessor as p#forming a separate feature for cleaned tweets
import string
import nltk
from nltk.corpus import stopwords

def txt_cleaner(text):
        
        text = text.encode(encoding="ascii", errors="ignore")
        text = text.decode() # removing unicode from the text 
        
        text = p.clean(text)
        
        text = text.lower() #lowering all the text
        
        punct = set(string.punctuation)
        text = "".join([ch for ch in text if ch not in punct]) #remove punctation
        
        stop_words = set(stopwords.words("english"))
        text = " ".join([word for word in text.split() if word not in stop_words]) #remove stopwords
        # try out stemming and lemmatization
        return text