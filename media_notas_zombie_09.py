notas = []

x = 1
soma = 0

while x <= 4:
    notas.append(float(input("Digite a nota %d:" %x)))
    soma += notas[x-1]
    x += 1
    
print("Notas inseridas: \n", notas)
print("Média: ", soma/(x-1))
