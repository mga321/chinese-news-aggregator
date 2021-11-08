import os
import json
import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import datetime


# Change to chinese-news-aggregator directory
app_directory = Path.home() / "OneDrive - Jobin Machine, Inc/2021/chinese-news-aggregator/app"
os.chdir(app_directory)



# Read in the list of links
file_source = app_directory / "data/potential_new_links.json"
with open(file_source, "r") as file:
    secure_links = json.load(file)



# Collect data from each article
list_of_lists = []

for url in secure_links:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    all_article_content = soup.find("div", class_="lft_art")

    # Collect article date
    date_element = all_article_content.find("span", class_="info_l")
    date = date_element.text.split("|")[-1].strip()[9:-6]

    # Collect article title
    title_element = all_article_content.find("h1")
    title = title_element.text.strip()

    # Collect article body
    article_body = []

    body_element = all_article_content.find_all("p")
    for paragraph in body_element:
        article_body.append(paragraph.text.strip())

    body = " ".join(article_body).strip()

    # Append data to list_of_lists
    list_of_lists.append([date, title, body])


# for list in list_of_lists:
#     for item in list:
#         print(item, "\n\n")



# Convert list of lists into DataFrame, filter by date (only keep today's articles
df = pd.DataFrame(list_of_lists, columns=["date", "title", "body"])
df["date"] = pd.to_datetime(df["date"])

# Create datetime format variable for current day comparison
today = datetime.date.today()
today_datetime = pd.to_datetime(today)

# Filter DataFrame based on today's date
df = df[df["date"] == today_datetime]
print(df)
