import os
import helpers
import constants


# Change to chinese-news-aggregator directory
os.chdir(constants.SCRAPED_DATA_DIRECTORY)

helpers.upload_file("china-daily-data.json", "daily-data-collection")
