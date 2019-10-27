'''
Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
Entre 200 e 400 minutos, o preço é R$0,18. Acima de 400 minutos o preço por minuto é R$ 0,15. Calcule sua 
conta de telefone.
'''

def contaDeTelefone(minutosUtilizados):

    if minutosUtilizados < 200:

        return minutosUtilizados * 0.20

    else:

        if minutosUtilizados < 400:
    
            return minutosUtilizados * 0.18
    
        else:
    
            return minutosUtilizados * 0.15

def main():

    op = 1

    while op == 1:

        print("----Menu----")
        print("1 - Calcular Conta:")
        print("2 - Sair")
        op = int(input("Digite uma opcao: "))

        if op == 1:

            minutos = int(input("Digite a quantidade de minutos utilizados: "))
        
            print("O valor da sua conta de telefone é: R$%.2f" % contaDeTelefone(minutos))
           

main()