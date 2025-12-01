import os, shutil

def upload_to_nas(zip_dcm_file, nas_target):

    file_name = os.path.basename(zip_dcm_file)
    destination = os.path.join(nas_target, file_name)

    shutil.copytree(zip_dcm_file, destination, dirs_exist_ok=True)

    print(f"NAS 업로드 완료: {destination}")
    return destination
