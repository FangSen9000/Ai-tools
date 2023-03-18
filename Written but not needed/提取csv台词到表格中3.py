# Python code: 

import csv 

with open('how2sign_realigned_val.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) 

    with open('new_data.csv', 'w') as new_file: 
        csv_writer = csv.writer(new_file, delimiter=',') 

        for line in csv_reader: 
            csv_writer.writerow(line[0].split(" "))
