#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo
import requests
import pandas as pd


# # Step 1 - Scraping

# ### NASA Mars News

# In[3]:


news_url = 'https://mars.nasa.gov/news/'
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(news_url)
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
news_html = browser.html
soup = bs(news_html, 'lxml')
result = soup.select_one("ul.item_list li.slide")
news_title = result.find("div", class_= "content_title").text
print(news_title)
news_paragraph = result.find("div", class_ = "article_teaser_body").text
print(news_paragraph)


# In[ ]:


# url = 'https://mars.nasa.gov/news/'
# response = requests.get(url)
# soup = bs(response.text, 'lxml')
# result = soup.select_one("ul.item_list li.slide")
# news_title = result.find("div", class_= "content_title").text
# print(title)
# news_paragraph = result.find("div", class_ = "article_teaser_body").text
# print(news_paragraph)


# ### JPL Mars Space Images - Featured Image

# In[46]:


featue_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(featue_url)
featue_html = browser.html
soup = bs(featue_html, 'html.parser')
featured_group = soup.find("article", class_= "carousel_item")
part_image_url = featured_group.find('a', class_='button fancybox')['data-fancybox-href']
featured_image_url = f"https://www.jpl.nasa.gov{part_image_url}"
print(featured_image_url)


# ### Mars Facts

# In[30]:


facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
facts_df = tables[0]
facts_df.columns = ['MARS PLANT PROFILE', 'Parameter']
facts_df


# In[32]:


facts_df.to_html("facts_table.html")
facts_html = facts_df.to_html()
facts_html = facts_html.replace('\n','')
facts_html


# ### Mars Hemispheres

# In[94]:


hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(hemi_url)
hemi_html = browser.html
soup = bs(hemi_html, 'lxml')
results = browser.find_by_css('div.description a.product-item')
hemisphere_image_urls = []
for i in range(len(results)):
    browser.find_by_css('div.description a.product-item')[i].click()
    img = browser.find_by_text("Sample").first
    img_url = img['href']
    img_title = browser.find_by_css('h2.title').text
    info = {"title":img_title, "img_url":img_url}
    hemisphere_image_urls.append(info)
    browser.back()
    
hemisphere_image_urls


# # Step 2 - MongoDB and Flask Application

# 

# In[ ]:




