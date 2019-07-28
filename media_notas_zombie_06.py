notas = [10,10,10,8,9.3]

totalNotas = 0
x = 0

while x < 5:
    totalNotas += notas[x]
    print("Nota %d = %.2f" %(x, notas[x]))
    x += 1

print("Média: %.2f" %(totalNotas/x))
