import json
from export_services.download_to_nas import download_to_nas

def handle_message(msg):
    """
    큐 메세지 하나 처리
    body에서 bucket/key 추출
    nas로 다운 -여기깔지-
    dicom 헤더 복원
    """

    body = json.loads(msg["Body"])

    bucket = body.get("bucket")
    key = body.get("key")
    print(f"bucket = {bucket}, key = {key}")

    file_path = download_to_nas(bucket, key)

    