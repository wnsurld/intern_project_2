import os, shutil
from services.s3conn import s3_connection

def download_to_nas(bucket, key):
    s3 = s3_connection()

    filename = key.split("/")[-1]
    zip_path = os.path.join("Z:/", filename)

    s3.download_file(bucket, key, zip_path)
    print("S3 파일 다운로드 완료")

    extract_folder_name = filename.replace(".zip", "")
    extract_folder_path = os.path.join("Z:/", extract_folder_name)

    # 폴더가 없으면 생성
    os.makedirs(extract_folder_path, exist_ok=True)

    # 3) 압축 해제
    shutil.unpack_archive(zip_path, extract_folder_path)
    return extract_folder_path