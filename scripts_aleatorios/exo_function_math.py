import random

def main():
    op = 0
    while op >= 0:
        aleatorio = random.randint(0,100)
        op = int(input('Digite um número inteiro: '))
        if op == aleatorio:
            print('Você descobiu o numero aleatorio! => {} '.format(aleatorio))
            print(exp_function_math(fat(op)))
        else:
            print(exp_function_math(op))

def exp_function_math(x):
    return x**x

def fat(n):
    if n == 0:
        return 1
    else: return fat(n-1)*n

main()
