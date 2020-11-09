#!/usr/bin/env python
# coding: utf-8

# In[96]:


#print first 5 and last 7 records
import pandas as pd
df = pd.read_csv(r'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
df.head()


# In[2]:


df.tail(7)


# In[6]:


# print total records and type of variables
index = df.index
no_of_rows = len(index)
no_of_rows


# In[7]:


df.dtypes


# In[3]:


#Print the name of all the columns.
df.columns


# In[8]:


#How is the dataset indexed?
df.index


# In[74]:


#Which was the most ordered item? and How many items were ordered?
groupItem = df.groupby("item_name")
sumOfGroupedItem = groupItem.sum()
sumOfGroupedItem.sort_values('quantity', ascending=False).head(1)


# In[75]:


#What was the most ordered item in the choice_description column?
df.head()


# In[81]:


choiceGroup = df.groupby('choice_description')
sumchoice = choiceGroup.sum()
sumchoice.sort_values("quantity",ascending=False).head(1)


# In[82]:


#Turn the item price into a float
df.head()


# In[98]:


def strToFloat(str):
    return float(str[1:])
df['item_float'] = df['item_price'].apply(strToFloat)
df.head()


# In[103]:


#print a data frame with only two columns item_name and item_price
df[['item_name','item_price']]


# In[108]:


# delete the duplicates in item_name and quantity
dfCleaned = df.drop_duplicates(["item_name","quantity"])
dfCleaned


# In[134]:


# select only the products with quantity equals to 1
df[df["quantity"]==1]


# In[118]:


# select only the item_name and item_price columns
df[["item_name","item_price"]]


# In[144]:


# sort item from the most to less expensive
grouped = df.sort_values("item_float",ascending=False)
grouped.head()


# In[159]:


#What was the quantity of the most expensive item ordered?
grouped.head(1)[["quantity","item_name"]]


# In[166]:


#How many times were a Veggie Salad Bowl ordered?
print(str(len(df[df['item_name']=="Veggie Salad Bowl"]))+" Times")


# In[ ]:





# In[ ]:





# In[ ]:




