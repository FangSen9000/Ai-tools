import os
import json

source_folder = "source/"
target_folder = "target/"

json_list = []

for i in range(3):
    # 构造文件路径
    source_path = source_folder + str(i) + ".png"
    target_path = target_folder + str(i) + ".png"
    # 读取图片信息
    source_info = {"source": source_path}
    target_info = {"target": target_path}
    # 获取提示信息
    prompt = input("请输入图片{}的提示信息：".format(i))
    # 构造JSON对象并添加到列表中
    json_obj = {**source_info, **target_info, "prompt": prompt}
    json_list.append(json_obj)

# 将JSON列表写入文件
with open("output.json", "w") as f:
    json.dump(json_list, f, indent=4)
