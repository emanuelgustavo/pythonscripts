palavra = str(input("Digite uma palavra: "))

import random

np = list(palavra)
random.shuffle(np)
np = ''.join(np)

print(np)
