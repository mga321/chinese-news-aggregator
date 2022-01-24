import os
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup


# Change to chinese-news-aggregator directory
pipeline_directory = Path.home() / "OneDrive/2021/Programming/python/chinese-news-aggregator"
os.chdir(pipeline_directory)


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
file_destination = pipeline_directory / "chinese-news-aggregator/data/potential-new-links.json"

with open(file_destination, "w") as file:
    json.dump(secure_links, file, indent=4)
