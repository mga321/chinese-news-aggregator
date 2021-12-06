import boto3

AWS_REGION = "us-east-2"

s3_resource = boto3.resource("s3", region_name=AWS_REGION)


# Create new bucket
bucket_name = "daily-data-collection"
location = {"LocationConstraint": AWS_REGION}

bucket = s3_resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)


print(f"Amazon S3 bucket named \"{bucket_name}\" has been created.")