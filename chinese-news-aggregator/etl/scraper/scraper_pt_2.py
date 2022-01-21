import os
import json
import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import datetime


def collect_all_article_content(soup_object):
    """This function takes a BeautifulSoup soup object as input and returns all of the HTML content within
    the specified tags. The returned content contains all of the potential data we will be extracting."""

    all_article_content = soup_object.find("div", class_="lft_art")

    return all_article_content


def collect_article_date(all_article_content):
    """This function takes the subset of HTML data from a webpage provided by the collect_all_article_content()
    function and parses thru it to find the date that the article was posted."""

    date_element = all_article_content.find("span", class_="info_l")
    date = date_element.text.split("|")[-1].strip()[9:-6]

    return date


def collect_article_title(all_article_content):
    """This function takes the subset of HTML data from a webpage provided by the collect_all_article_content()
    function and parses thru it to find the title of the article."""

    title_element = all_article_content.find("h1")
    title = title_element.text.strip()

    return title


def collect_article_body(all_article_content):
    """This function takes the subset of HTML data from a webpage provided by the collect_all_article_content()
    function and parses thru it to find the body of the article."""

    article_body = []

    body_element = all_article_content.find_all("p")
    for paragraph in body_element:
        article_body.append(paragraph.text.strip())

    body = " ".join(article_body).strip()

    return body


def create_filtered_dataframe(data, list_of_columns):
    """This function takes a list of lists and a list of the column names, creates a DataFrame, and filters that
    DataFrame by date to keep only date from articles posted on the current date."""

    df = pd.DataFrame(data, columns=list_of_columns)
    df["date"] = pd.to_datetime(df["date"])

    today = datetime.date.today()
    today_datetime = pd.to_datetime(today)

    df = df[df["date"] == today_datetime]

    return df




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
