from random import random
import string

numbers = list(round(random() * 10) for i in range(26))
alfa = list(string.ascii_lowercase)

enum = enumerate(zip(alfa, numbers))
di = {key: velue for key, velue in enum}

for k, v in di.items():
    print(f"key: {k}, value: {v}")

