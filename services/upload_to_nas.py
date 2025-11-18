import os, shutil

def upload_to_nas(zip_dcm_file, nas_target):

    file_name = os.path.basename(zip_dcm_file)
    destination = os.path.join(nas_target, file_name)

    shutil.copy2(zip_dcm_file, destination)

    print(f"NAS 업로드 완료: {destination}")
    return destination