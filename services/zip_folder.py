import shutil
import os

def zip_dicom_folder(folder_path):

    #경로와 파일 이름 분리
    base_name = os.path.basename(folder_path.rstrip(os.sep))
    zip_file_name = base_name + ".zip"

    #압축 생성
    shutil.make_archive(base_name, 'zip', folder_path)
    print("압축 완료")
    
    return os.path.abspath(zip_file_name)
