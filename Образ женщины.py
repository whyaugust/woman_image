#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


df=pd.read_csv('data',dtype={'age':str, 'race':str, 'shot':str, 'nudity':str, 'body':str, 'makeup':str,'skin':str, 'hair':str,})
df


# In[4]:


df['age'].value_counts()


# In[5]:


df['race'].value_counts()


# In[6]:


df['shot'].value_counts()


# In[7]:


df['nudity'].value_counts()


# In[8]:


df['body'].value_counts()


# In[9]:


df['makeup'].value_counts()


# In[10]:


df['skin'].value_counts()


# In[11]:


df['hair'].value_counts()


# In[12]:


df['body_settings'].value_counts()


# In[29]:


df['age'].value_counts().plot(kind='bar')


# In[30]:


df['race'].value_counts().plot(kind='bar')


# In[31]:


df['nudity'].value_counts().plot(kind='bar')


# In[32]:


df['body'].value_counts().plot(kind='bar')


# In[35]:


df['makeup'].value_counts().plot(kind='bar')


# In[36]:


df['skin'].value_counts().plot(kind='bar')


# In[37]:


df['hair'].value_counts().plot(kind='bar')

