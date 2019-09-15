#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Run required imports
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


# In[2]:


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[3]:


def scrape_image():
    browser = init_browser()

    # Visit the nasa site to find latest articles
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    browser.click_link_by_id('full_image')
    time.sleep(2)

    browser.click_link_by_partial_text('more info')

    # Scrape page using beautiful_soup
    html=browser.html
    soup=bs(html, 'html.parser')

    # Find the featured image available
    mars_image_url = soup.find('img', class_='main_image')['src']
    featured_image_url=(f'https://www.jpl.nasa.gov{mars_image_url}')
    print(featured_image_url)
    browser.quit()
    
    #return results
    return featured_image_url.text


# In[4]:



# In[ ]:





# In[ ]:




