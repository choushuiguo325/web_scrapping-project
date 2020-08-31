
from splinter import Browser
from bs4 import BeautifulSoup as bs
from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo
import requests
import pandas as pd


def scrape():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_url = 'https://mars.nasa.gov/news/'

    browser.visit(news_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    news_html = browser.html
    soup = bs(news_html, 'lxml')
    result = soup.select_one("ul.item_list li.slide")
    news_title = result.find("div", class_= "content_title").text
    news_paragraph = result.find("div", class_ = "article_teaser_body").text


    featue_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featue_url)
    featue_html = browser.html
    soup = bs(featue_html, 'html.parser')
    featured_group = soup.find("article", class_= "carousel_item")
    part_image_url = featured_group.find('a', class_='button fancybox')['data-fancybox-href']
    featured_image_url = f"https://www.jpl.nasa.gov{part_image_url}"


    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    facts_df = tables[0]
    facts_df.columns = ['MARS PLANT PROFILE', 'Parameter']
    facts_html = facts_df.to_html()
    facts_html = facts_html.replace('\n','')


    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
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

    web_info = {
        'news_title':news_title,
        'news_paragraph':news_paragraph,
        'featured_image_url':featured_image_url,
        'facts_html':facts_html,
        'hemi':hemisphere_image_urls
    }

    browser.quit()


    return web_info






