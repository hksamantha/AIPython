import csv

with open('sample_data.csv','r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)