import os
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup


# Change to chinese-news-aggregator directory
app_directory = Path.home() / "OneDrive - Jobin Machine, Inc/2021/chinese-news-aggregator/app"
os.chdir(app_directory)



# Collect html code from china-us section page on China Daily website
url = "https://www.chinadaily.com.cn/world/china-us#"
page = requests.get(url)
# print(page.status_code)
# print(page.text)

# Create a soup object containing all of the web page's html content
soup = BeautifulSoup(page.content, "html.parser")



# Article Links Part 1:  Collect link from primary article (top left of webpage, the left portion of html section <div class="tw2" section)
secure_links = []

primary_article = soup.find("span", class_="tw2_l_t")
primary_article_link = primary_article.a.get("href")
secure_link = "https:" + primary_article_link

secure_links.append(secure_link)



# Article Links Part 2:  Collect links from secondary articles (top right of webpage. the right portion of html section <div class="tw2" section)
secondary_articles = soup.find_all("div", class_="tBox2")

for secondary_article in secondary_articles:
    secondary_article_link = secondary_article.a.get("href")
    secure_link = "https:" + secondary_article_link

    secure_links.append(secure_link)



# Article Links Part 3:  Collect links from list of articles (center of webpage below the primary and secondary articles section, the list of <div class="mb10 tw3_01_2" sections)
articles_list = soup.find_all("span", class_="tw3_01_2_t")

for listed_article in articles_list:
    listed_article_link = listed_article.a.get("href")
    secure_link = "https:" + listed_article_link

    secure_links.append(secure_link)

# print(secure_links)



# Create json file containing all potential new links for the current day
file_destination = app_directory / "data/potential_new_links.json"

with open(file_destination, "w") as file:
    json.dump(secure_links, file, indent=4)
