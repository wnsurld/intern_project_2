import os
from services.get_header import get_header
from services.hide_header import hide_header
from services.zip_folder import zip_dicom_folder
from services.upload_to_nas import upload_to_nas
from services.upload_to_s3 import upload_to_s3
from services.delete_from_nas import delete_from_nas

# 현재 로컬 pc에서 수행중인데 경로를 nas로 수정
# nas에서 구동하는 로직?
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

folder_name = input("업로드 할 DICOM 폴더 : ")
dicom_root = os.path.join(BASE_DIR, "dicom")    #다이컴 폴더 경로       -/-/dicom
folder_path = os.path.join(dicom_root, folder_name)  #입력받은 다이컴 폴더 경로     -/-/dicom/input_value

dicom_files = [file for file in os.listdir(folder_path) if file.lower().endswith(".dcm")]   # -/-/dicom/input_value/0004.DCM~~
first_file = os.path.join(folder_path, dicom_files[0]) #폴더 내 첫번째 파일 경로    

dcm_header = get_header(first_file) #헤더 필드 get

hide_header(folder_name, dcm_header, dicom_files, folder_path) #헤더 필드 익명화

zip_dcm_file = zip_dicom_folder(folder_path) #dicom 파일 압축

#nas 업로드
nas_target = "Z:/"
nas_folder_path = upload_to_nas(zip_dcm_file, nas_target)    #Z:/filename

#S3 업로드
upload_to_s3(nas_folder_path)

#nas 삭제
delete_from_nas(nas_folder_path)

# db테이블 생성하고 nas 삭제 주석화 해서 잘 되나 확인하기. s3 env작성하기