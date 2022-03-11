import os
from pathlib import Path


PROJECT_DIRECTORY = Path.home() / "chinese-news-aggregator"
SCRAPER_DIRECTORY = PROJECT_DIRECTORY / "chinese-news-aggregator/etl/scraper"
SCRAPED_DATA_DIRECTORY = SCRAPER_DIRECTORY / "scraped-data"


print('Starting China Daily Scraper and S3 Upload...')

# Begin in project directory
os.chdir(PROJECT_DIRECTORY)

# Change to Scrapy scraper directory
os.chdir(SCRAPER_DIRECTORY)

# Run China Daily Spider
print('Starting China Daily Scraper...')
os.system('scrapy crawl china_daily -O scraped-data/test.json')
print('China Daily Scraper Complete')

# Upload the new data file to S3 bucket
print('Starting S3 Upload...')
os.chdir('../s3')
os.system('python s3_upload_files.py')

print('S3 Upload Complete')