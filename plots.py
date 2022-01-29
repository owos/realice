import numpy as np
import pandas as pd
#import streamlit as st
import plotly as px
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
from wordcloud import STOPWORDS
np.random.seed(43)



def clean_text(text):
    #Remove RT
    text = re.sub(r'RT', '', text)
    
    #Fix &
    text = re.sub(r'&amp;', '&', text)
    
    #Remove punctuations
    text = re.sub(r'[?!.;&/:,#@-]', '', text)
  

    #Convert to lowercase to maintain consistency
    text = text.lower()
    return text

def gen_freq(text):
    #Will store the list of words
    word_list = []

    #Loop over all the tweets and extract words into word_list
    for tw_words in text.split():
        word_list.extend(tw_words)

    #Create word frequencies using word_list
    #print(word_list)
    word_freq = pd.Series(word_list).value_counts()

    #Print top 20 words
    word_freq[:20]
    
    return word_freq


df= pd.read_csv(r'data/project_realice_clean_final.csv')

print(df.head())
df["one_word"].fillna('None', inplace =True)
one_word = df["one_word"].apply(lambda x: clean_text(x))

one_word_freq = gen_freq(one_word.str)
one_word = df["one_word"].apply(lambda x: clean_text(x))
one_word_freq = gen_freq(one_word.str)
real_words = one_word_freq.drop(labels= STOPWORDS, errors= 'ignore')
wcc = WordCloud(width=550, height=330, max_words=50, background_color="white", colormap = "plasma").generate_from_frequencies(real_words)
plt.figure(figsize=(12, 14))
fig, ax = plt.subplots()
plt.imshow(wcc, interpolation='bilinear')
plt.title('Word Cloud of Top 50 words in Jobs Dataset', fontsize = 20)
plt.axis('off')