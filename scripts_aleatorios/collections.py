import collections
import random

c = collections.Counter('helloworld!')

print(c)
print(c.most_common())

numeros = [random.randint(1,60) for x in range(2**10)]
print(numeros)

c = collections.Counter(numeros)
print(c.most_common(5))