import random

num = ["1", "2", "3", "4", "5", "6"]
special_char = ["@", "#", "^", "&", "!"]
wordlist = []
with open("hello.txt", "r") as file:
    data = file.readlines()

    for line in data:
        words = line.split()

        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())

word = random.choice(wordlist)
shar = random.choice(special_char)
num = random.randint(100, 1000)
print(word + shar + str(num))