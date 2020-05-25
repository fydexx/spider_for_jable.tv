import pyodbc
# 清洗数据库字段
DBfile = r"./DB.accdb"
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
cursor = conn.cursor()
sql = "SELECT * FROM av_db"
res = cursor.execute(sql)

def update_fanhao(old,fanhao):
    sql1 = "UPDATE av_db SET fanhao = '{}' WHERE fanhao = '{}'".format(fanhao,old)
    print(sql1)
    cursor.execute(sql1)
    conn.commit()

res_list = []
for row in res:
    hello = row[1]
    res_list.append(hello)
    

for only_name in res_list:
    try:
        new_name = only_name.split('-')[0]+'-'+only_name.split('-')[1]
        new_name = new_name.upper()
        print(only_name+'  >>>>>>>>>  '+new_name)
        update_fanhao(only_name,new_name)
    except IndexError:
        new_name = only_name.upper()
        print(only_name+'  >>>>>>>>>  '+new_name)
        update_fanhao(only_name,new_name)

cursor.close()
conn.close()