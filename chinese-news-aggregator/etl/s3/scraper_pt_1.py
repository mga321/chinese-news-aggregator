import os
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup


# Article Links Func 1:  Collect link from primary article (top left of webpage, the left portion of html section <div class="tw2" section)
def collect_primary_article_link(soup_object, list_of_secure_links):
    """This function takes a soup object and a list as inputs, parses thru the soup object to find
    primary article link (main article at the top left of the page), and appends the link to the list
    of secure links."""

    # Collect from webpage primary article
    primary_article = soup_object.find("span", class_="tw2_l_t")
    primary_article_link = primary_article.a.get("href")
    secure_link = "https:" + primary_article_link

    list_of_secure_links.append(secure_link)


# Article Links Func 2:  Collect links from secondary articles (top right of webpage. the right portion of html section <div class="tw2" section)
def collect_secondary_article_links(soup_object, list_of_secure_links):
    """This function takes a soup object and a list as inputs, parses thru the soup object to find
    secondary article links (main articles at the top right of the page), and appends the links to the list
    of secure links."""
    
    secondary_articles = soup_object.find_all("div", class_="tBox2")

    for secondary_article in secondary_articles:
        secondary_article_link = secondary_article.a.get("href")
        secure_link = "https:" + secondary_article_link

        list_of_secure_links.append(secure_link)


# Article Links Func 3:  Collect links from list of articles (center of webpage below the primary and secondary articles section, the list of <div class="mb10 tw3_01_2" sections)
def collect_listed_article_links(soup_object, list_of_secure_links):
    """This function takes a soup object and a list as inputs, parses thru the soup object to find
    listed articles links (list of articles in the center of the page), and appends the links to the list
    of secure links."""

    articles_list = soup_object.find_all("span", class_="tw3_01_2_t")

    for listed_article in articles_list:
        listed_article_link = listed_article.a.get("href")
        secure_link = "https:" + listed_article_link

        list_of_secure_links.append(secure_link)




# Change to chinese-news-aggregator directory
app_directory = Path.home() / "OneDrive - Jobin Machine, Inc/2021/chinese-news-aggregator/app"
os.chdir(app_directory)


# Collect html code from china-us section page on China Daily website and create soup object
url = "https://www.chinadaily.com.cn/world/china-us#"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


# Collect article links
secure_links = []
funcs = [collect_primary_article_link, collect_secondary_article_links, collect_listed_article_links]

for func in funcs:
    func(soup, secure_links)


# Create json file containing all potential new links for the current day
file_destination = app_directory / "data/potential-new-links.json"

with open(file_destination, "w") as file:
    json.dump(secure_links, file, indent=4)
