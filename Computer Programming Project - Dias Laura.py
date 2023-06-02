#!/usr/bin/env python
# coding: utf-8

# # Emotional Flexibility

# ### Introduction

# The following script is an analysis of behavioral data collected in the context of an experiment on Emotional Flexibility. 
# 
# In the experiment the participants are presented with several pairs images of different emotional valences (emotionally positive or negative). The first picture of the pair is a cropped picture and the second is the full picture. Sometimes the emotional valence changes between pictures and other times it doesn't, following no specific pattern. Emotional flexibility is the ability to correctly perceive and adapt to novel emotional stimuli and is quantified by the switch cost mean which we measured during this experiment. 
# 
# In this analysis, it is possible to visualize the Switch cost mean and the Depression, Anxiety and Stress scores (from the DASS-21 Questionnaire). 
# 

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('new_data_python.csv')

print(data)


# In[7]:


print(data.head())
print(data.describe())
print(data.info())


# In[8]:


data=data.dropna()
data=data.drop_duplicates()


# ### Variation of the Switch cost mean

# This boxplot shows the variation of the Switch cost mean in the group of participants.
# 
# 

# In[47]:


# Customizing the boxplot
plt.boxplot(data['Switch cost mean'], boxprops={'color': 'red'}, whiskerprops={'color': 'blue', 'linewidth': 2, 'linestyle': '--'},
            medianprops={'color': 'green'})
plt.xticks([], [])
plt.title('Switch Cost Mean', fontsize=14)

#Displaying the plot
plt.show()


# ### Comparisson of the Depression Anxiety and Stress Sores (DASS)

# This section shows the Boxplots for the Depression, Anxiety and Stress Scores, which might have an influence on the individual's emotional flexibility.
# 
# 

# In[46]:


fig, axs = plt.subplots(1, 3, figsize=(12, 6))

axs[0].boxplot(data['DASS_D'], boxprops={'color': 'red'}, whiskerprops={'color': 'blue', 'linewidth': 2, 'linestyle': '--'},
            medianprops={'color': 'green'})
axs[0].set_xticks([]) 
axs[0].set_ylim(-2, 16)
axs[0].set_title('Depression Score')


axs[1].boxplot(data['DASS_A'], boxprops={'color': 'red'}, whiskerprops={'color': 'blue', 'linewidth': 2, 'linestyle': '--'},
            medianprops={'color': 'green'})
axs[1].set_xticks([]) 
axs[1].set_ylim(-2, 16)
axs[1].set_title('Anxiety Score')


axs[2].boxplot(data['DASS_S'], boxprops={'color': 'red'}, whiskerprops={'color': 'blue', 'linewidth': 2, 'linestyle': '--'},
            medianprops={'color': 'green'})
axs[2].set_xticks([]) 
axs[2].set_ylim(-2, 16)
axs[2].set_title('Stress Score')


# In[ ]:




