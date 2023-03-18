# 导入必要的库
import csv
import xlwt 

# 创建一个excel工作薄
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('sheet1')

# 读取csv文件中的内容
with open('how2sign_realigned_val.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # 将csv文件中的内容写入excel表格
    row_num = 0
    for row in csv_reader:
        col_num = 0
        # 将首列的内容拆分，分别存入两列
        words = row[0].split(' ')
        for word in words[-2:]:
            worksheet.write(row_num, col_num, word)
            col_num += 1
        row_num += 1

# 保存excel文件
workbook.save('data.xls')