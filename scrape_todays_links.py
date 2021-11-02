import pandas as pd
import requests
from bs4 import BeautifulSoup

# Collect html code from china-us section page on China Daily website
url = "https://www.chinadaily.com.cn/world/china-us#"
page = requests.get(url)
# print(page.status_code)
# print(page.text)



# Create a soup object containing all of the web page's html content
soup = BeautifulSoup(page.content, "html.parser")

# Find all the content contained under the id "left", this is where the list of article content is found
results = soup.find(id="left")

# Fild the full list of article elements
article_elements = results.find_all("div", class_="mb10 tw3_01_2")



# Find the tag containing the link for each article
article_links = []

for article_element in article_elements:
    link_element = article_element.find("a")
    link = link_element.get("href")
    link = link[2:].strip()

    secure_link = "https://" + link

    article_links.append(secure_link)

    print(secure_link)

print(article_links)


# Convert list of articles to a csv file
df = pd.DataFrame(article_links, columns=["link"])

# print(df.head())
df.to_csv("data/todays_links.csv", index=False)




# NEXT STEPS
# This program scrapes all articles listed below the 3-4 articles that are up top in a different format, so I need to collect those
# articles above it as well as check the entire list of articles for only the ones with the current date on them. I don't want to include
# any articles from an older date