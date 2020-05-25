import requests        #导入requests包
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pyodbc
from time import sleep

item_num=24
page_num=124

proxies={
    "https":"socks5://127.0.0.1:20001"
}

# 获取特定页码的url,按照最近更新排序
def getPageurl(pageNum):
    url="https://jable.tv/categories/chinese-subtitle/?mode=async&function=get_block&block_id=list_videos_common_videos_list&sort_by=post_date&from={}".format(str(pageNum))
    return url

# 获取特定item的选择器
def getSelector(itemNum):
    selector="#list_videos_common_videos_list > div > section > div > div:nth-child({}) > div > div.detail > h6 > a".format(itemNum)
    return selector

#主方法
#用于爬取特定数据
current_page_soup=""
current_num=0
def getData(pageNum,itemNum):
    global current_num
    global current_page_soup
    if pageNum==current_num:
        data=current_page_soup.select(getSelector(itemNum))
        for item in data:
            herf=item.get('href')
            title=item.text
            fanhao=urlparse(herf).path.split("/")[2]
            return {"f":fanhao,"u":herf,"t":title}
    else:
        current_num=pageNum

        requests.adapters.DEFAULT_RETRIES = 20
        s = requests.session()
        s.keep_alive = False
        strhtml = requests.get(getPageurl(pageNum),proxies=proxies)
        soup=BeautifulSoup(strhtml.text,'lxml')
        current_page_soup=soup
        data = soup.select(getSelector(itemNum))
        for item in data:
            herf=item.get('href')
            title=item.text
            fanhao=urlparse(herf).path.split("/")[2]
            return {"f":fanhao,"u":herf,"t":title}

def insert_into_db(cursor,data):
    sql = "INSERT INTO av_db(fanhao,url,title) VALUES('{}','{}','{}')".format(data.get('f'),data.get('u'),data.get('t'))
    print(sql)
    cursor.execute(sql)
    
def main():
    DBfile = r"./test.accdb"
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
    cursor = conn.cursor()
    #清空数据库
    cursor.execute("DELETE * FROM av_db")
    for page in range(1,page_num+1):
        for item in range(1,item_num+1):
            insert_into_db(cursor,getData(page,item))
            conn.commit()
        sleep(1)     
    cursor.close()  
    conn.close()

main()
