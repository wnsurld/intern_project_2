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

#nas 업로드
nas_target = "C:/a" # 수정하기
nas_folder_path = upload_to_nas(folder_path, nas_target)    #Z:/filename

dicom_files = [file for file in os.listdir(nas_folder_path) if file.lower().endswith(".dcm")]   # -/-/dicom/input_value/0004.DCM~~
first_file = os.path.join(nas_folder_path, dicom_files[0]) #폴더 내 첫번째 파일 경로

dcm_header = get_header(first_file) #헤더 필드 get

hide_header(folder_name, dcm_header, dicom_files, nas_folder_path) #헤더 필드 익명화

zip_dcm_file = zip_dicom_folder(nas_folder_path) #dicom 파일 압축


#S3 업로드
upload_to_s3(zip_dcm_file)

#nas 삭제
delete_from_nas(nas_folder_path, zip_dcm_file)
