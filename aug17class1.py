my_list = ['may be', 'Australia', 'USA is a',
           'Apple can be', 'it is', 'Amazingly bea']
count = 0
for word in my_list:
    new_list = word.split()
    if 'be' in new_list:
        count += 1
print(count)
