import pandas as pd

# 读取csv文件
df = pd.read_csv("how2sign_realigned_val.csv")

# 创建空列表用于存放提取的数据
extracted_data = []

# 遍历每一行
for row in df.iterrows():
    # 将每一行的数据拆分为单词列表
    row_data = row[1][0].split(" ")

    # 用于存放两个数字前的第一个以"front"结尾的部分
    front_data = ""
    # 用于存放两个数字后的英文句子
    sentence_data = ""
    # 标记是否找到两个数字
    find_num = False

    # 遍历单词列表
    for word in row_data:
        # 如果当前单词是两个数字，则设置标记，并跳过本次循环
        if "." in word and len(word) > 2:
            find_num = True
            continue
        # 如果之前已经找到两个数字，则将当前单词加入英文句子
        elif find_num:
            sentence_data += word + " "
        # 否则，将当前单词加入以"front"结尾的部分
        else:
            front_data += word + " "

    # 将前、后两部分分别加入列表
    extracted_data.append([front_data, sentence_data])

# 将提取的数据写入Excel
df_new = pd.DataFrame(extracted_data, columns=['Front Part', 'Sentence'])
df_new.to_excel('extracted_data.xlsx', index=False)
