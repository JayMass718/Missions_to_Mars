# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
import pandas as pd

# Set variables
# create route that renders index.html template

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/Users/julianmassiah/Desktop/Columbia Boot Camp/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def mars_scraper():
    browser = init_browser()
#-----------------------------------------------------------------------------------------------
    ## NASA Mars News
    
    # To visit the website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    # Print all headlines
    content_titles = soup.find_all('div', class_="content_title")
    # A blank list to hold the headlines
    news_titles = []
    # Loop over div elements
    for content_title in content_titles:
        # If div element has an anchor...
        if (content_title.a):
            # And the anchor has non-blank text...
            if (content_title.a.text):
                # Append the td to the list
                news_titles.append(content_title)

    # Print all descriptions
    content_descriptions = soup.find_all('div', class_="rollover_description_inner")
    # A blank list to hold the descriptions
    news_descriptions = []
    # Loop over div elements
    for content_des in content_descriptions:
        # And the anchor has non-blank text...
        if (content_des.text):
            # Append the div to the list
            news_descriptions.append(content_des)

    # Finisher Definitions
    news_title = news_titles[0].text
    news_p = news_descriptions[0].text
    
    # Close the browser after scraping
    browser.quit()

#-----------------------------------------------------------------------------------------------
    ##JPL Mars Space Images - Featured Image
    
    # To visit the website
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)  
    # Retrieve all elements that contain media information
    media_elements = soup.find_all('div', class_="default floating_text_area ms-layer")
    # Iterate through the element
    for media_element in media_elements:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        footer = media_element.find('footer')
        link = footer.find('a')
        href = link['data-fancybox-href']
    
    # Finisher Definition
    featured_image_url = "https://www.jpl.nasa.gov"+href
    
    # Close the browser after scraping
    browser.quit()

 #-----------------------------------------------------------------------------------------------   
    ## Mars Weather
    
    # To visit the website
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    # Print all the tweets
    tweet_entries = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    # A blank list to hold the tweets
    tweets = []
    # Loop over div elements
    for tweet_entry in tweet_entries:
        # If div element has a paragraph...
        if (tweet_entry.text):
            # Append the div to the list
            tweets.append(tweet_entry)
        
    # Finisher Definition
    mars_weather = tweets[0].text
    
    # Close the browser after scraping
    browser.quit()

#----------------------------------------------------------------------------------------------- 
    # Dictionary Storage
    
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather
    }

    # Return results
    return mars_data