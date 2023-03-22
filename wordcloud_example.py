import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys
import os
os.chdir(sys.path[0])


# read Text
text = open('jeff_bezos_speech.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS
print(stopwords)

wc = WordCloud(
    background_color='white',
    stopwords=stopwords,
    height=600,
    width=400
)

wc.generate(text)

wc.to_file('wordcloud_output.png')
