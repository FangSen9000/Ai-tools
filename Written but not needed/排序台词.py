# 程序
import csv

# 读取txt文件
with open('dev.txt','r') as f:
    contenttxt = f.readlines()

# 读取csv文件
csvfile = csv.reader(open('csv.csv', 'r'))

with open('res.txt', 'w') as res:
    # 对每一行能txt文件遍历
    for row in contenttxt:
        flag = False
        # 遍历csv文件每一行
        for r in csvfile:
            # 比较，如果满足条件，取出csv文件第二个元素
            if row.strip() == r0:
                flag = True
                res.write(r1 + '\n')
                break
        # 如果没有满足条件，存储'nofound'
        if flag == False:
            res.write('nofound' + '\n')

