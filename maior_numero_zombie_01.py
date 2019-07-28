'''
tres numeros e determinar o maior deles
'''

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a >= b and a >= c:
    print("O maior número é %d" %a)
elif b >= c:
    print("O maior número é %d" %b)
else:
    print("O maior número é %d" %c)
