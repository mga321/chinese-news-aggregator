import os
import json
import requests
from bs4 import BeautifulSoup
import helpers
import constants


# Change to chinese-news-aggregator directory
os.chdir(constants.PROJECT_DIRECTORY)


# Collect html code from china-us section page on China Daily website and create soup object
url = "https://www.chinadaily.com.cn/world/china-us#"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


# Collect article links
secure_links = []
funcs = [helpers.collect_primary_article_link, helpers.collect_secondary_article_links, helpers.collect_listed_article_links]

for func in funcs:
    func(soup, secure_links)


# Create json file containing all potential new links for the current day
file_destination = "../data/potential-new-links.json"

with open(file_destination, "w") as file:
    json.dump(secure_links, file, indent=4)
