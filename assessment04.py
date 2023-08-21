s = input("Input: ")
ns = s.split()
if ns[-1] == ' ':
    print(len(ns[-2]))
else:
    print(len(ns[-1]))
