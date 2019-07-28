'''
validador de Ip
'''

ipsValidos = open('ipsValidos.txt', 'w')
ipsInvalidos = open('ipsInvalidos.txt', 'w')

with open('ipsFile.txt', 'r') as ips:
    for ip in ips:
        testeIp = ip.split('.')
        ipValido = True
        for parteIp in testeIp:
            if int(parteIp) > 255:
                ipValido = False
        if ipValido:
            ipsValidos.write('%s\n' %ip)
        else:
            ipsInvalidos.write('%s\n' %ip)

ipsValidos.close()
ipsInvalidos.close()
