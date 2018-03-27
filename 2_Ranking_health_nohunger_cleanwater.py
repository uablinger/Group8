### SCRIPT FOR RANKING THE GOALS
import pandas as pd

# Import csv file and dump NA rows with dropna
# header important
data_file = pd.read_csv(filename.csv, sep=",").dropna()

#checking how many rows and columns are in the file to have an overview and possibility to check
print data_file.shape

# After dumping NA rows, index is currupted and is setup new
data_file.index = pd.RangeIndex(len(data_file.index))

# Define List of Keywords - all keywords from the list as defined
health_key = ["health", "wellbeing","goal3", "sdg3"]
cleanwater_key = ["cleanwater", "goal6","cleandrinkingwater", "worldwaterday", "sdg6", "worldwaterday", "sanitation"]
nohunger_key = ["nohunger","goal2","nutrition", "sdg2","zerohunger"]
    
# search for string in column "text" using contains function. join keywords with regex OR | using join()
#case=FALSE to include also capital letters
data_file["health"] = data_file["text"].str.contains("|".join(health_key),case=False)
data_file["cleanwater"] = data_file["text"].str.contains("|".join(cleanwater_key),case=False)
data_file["nohunger"] = data_file["text"].str.contains("|".join(nohunger_key),case=False)

#count times how often topic occurs
print data_file["health"].value_counts()[True]
print data_file["cleanwater"].value_counts()[True]
print data_file["nohunger"].value_counts()[True]

import matplotlib.pyplot as plt

un_goals = ["health", "cleanwater" , "nohunger"]
tweets_by_un_goals = [data_file["health"].value_counts()[True], data_file["cleanwater"].value_counts()[True], data_file["nohunger"].value_counts()[True]]

x_pos = list(range(len(un_goals)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_un_goals, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: health vs. cleanwater vs. nohunger', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(un_goals)
plt.grid()

plt.show()
