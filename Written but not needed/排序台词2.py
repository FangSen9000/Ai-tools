import csv

txt_file = open("dev.txt", "r")
csv_file = open("how2sign.csv")

csv_reader = csv.reader(csv_file)

res_file = open("res.txt", "w")

for line in txt_file.readlines():
    line = line.strip()

    found_flag = False
    for content in csv_reader:
        if line == content[0]:
            res_file.write(content[1] + "\n")
            found_flag = True
            break

    if not found_flag:
        res_file.write("nofound\n")

txt_file.close()
csv_file.close()
res_file.close()
