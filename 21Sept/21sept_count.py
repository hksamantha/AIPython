file1 = open("myfile.txt", "r")
read_content = file1.read()
words = read_content.split()
count = len(words)
print(count)


