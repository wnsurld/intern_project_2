import json
from export_services.download_to_nas import download_to_nas
from export_services.restore_header import restore_header
from export_services.download_to_local import download_to_local

def handle_message(msg):
    """
    큐 메세지 하나 처리
    body에서 bucket/key 추출
    nas로 다운
    dicom 헤더 복원
    로컬 다운로드
    """

    body = json.loads(msg["Body"])
    print(f"body = {body}")

    record = body["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]
    print(f"bucket = {bucket}, key = {key}")

    file_path = download_to_nas(bucket, key)

    restore_header(file_path)

    download_to_local(file_path)