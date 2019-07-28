'''
algoritmo de euclides
'''
a = int(input("Digite um numero inteiro: "))
b = int(input("Digite um numero inteiro: "))
'''
resto = 1

while resto != 0:

    q = a / b
    resto = a % b
    a = b
    if resto != 0:
        b = resto        
    
    print("A: %d, B: %d, Q: %d, R: %d" %(a, b, q, resto))
'''

while a % b != 0:
    a, b = b, a % b
    
print("MDC: %d" %b)

    
