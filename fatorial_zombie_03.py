n = int(input("Digite um numero para fatorial: "))

if n == 0:
    print(0)
else:
    total = 1

    while n != 0:
        total *= n
        n -= 1

    print(total)
