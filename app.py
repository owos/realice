import numpy as np
import pandas as pd
import streamlit as st
import plotly as px
import plotly.express as express
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
import plotly.graph_objects as go
from wordcloud import STOPWORDS
from plots import real_words
from notebook import data
from notebook import data2
from notebook import data3
from notebook import  data4

st.set_page_config(layout='wide')
np.random.seed(43)
st.title('Team Johnson Sirleaf: Realice')

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






with st.sidebar:
    st.title('Team Johnson Sirleaf: Realice')
    st.subheader('The project aims at analyzing the feelings of Nigerian citizens’ on the current state of the Nigerian Security Force. It was done to honour those who died of the brutality of security forces and also the men in uniforms who died in their line of duty.')

with st.container():
    col1, col2, = st.columns(2)

    with col1:

        st.subheader('Frequency of Positive Police Encounter')
        fig = go.Figure(data)                    
        fig.update_layout(barmode = 'group', )
        fig.update_xaxes(title_text="Age Range")
        config = {'displayModeBar' : False}
        st.plotly_chart(fig, use_container_width=True)
        # 
                
        st.subheader('Frequency of Negative Police Encounter')
        fig3 = go.Figure(data2)                    
        fig3.update_layout(barmode = 'group')
        fig3.update_xaxes(title_text="Age Range")

        st.plotly_chart(fig3, use_container_width=True)#

        wcc = WordCloud(width=550, height=330, max_words=50, background_color="white", colormap = "plasma").generate_from_frequencies(real_words)
        plt.figure(figsize=(12, 14))
        fig, ax = plt.subplots()
        fig2 =express.imshow(wcc)
        fig2.update_xaxes(visible=False)
        fig2.update_yaxes(visible=False)
        st.subheader('Word Cloud of Top 50 One Word to Describe the Police')
        st.plotly_chart(fig2)
        

    with col2:

        st.subheader('Counts of Personal Police Harassment by Year')
        fig4 = go.Figure(data3)                    
        fig4.update_layout(barmode = 'group' )
        fig4.update_xaxes(title_text="Year")
        #For you to take a look at the result use
        st.plotly_chart(fig4, use_container_width=True)

        st.subheader('Counts of Others Police Harassment by Year')
        fig5 = go.Figure(data4)                    
        fig5.update_layout(barmode = 'group')
        fig5.update_xaxes(title_text="Year")  
        st.plotly_chart(fig5, use_container_width=True)  
        
        

        
