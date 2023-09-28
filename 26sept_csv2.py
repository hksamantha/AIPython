import csv

# Data to be written to the CSV file (a list of dictionaries)
data = [
   {"Name": "John Doe", "Age": 30, "City": "New York"},
   {"Name": "Jane Smith", "Age": 28, "City": "Los Angeles"},
   {"Name": "Bob Johnson", "Age": 35, "City": "Chicago"}
            ]
# Define the CSV fieldnames (column names)
fieldnames = ["Name", "Age", "City"]   

with open('sample_output.csv', 'w',newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    for row in data:csv_writer.writerow(row)


