import os
import json

source_folder_path = "train_poseimg"
target_folder_path = "train_img"
source_dirs = os.listdir(source_folder_path)
target_dirs = os.listdir(target_folder_path)

json_list = []

for folder in source_dirs:
    folder_path = os.path.join(source_folder_path, folder)
    if os.path.isdir(folder_path):
        source_images = os.listdir(folder_path)
        for image_name in source_images:
            source_image_path = os.path.join(folder_path, image_name)

for folder in target_dirs:
    folder_path = os.path.join(target_folder_path, folder)
    if os.path.isdir(folder_path):
        target_images = os.listdir(folder_path)
        for image_name in target_images:
            target_image_path = os.path.join(folder_path, image_name)

for i in range(1653):
    # 构造文件路径
    source_path = source_image_path[i]
    target_path = target_image_path[i]
    # 读取图片信息
    source_info = {"source": source_path}
    target_info = {"target": target_path}
    # 获取提示信息
    #prompt = input("请输入图片{}的提示信息：".format(i))
    # 构造JSON对象并添加到列表中
    json_obj = {**source_info, **target_info, "prompt": ""}
    json_list.append(json_obj)

# 将JSON列表写入文件
with open("prompt.json", "w") as f:
    json.dump(json_list, f, indent=4)
