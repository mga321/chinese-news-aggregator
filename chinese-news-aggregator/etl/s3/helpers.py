import boto3
import datetime


def upload_file(file_name: str, bucket: str, key=None):
    """This function takes the updated article data file from the data directory and uploads it to
    AWS S3 using the AWS SDK for Python while providing it with a S3 Key based on the data source, section
    from the news site, and the current date.
    
    # file_name is the path to the file on the local machine
    # bucket is the bucket name to upload to
    # key is the name the file will have in s3"""

    today_str = datetime.date.today().strftime("%Y-%m-%d")

    if key is None:
        key = f"china-daily/china-us/" + today_str + ".json"

   
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket, key)
