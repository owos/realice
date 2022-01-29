

# In[1]:


# the dependencies
import os
import numpy as np
import pandas as pd


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

from wordcloud import WordCloud, STOPWORDS


# In[2]:


# Ensure Reproducibility
np.random.seed(10) 


path = 'data/project_realice_clean_final.csv'
fileName = 'project_realice_clean_final'

# since file is already downloaded already opened as a CSV file, then import as such.
try:
    df_pol = pd.read_csv(f"{path}{fileName}.zip")
except:
    df_pol = pd.read_csv("data/project_realice_clean_final.csv")


# In[4]




# In[5]:


df_pol.drop('Unnamed: 0', axis=1, inplace=True)
df_pol.columns


# In[6]:


df_pol['right_viol_day'].value_counts()


# In[7]:


#rename column from long name to q1, q2, q3, etc.
df_pol.rename(columns= {"age_range":'age_range', '#NAME?' : '+exp_np', '#NAME?.1': '+exp_np_unit', '#NAME?.2': '+exp_np_describe',
                        '#NAME?.3': '-exp_np', '#NAME?.4': '-exp_np_unit', '#NAME?.5': '-exp_np_describe', 'harass_np': 'harass_exp',
                        'harass_np_year':'harass_np_year', 'haras_np_day':'harass_np_day', 'right_viol_day':'right_viol_day', 
                        'right_viol_place':'right_viol_place', 'confidence_level_np':'confidence_level_np',
                        'one_word' : 'one_word', 'suggestions':'suggestions'}, inplace = True)
df_pol.columns = df_pol.columns.str.lower()



# In[8]:


print(df_pol.shape)


# In[9]:


#look at the columns
df_pol.columns.to_list()


# In[10]:


#covert columns names into strings
df_pol.columns = list(map(str, df_pol.columns))

#Chart Type 1/2

# Here is my selected Dataframe to visualise
df_vis_1 = df_pol[['age_range','+exp_np']]
df_vis_2 = df_pol[['age_range','-exp_np']]
df_vis_3 = df_pol[['+exp_np', '+exp_np', '+exp_np_unit']]
df_vis_4 = df_pol[[ '-exp_np_unit']]
final_data = df_pol
#import library
import plotly.graph_objects as go
                    
# Create data frame 
df_vis_1 = df_pol[['age_range','+exp_np']]
#Cross-tabulate the example data frame.
df_cross = pd.crosstab(df_pol['age_range'],df_pol['+exp_np'])
# initiate data list for figure
data = []
#use for loop on every +exp_np to create bar data
for x in df_cross.columns:
   data.append(go.Bar(name=str(x), x=df_cross.index, y=df_cross[x]))

##beautify the code basis 
data = data
fig = go.Figure(data, layout_title_text="Frequency of Positive Police Encounter")                    
fig.update_layout(barmode = 'group', )
fig.update_xaxes(title_text="Age Range")
#For you to take a look at the result use
#fig.show(width=800, height=1600)


# In[12]:


#import library
import plotly.graph_objects as go
                    
# Create data frame 
df_vis_2 = df_pol[['age_range','-exp_np']]
#Cross-tabulate the example data frame.
df_cross_2 = pd.crosstab(df_pol['age_range'],df_pol['-exp_np'])
# initiate data list for figure
data_2 = []
#use for loop on every -exp_np to create bar data
for x in df_cross_2.columns:
   data_2.append(go.Bar(name=str(x), x=df_cross_2.index, y=df_cross_2[x]))

##beautify the code basis 
data2 = data_2
fig = go.Figure(data, layout_title_text="Frequency of Negative Police Encounter")                    
fig.update_layout(barmode = 'group' )
fig.update_xaxes(title_text="Age Range")
#For you to take a look at the result use
#fig.show(width=800, height=1600)


# In[13]:


#import library
import plotly.graph_objects as go
                    
# Create data frame 
df_vis_3 = df_pol[['harass_exp','harass_np_year']] 
#Cross-tabulate the example data frame.
df_cross_3 = pd.crosstab(df_pol['harass_exp'],df_pol['harass_np_year'])
# initiate data list for figure
data_3 = []
#use for loop on every -exp_np to create bar data
for x in df_cross_3.columns:
   data_3.append(go.Bar(name=str(x), x=df_cross_3.index, y=df_cross_3[x]))

##beautify the code basis 
data3 = data_3
fig = go.Figure(data_3, layout_title_text="Counts of Personal Police Harassment by Year")                    
fig.update_layout(barmode = 'group', )
fig.update_xaxes(title_text="Year")
#For you to take a look at the result use
#fig.show(width=800, height=1600)


#import library
                    
# Create data frame 
df_vis_4 = df_pol[['right_viol','right_viol_year']]  

#Cross-tabulate the example data frame.
df_cross_4 = pd.crosstab(df_pol['right_viol'],df_pol['right_viol_year'])
# initiate data list for figure
data_4 = []
#use for loop on every -exp_np to create bar data
for x in df_cross_4.columns:
   data_4.append(go.Bar(name=str(x), x=df_cross_4.index, y=df_cross_4[x]))

##beautify the code basis 
data4 = data_4
fig = go.Figure(data_4, layout_title_text="Counts of Others Police Harassment by Year")                    
fig.update_layout(barmode = 'group', )
fig.update_xaxes(title_text="Year")
#For you to take a look at the result use
#fig.show(width=800, height=1600)