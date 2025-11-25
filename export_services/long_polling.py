import time, os
from export_services.sqsconn import sqs_conn
from export_services.handle_message import handle_message
from dotenv import load_dotenv
load_dotenv()
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")

def long_polling():
    sqs = sqs_conn()
    
    while True:
        try:
            resp = sqs.receive_message(
                QueueUrl=SQS_QUEUE_URL, #환경변수 load해서 가져오는거로
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20,   
            )
        except Exception as e:
            print(f"receive_msg 실패: {e}")
            time.sleep(5)   #5초쉬고 ㅏ다시
            continue

        messages = resp.get("Messages", []) # 가져온 큐의 Messages 필드

        if not messages:    # 메시지 없으면 다시 
            continue

        for msg in messages:
            receipt_handle = msg["ReceiptHandle"]   # 큐 메세지 삭제를 위한 키

            try:
                handle_message(msg)
               
                sqs.delete_message(     # 성공 시 메시지 삭제
                    QueueUrl=SQS_QUEUE_URL,
                    ReceiptHandle=receipt_handle
                )
            except Exception as e:
                print(f"메시지 처리 중 예외 발생(삭제 안함): {e}") # 다시 시도하기 위해 메세지 유지

        
        time.sleep(0.2) # 적당히 여유