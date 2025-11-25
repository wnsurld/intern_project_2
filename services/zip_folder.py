import shutil
import os

def zip_dicom_folder(folder_path):

    #경로와 파일 이름 분리
    base_name = os.path.basename(folder_path.rstrip(os.sep))
    zip_full_path = os.path.join(os.path.dirname(folder_path), base_name)

    #압축 생성
    shutil.make_archive(zip_full_path, 'zip', root_dir=folder_path)
    print("압축 완료")
    
    return zip_full_path + ".zip"
