import os
from dotenv import load_dotenv
from services.s3conn import s3_connection, get_bucketName

load_dotenv()

def upload_to_s3(nas_zip_path):
    s3 = s3_connection()
    bucket_name = get_bucketName()
    filename = os.path.basename(nas_zip_path) 
    prefix = os.getenv("S3_PREFIX_IMPORT") # ~~/
    s3_key = f"{prefix}{filename}"

    s3.upload_file(nas_zip_path, bucket_name, s3_key)
    print("S3 업로드 완료")