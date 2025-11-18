from dotenv import load_dotenv
import os, boto3

load_dotenv()

def s3_connection():
    s3 = boto3.client(
        's3',
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name = os.getenv("AWS_REGION")
    )
    return s3

def get_bucketName():
    return os.getenv("BUCKET_NAME")
