import random

upper_char = ["A", "B", "C", "D", "E"]
lower_case = ["a", "b", "c", "d", "e"]
num = ["1", "2", "3", "4", "5", "6"]
special_char = ["@", "#", "^", "&", "!"]

passw = (
    random.choice(upper_char)
    + random.choice(lower_case)
    + random.choice(num)
    + random.choice(special_char)
)
print(passw)