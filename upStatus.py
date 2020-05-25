import pyodbc
import os
## 根据实际文件更新数据库
DBfile = r"./DB.accdb"
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
cursor = conn.cursor()

def setHave(fanhao):
    sql = "UPDATE av_db SET isdown=True WHERE fanhao='{}'".format(fanhao)
    print(sql)
    cursor.execute(sql)
    conn.commit()

g = os.walk(r"E:\VIDEOS\Jable.tv")
for path,dir_list,file_list in g:  
    for file_name in file_list:  
        (filename,extension) = os.path.splitext(file_name)
        if os.path.getsize(os.path.join(path,file_name)) > 100*1024*1024:
            setHave(filename)
            print(filename+"  >>>>>  "+"True")


cursor.close()
conn.close()