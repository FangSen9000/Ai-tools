import os

count = 1
for root, dirs, files in os.walk("."):  # 遍历当前文件夹及其子文件夹
    for dir_name in dirs:  # 遍历每个文件夹并重命名
        new_name = str(count).zfill(6)  # 构造新名称，使用zfill方法保证名称长度为6位，例如：000001
        os.rename(os.path.join(root, dir_name), os.path.join(root, new_name))  # 重命名
        count += 1  # 计数器加1