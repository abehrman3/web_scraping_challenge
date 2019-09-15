#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Run required imports
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


# In[19]:


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[20]:


def scrape_news():
    browser = init_browser()

    # Visit the nasa site to find latest articles
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page using beautiful_soup
    html=browser.html
    soup=bs(html, 'html.parser')

    # Find the first article available
    news_article = soup.find('div', class_='content_title')
    news_p = soup.find('div', class_='article_teaser_body')
    mars_news=news_article.text
    mars_paragraph=news_p.text
    print(news_article)
    
     # Store data in a dictionary
    nasa_news = {
        "news_article": news_article,
        "news_p": news_p,
    }
    print(nasa_news)
    browser.quit()
    
    #return results
    return news_article.text, news_p.text

    


# In[21]:




# In[ ]:




