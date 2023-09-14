#your string and separator both you can input
separator=input("Enter separator: ")
def split_strings(your_string):
    return your_string.split(separator)

print(list(split_strings(input("Enter your string: "))))
