import json

student_data = {
   "name": "John Nash",
   "Maths": 60,
   "Science": 55,
   "English": 70
}

def cal_average(student_data):

    sum_marks = 0
    for subject, score in student_data.items():
        if subject != "name":
            sum_marks += score
    average = sum_marks / (len(student_data) - 1)
    
    print(average)

    new_data = {
        "name":student_data["name"],
        "average": average
    }

    with open('test.json', 'w') as json_file:

        json_data = json.dumps(new_data)

        json_file.write(json_data)

cal_average(student_data)