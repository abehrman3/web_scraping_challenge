#!/usr/bin/env python
# coding: utf-8

# # Scraping with Pandas

# In[17]:


import pandas as pd


# In[18]:

def scrape_table():

    table_url = 'https://space-facts.com/mars/'


    # In[19]:


    table = pd.read_html(table_url)
    table


    # In[20]:


    df=table[0]
    df.head()


    # In[21]:


    df = df.drop(columns="Earth")
    df.columns=[' ', 'value']
    df.set_index(' ', inplace=True)
    df.head()


    # In[22]:


    html_table = df.to_html()
    html_table


    # In[23]:


    mars_table = df.to_html()

    mars_table_dict = {"mars_table": mars_table
    }

    return mars_table_dict


# In[ ]:




