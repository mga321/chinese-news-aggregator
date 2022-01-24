import os
import helpers
import constants



# Change to chinese-news-aggregator directory
os.chdir(constants.DATA_DIRECTORY)

helpers.upload_file("article-data-from-new-links.json", "daily-data-collection")