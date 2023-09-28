def newline(string_list, file_name):
    with open(file_name, "w") as output_file:
        for string in string_list:
            output_file.write(string+"\n")

string_list= ["This is awesome", "I Love Programming", "We talked about file handling", "Hello world"]

newline(string_list, "output.txt")

