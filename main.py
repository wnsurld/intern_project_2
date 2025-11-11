import os
from services.dbconn import db_connection
from services.get_header import get_header
from services.hide_header import hide_header
from services.zip_folder import zip_dicom_folder

folder_name = input("업로드 할 DICOM 폴더 : ")
folder_path = os.path.join("dicom", folder_name)    #폴더 경로
dicom_files = [file for file in os.listdir(folder_path) if file.lower().endswith(".dcm")]
first_file = os.path.join(folder_path, dicom_files[0]) #폴더 내 첫번째 파일 경로

dcm_header = get_header(first_file) #헤더 필드 get

hide_dcm_header = hide_header(folder_name, dcm_header, dicom_files) #헤더 필드 익명화

zip_dcm_file = zip_dicom_folder(folder_path) #dicom 파일 압축

#nas 업로드 구현 예정