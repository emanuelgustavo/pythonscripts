'''
gerador aleatorio de IP para o exercicios de verificação de IPs
'''
import random

ips = []

qtdeIps = int(input("Digite a quantidade de Ips a gerar: "))
i = 0
contadorDeIps = 1

while i < qtdeIps:
    ip = ''
    j = 0
    while j < 4:
        ip += str(random.randint(1, 300))
        if j < 3:
            ip += '.'
        j += 1
    if ip not in ips:
        ips.append(ip)
    i += 1
    print('%d de %d ip(s) gerado(s)' %(contadorDeIps, qtdeIps))
    contadorDeIps += 1
    

ipsFile = open('ipsFile.txt', 'w')
for ip in ips:
    ipsFile.write('%s \n' % ip)        
ipsFile.close()
