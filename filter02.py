strings = ["This is apple", "I love carrot",
           "This city is beautiful", "Australia has apple gardens"]


def search_apple(sentence):
    return "apple" in sentence


apple_sent = filter(search_apple, strings)

print(list(apple_sent))
