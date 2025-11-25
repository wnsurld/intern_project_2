import os
import shutil

def download_to_local(folder_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # ../modify_dicom 폴더 생성
    local_dir = os.path.join(base_dir, "modify_dicom")
    os.makedirs(local_dir, exist_ok=True)
    
    # 폴더명 추출
    folder_name = os.path.basename(folder_path.rstrip(os.sep))
    
    # 최종 저장 경로
    local_path = os.path.join(local_dir, folder_name)
    
    if os.path.exists(local_path):
        shutil.rmtree(local_path)
    
    # 파일 복사
    shutil.copytree(folder_path, local_path)
    print(f"로컬 저장 완료")