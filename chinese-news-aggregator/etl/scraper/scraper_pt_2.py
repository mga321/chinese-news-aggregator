import os
import json
import requests
from bs4 import BeautifulSoup
import helpers
import constants


# Change to chinese-news-aggregator directory
os.chdir(constants.PROJECT_DIRECTORY)


# Read in the list of links
file_source = "../data/potential-new-links.json"
with open(file_source, "r") as file:
    secure_links = json.load(file)


# Collect required data from each article
list_of_lists = []

for url in secure_links:
    # Make soup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Collect data
    all_content = helpers.collect_all_article_content(soup)
    date = helpers.collect_article_date(soup)
    title = helpers.collect_article_title(soup)
    body = helpers.collect_article_body(soup)
    
    # Append to list of lists for DataFrame
    list_of_lists.append([date, title, body])


# Convert data to DataFrame and filter by date (only keep today's articles)
df = helpers.create_filtered_dataframe(list_of_lists, list_of_columns=["date", "title", "body"])


# Save DataFame to json file
file_destination = "../data/article-data-from-new-links.json"
df.to_json(file_destination, orient="records", indent=4)
