import csv
import pandas as pd
import re
from unidecode import unidecode

# Import csv file and dump NA rows with dropna
# header important
data_file = pd.read_csv("filename.csv", sep=",").dropna()

#checking how many rows and columns are in the file to have an overview and possibility to check
print data_file.shape

# rename columns if you want to - in this case to make live easer with text column
data_file = data_file.rename(columns = {"Text":"text"})

# After dumping NA rows, index is currupted and is setup new
data_file.index = pd.RangeIndex(len(data_file.index))

# Define List of Keywords
health_key = ["health", "wellbeing","goal3", "sdg3""cleanwater", "goal6","cleandrinkingwater", "sdg6", "worldwaterday", "sanitation", "nohunger","goal2","nutrition", "sdg2","zerohunger"]
equality_key = ["equalrights", "womenunited", "women", "goal5", "sdg5", "equality", "timeisnow", "sdggenderindex", "inequality", "IWD2018", "internationalwomensday", "womensday"]  
    
# test area starts here # search for string in column "text" using contains function. join keywords with regex OR | using join()
#case=FALSE to include also capital letters
data_file["health"] = data_file["text"].str.contains("|".join(health_key),case=False)
data_file["equality"] = data_file["text"].str.contains("|".join(equality_key),case=False)

#defining a dataframe
df = pd.DataFrame(data_file, columns = ['Datetime','text','health','equality'])
#print dataframe in case you wanna visualize it for checking purposes
#print df

#condition: tweet must be made by a verified user and containing health goal health | cleanwater | nohunger
equality_text = df[(df['equality'] == True)]

text_s = equality_text['text']
#print text_s

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