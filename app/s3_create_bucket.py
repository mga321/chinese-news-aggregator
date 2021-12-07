import boto3

aws_region = "us-east-2"

s3_resource = boto3.resource("s3", region_name=aws_region)


# Create new bucket
bucket_name = "daily-data-collection"
location = {"LocationConstraint": aws_region}

bucket = s3_resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)


print(f"Amazon S3 bucket named \"{bucket_name}\" has been created.")