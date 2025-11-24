import json
from export_services.download_to_nas import download_to_nas
from export_services.restore_header import restore_header

def handle_message(msg):
    """
    큐 메세지 하나 처리
    body에서 bucket/key 추출
    nas로 다운
    dicom 헤더 복원
    """

    body = json.loads(msg["Body"])

    bucket = body.get("bucket")
    key = body.get("key")
    print(f"bucket = {bucket}, key = {key}")

    file_path = download_to_nas(bucket, key)

    restore_header(file_path)