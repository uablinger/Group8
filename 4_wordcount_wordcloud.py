import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import re, prettytable

# Import csv file and dump NA rows with dropna
# header important
data_file = pd.read_csv("filename.csv", sep=",").dropna()

text = " ".join(data_file['text'].values.astype(str))

#cleanse text
no_urls_no_tags = " ".join([word for word in text.split(" ")
                                if 'http' not in word
                                    and 'amp' not in word
                                    and 'GlobalGoals' not in word
                                    and not word.startswith('@')
                                    and word != 'RT'
                                ])

# script to find the k most frequent words

from collections import Counter
 
# split() returns list of all the words in the string
split_it = no_urls_no_tags.split()

stop_words = ['the', 'if', 'of', 'be', 'to', 'for','a','and','is','in','to','no','one']
words = no_urls_no_tags

c = Counter(split_it)
c = Counter({k: v for k, v in c.items() if k not in stop_words})

pt = prettytable.PrettyTable(['Words', 'Counts'])
pt.align['Words'] = 'l'
pt.align['Counts'] = 'r'
for row in c.most_common(15):
    pt.add_row(row)

print(pt)

#make a worldcloud - (lower max_font_size)
wordcloud = WordCloud(max_words=100, max_font_size=60, width=1600, height=800, background_color='white').generate(no_urls_no_tags)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()