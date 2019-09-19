#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Run required imports
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


# In[77]:


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[78]:


def scrape_weather():
    browser = init_browser()

    # Visit the nasa site to find latest articles
    news_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page using beautiful_soup
    html=browser.html
    soup=bs(html, 'html.parser')

    # Find the weather tweets that include Insight sol - weather
    # Add each weather tweet instance to a list
    weather_data=[]
    for weather_tweet in soup.find_all("p"):
        if not "InSight sol" in weather_tweet.text:continue
        weather_data.append(weather_tweet.text)
        
    #Provide me the first instance of a weather tweet 
    mars_weather = weather_data[0]
    weather_data = {"mars_weather": mars_weather
    }
    print(mars_weather)
    
    browser.quit()
    
    #return results
    return weather_data
    







