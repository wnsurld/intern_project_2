import shutil
import os

def zip_dicom_folder(folder_path):

    #경로와 파일 이름 분리
    base_name = os.path.basename(folder_path.rstrip(os.sep))
    target_dir = os.path.dirname(folder_path)
    zip_full_path = os.path.join(target_dir, base_name)

    #압축 생성
    shutil.make_archive(zip_full_path, 'zip', folder_path)
    print("압축 완료")
    
    return zip_full_path + ".zip"