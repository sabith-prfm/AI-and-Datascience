#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv', sep=",")


# In[3]:


df.head()


# In[14]:


#Convert the type of the column Year to datetime64
df['Year']=pd.to_datetime(df['Year'])


# In[15]:


df.dtypes


# In[57]:


#Set the Year column as the index of the dataframe¶
df1 = df.set_index("Year")
df1.head()


# In[18]:


#Return the first 3 rows of the DataFrame df.
df.head(3)


# In[23]:


#Select just the 'Murder' and 'Robbery' columns from the DataFrame df and print first 5 rows
df[["Murder","Robbery"]].head()


# In[25]:


#Select the data in rows [3, 4, 8] and in columns ['Murder', 'Robbery']
df[["Murder","Robbery"]].iloc[[3,4,8]]


# In[28]:


#Select only the rows where the number of murder is greater than 24,000
df[df["Murder"] > 24000]


# In[56]:


#Select the rows the murder is between 20k and 24k (inclusive)
df[df["Murder"].between(20000,25000)].head()


# In[55]:


#Calculate the mean murder for each different year in df.
df.groupby('Year')["Murder"].mean().head()


# In[54]:


#Sort df first by the values in the 'Murder' in decending order, then by the value in the 'Violent'column in ascending order.
df.sort_values(by="Murder",ascending=False).head()


# In[53]:


df.sort_values(by='Violent', ascending=True).head()


# In[ ]:




