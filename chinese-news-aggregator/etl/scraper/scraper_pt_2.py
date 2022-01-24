import os
import json
import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import datetime


# Change to chinese-news-aggregator directory
pipeline_directory = Path.home() / "OneDrive/2021/Programming/python/chinese-news-aggregator"
os.chdir(pipeline_directory)


# Read in the list of links
file_source = pipeline_directory / "chinese-news-aggregator/data/potential-new-links.json"
with open(file_source, "r") as file:
    secure_links = json.load(file)


# Collect required data from each article
list_of_lists = []

for url in secure_links:
    # Make soup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Collect data
    all_content = collect_all_article_content(soup)
    date = collect_article_date(soup)
    title = collect_article_title(soup)
    body = collect_article_body(soup)
    
    # Append to list of lists for DataFrame
    list_of_lists.append([date, title, body])


# Convert data to DataFrame and filter by date (only keep today's articles)
df = create_filtered_dataframe(list_of_lists, list_of_columns=["date", "title", "body"])


# Save DataFame to json file
file_destination = pipeline_directory / "chinese-news-aggregator/data/article-data-from-new-links.json"
df.to_json(file_destination, orient="records", indent=4)
