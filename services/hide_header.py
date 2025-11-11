import pydicom, os
from services.dbconn import db_connection

#추후 s3검색 로직에서 폴더이름으로 쿼리(uuid5 사용)
#원본 db에 저장 후 헤더 익명화
def hide_header(folder_name, header, dicom_files):

    conn = db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO study
        (folder_name, study_instance_uid, patient_name, patient_id, patient_sex, patient_birthdate)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        folder_name,
        header["StudyInstanceUID"],
        header["PatientName"],
        header["PatientID"],
        header["PatientSex"],
        header["PatientBirthDate"],
    ))
    cur.close()
    conn.commit()
    conn.close()
    print("원본 헤더 DB 저장 완료")

    # 익명화 단계
    folder_path = os.path.join("dicom", folder_name)
    for filename in dicom_files:
        file_path = os.path.join(folder_path, filename)
        dcm = pydicom.dcmread(file_path)

        for key in header:
            setattr(dcm, key, "anonymous")
        
        dcm.save_as(file_path)
    print("헤더 수정 완료")