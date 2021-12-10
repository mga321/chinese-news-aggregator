import boto3
import os
import datetime
from pathlib import Path


def upload_file(file_name, bucket, key=None):
    """This function takes the updated article data file from the data directory and uploads it to
    AWS S3 using the AWS SDK for Python while providing it with a S3 Key based on the data source, section
    from the news site, and the current date.
    
    # file_name is the path to the file on the local machine
    # bucket is the bucket name to upload to
    # key is the name the file will have in s3"""

    today_str = (datetime.date.today()).strftime("%Y-%m-%d")

    if key is None:
        key = f"china-daily/china-us/" + today_str + ".json"

   
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket, key)



# Change to chinese-news-aggregator directory
# data_directory = Path.home() / "OneDrive - Jobin Machine, Inc/2021/chinese-news-aggregator/app/data"
data_directory = Path.home() / "OneDrive/2021/Programming/python/chinese-news-aggregator/app/data"
os.chdir(data_directory)

upload_file("article_data_from_new_links.json", "daily-data-collection")
