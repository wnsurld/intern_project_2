import pydicom

def get_header(dicom_file):
    dcm = pydicom.dcmread(dicom_file, stop_before_pixels=True)

    header = {
        "StudyInstanceUID": getattr(dcm, "StudyInstanceUID", ""),
        "PatientName": getattr(dcm, "PatientName", ""),
        "PatientID": getattr(dcm, "PatientID", ""),
        "PatientSex": getattr(dcm, "PatientSex", ""),
        "PatientBirthDate": getattr(dcm, "PatientBirthDate", "")
    }
    
    print("헤더 추출 완료")
    return header
