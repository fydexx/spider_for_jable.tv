import os
import shutil

# 文件去掉-c

g = os.walk(r"E:\VIDEOS\Jable.tv")

for path, dir_list, file_list in g:
    for file_name in file_list:
        (only_name, extension) = os.path.splitext(file_name)
        if os.path.getsize(os.path.join(path, file_name)) > 100*1024*1024:
            print(os.path.join(path, file_name))
            os.rename(os.path.join(path, file_name),
                      os.path.join(path, file_name.upper()))
            print(os.path.join(path, file_name.upper()))
