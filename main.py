import os, csv

id = input("업로드할 ID : ")

#db에 저장된 데이터 쿼리
conn = db_connection()  #dbconn.py의 db_connection() 생성할것
cur = conn.cursor()
query = "SELECT * FROM sample_data WHERE id = %s;"
cur.excute(query, (id,))
rows = cur.fetchall()
column_names = [desc[0] for desc in cur.description]  #select한 객체들의 id값 추출

#쿼리한 데이터 csv로 변환 후 NAS에 저장
file_path = fr"Z:\sample_data_{id}.csv" #nas 폴더에 csv파일저장
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer()
    writer.writerow(column_names)
    writer.writerows(rows)
print("CSV파일 변환 및 NAS 저장 완료")

cur.close()
conn.close()