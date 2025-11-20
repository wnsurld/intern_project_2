import os
from services.s3conn import s3_connection

def download_to_nas(bucket, key):
    s3 = s3_connection()

    filename = key.split("/")[-1]
    path = os.path.join("Z:/", filename)

    s3.download_file(bucket, key, path)
    print("S3 파일 다운로드 완료")
    return path