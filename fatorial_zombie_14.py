'''fatorial
'''

n = int(input("Digite um numero: "))


def fatorial(n):
    if n == 0:
        return 1
    else:
        return fatorial(n-1)*n

print(fatorial(n))
