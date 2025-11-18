import os

def delete_from_nas(nas_file_path):
    
    os.remove(nas_file_path)
    print("NAS 파일 삭제 완료")