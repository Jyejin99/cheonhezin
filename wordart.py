import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud

wiki = wikipedia.page('artificial intelligence')
txt = wiki.content

wordcloud = WordCloud(width=2000, height = 1500).generate(txt)

plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show()
