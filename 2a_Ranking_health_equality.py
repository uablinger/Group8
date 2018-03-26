### SCRIPT FOR RANKING THE GOALS
import pandas as pd

# Import csv file and dump NA rows with dropna
# header important
data_file = pd.read_csv("filename.csv", sep=",").dropna()

# After dumping NA rows, index is currupted and is setup new
data_file.index = pd.RangeIndex(len(data_file.index))

# rename columns if you want to - in this case to make live easer with text column
data_file = data_file.rename(columns = {"Text":"text"})

# Define List of Keywords
health_key = ["health", "wellbeing","goal3", "sdg3","cleanwater", "goal6","cleandrinkingwater", "worldwaterday", "sdg6", "worldwaterday", "sanitation","nohunger","goal2","nutrition", "sdg2","zerohunger"]
equality_key = ["equalrights", "womenunited", "women", "goal5", "sdg5", "equality", "timeisnow", "sdggenderindex", "inequality", "IWD2018", "internationalwomensday", "womensday"]  
    
# test area starts here # search for string in column "text" using contains function. join keywords with regex OR | using join()
#case=FALSE to include also capital letters
data_file["health"] = data_file["text"].str.contains("|".join(health_key),case=False)
data_file["equality"] = data_file["text"].str.contains("|".join(equality_key),case=False)

#count times how often topic occurs
print data_file["health"].value_counts()[True]
print data_file["equality"].value_counts()[True]

import matplotlib.pyplot as plt

un_goals = ["health", "equality"]
tweets_by_un_goals = [data_file["health"].value_counts()[True], data_file["equality"].value_counts()[True]]

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