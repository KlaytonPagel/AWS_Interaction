# working with s3 buckets in AWS

import boto3
import os
from dotenv import load_dotenv


load_dotenv()
bucket = os.getenv("TEST_BUCKET")

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)


# upload file___________________________________________________________________________________________________________
def upload():
    with open("hehe.txt", "rb") as f:
        s3.upload_fileobj(f, bucket, "hehe.txt")


# Download file_________________________________________________________________________________________________________
def download():
    s3.download_file(bucket, "hehe.txt", "hehehe.txt")


download()
