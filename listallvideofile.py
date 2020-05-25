import os,shutil 

# 文件移动

root_dir="E:\\VIDEOS\\Jable.tv\\"
#列出所有下载好的文件
g = os.walk(r"E:\VIDEOS\Jable.tv\JAV_output")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        (filename,extension) = os.path.splitext(file_name)
        if os.path.getsize(os.path.join(path,file_name)) > 100*1024*1024:
            if not os.path.exists(root_dir+file_name):
                os.rename(os.path.join(path,file_name),root_dir+file_name)
                print(os.path.join(path,file_name)+"--->"+root_dir+file_name)
