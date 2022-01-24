import pandas as pd
import datetime


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