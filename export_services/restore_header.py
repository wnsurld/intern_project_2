import os, pydicom

from services.dbconn import db_connection
from services.get_header import get_header

def restore_header(file_path):
    dicom_files = [file for file in os.listdir(file_path) if file.lower().endswith(".dcm")]   # -/-/dicom/input_value/0004.DCM~~
    first_file = os.path.join(file_path, dicom_files[0]) #폴더 내 첫번째 파일 경로    
    header = get_header(first_file)

    db = db_connection()
    cur = db.cursor()
    cur.execute("""
                SELECT * FROM study
                WHERE study_instance_uid = %s
                """,(header["StudyInstanceUID"],))
    row = cur.fetchone()

    header["PatientName"] = row[3]
    header["PatientID"] = row[4]
    header["PatientSex"] = row[5]
    header["PatientBirthDate"] = row[6]

    for filename in dicom_files:
        single_file_path = os.path.join(file_path, filename)
        with open(single_file_path, 'rb') as dcm_file:
            dcm = pydicom.dcmread(dcm_file)

        for key in header:
            if(key != "StudyInstanceUID"):
                setattr(dcm, key, header[key])
        
        temp_path = file_path + ".tmp"
        dcm.save_as(temp_path)

        os.replace(temp_path, single_file_path)
    print("헤더 복원 완료")