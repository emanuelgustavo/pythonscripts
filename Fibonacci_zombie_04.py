'''
fibonacci
'''

a, b = 1, 0
k = 1

n = int(input("Digite o numero de termos de fibonacci: "))

while k <= n:
    a, b = b, a + b
    k += 1

print("Fib(%d) é: %d: " %(n, b))
