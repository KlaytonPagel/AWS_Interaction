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


# list objects in the bucket____________________________________________________________________________________________
def list_objects(file_name: str) -> str:
    objects = s3.get_object(Bucket=bucket, Key=file_name)
    content = str(objects["Body"].read())[2:-1]
    return content


# upload file___________________________________________________________________________________________________________
def upload():
    with open("hehe.txt", "rb") as f:
        s3.upload_fileobj(f, bucket, "hehe.txt")


# Download file_________________________________________________________________________________________________________
def download():
    s3.download_file(bucket, "Users/Employees/83GogrCqXcNd2bkDPEdOou8hyTtY0Qc2/dashboard.json", "hehehe.json")


thing = eval(list_objects("Users/Employees/83GogrCqXcNd2bkDPEdOou8hyTtY0Qc2/dashboard.json"))

print(thing['1'])
