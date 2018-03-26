import csv
import pandas as pd
import re
from unidecode import unidecode

data_file = pd.read_csv("filename.csv", sep=",").dropna()
text_s = data_file['text']
# check lines for comparison with final sentiment analysis result
#print text_s.shape

text_s = text_s.str.decode('utf8')
text_s = text_s.apply(unidecode)
#old text_regex = re.compile(r'[^a-zA-Z\s]')
text_regex = re.compile('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)')
text_s = text_s.str.replace(text_regex, " ")
#check text 
#print text_s.head()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

sentiment_analysis = {"positive":0,"neutral":0,"negative":0}
for x in text_s: 
    ss = analyzer.polarity_scores(x)
    if ss["compound"] == 0.0: 
        sentiment_analysis["neutral"] +=1
    elif ss["compound"] > 0.0:
        sentiment_analysis["positive"] +=1
    else:
        sentiment_analysis["negative"] +=1
print sentiment_analysis


import matplotlib.pyplot as plt

# making a pie chart:
labels = ['positive', 'neutral', 'negative']
sizes = [(sentiment_analysis["positive"]), (sentiment_analysis["neutral"]), (sentiment_analysis["negative"])]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.show()