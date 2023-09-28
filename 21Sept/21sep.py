file1 = open("myfile_1.txt", "w")

L = ["This is something new\n", "The writelines() method" ]

file1.writelines(L)

file1.close()