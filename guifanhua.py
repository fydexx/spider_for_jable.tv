import os,shutil 

#文件去掉-c

g = os.walk(r"E:\VIDEOS\Jable.tv")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        (only_name,extension) = os.path.splitext(file_name)
        if(len(only_name.split('-'))>2):
            new_name = only_name.split('-')[0]+'-'+only_name.split('-')[1]+extension
            if(not os.path.exists(os.path.join(path,new_name))):
                os.rename(os.path.join(path,file_name),os.path.join(path,new_name))
                print(os.path.join(path,file_name)+"    ->>>>>  "+os.path.join(path,new_name))