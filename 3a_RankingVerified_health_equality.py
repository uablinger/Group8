import pandas as pd

# Import csv file and dump NA rows with dropna
# header important
data_file = pd.read_csv("filename.csv", sep=",").dropna()

#checking how many rows and columns are in the file to have an overview and possibility to check
print data_file.shape

# After dumping NA rows, index is currupted and is setup new
data_file.index = pd.RangeIndex(len(data_file.index))

# Define List of Keywords
health_key = ["health", "wellbeing","goal3", "sdg3", "worldwaterday", "cleanwater", "goal6","cleandrinkingwater", "sdg6", "worldwaterday", "sanitation", "nohunger","goal2","nutrition", "sdg2","zerohunger"]
equality_key = ["equalrights", "womenunited", "women", "goal5", "sdg5", "equality", "timeisnow", "sdggenderindex", "inequality", "IWD2018", "internationalwomensday", "womensday"]  
    
# test area starts here # search for string in column "text" using contains function. join keywords with regex OR | using join()
#case=FALSE to include also capital letters
data_file["health"] = data_file["text"].str.contains("|".join(health_key),case=False)
data_file["equality"] = data_file["text"].str.contains("|".join(equality_key),case=False)

#defining a dataframe
df = pd.DataFrame(data_file, columns = ['Datetime', 'Text','verified','health','equality'])
#print dataframe in case you wanna visualize it for checking purposes
#print df

#condition: tweet must be made by a verified user and containing health goal health | cleanwater | nohunger
verified_health = df[(df['verified'] == True) &  (df['health'] == True)]
verified_equality = df[(df['verified'] == True) &  (df['equality'] == True)]
#For checking purposes:
#print verified_health

#show number of tweets from verified persons per topic
print len(verified_health)
print len(verified_equality)


import matplotlib.pyplot as plt

un_goals = ["health", "equality"]
tweets_by_un_goals = [(len(verified_health)), (len(verified_equality))]

x_pos = list(range(len(un_goals)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_un_goals, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: health vs. equality', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(un_goals)
plt.grid()

plt.show()