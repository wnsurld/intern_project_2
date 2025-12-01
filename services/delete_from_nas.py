import os
import shutil

def delete_from_nas(nas_folder_path, zip_dcm_file):
    
    os.remove(zip_dcm_file)
    shutil.rmtree(nas_folder_path)
    print("NAS 파일 삭제 완료")
    