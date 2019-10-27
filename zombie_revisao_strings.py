import urllib.request
import time

def comprar_cafe():
    preco = busca_preco()
    return ('Café comprado a {}'.format(preco))

def busca_preco():
    pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html'
    )
    texto = pagina.read().decode('utf8')
    onde = texto.find('>$')
    inicio = onde + 2
    fim = onde + 6
    preco = float(texto[inicio:fim])
    return preco

def main():

    preco = 99.99
    opcao = input('Deseja comprar já? S/N')
    if opcao.upper() == 'S':
        print(comprar_cafe())
    else:        
        while preco >= 4.74:
            time.sleep(600)
            preco = busca_preco() 
            print(preco)    
        print(comprar_cafe())
        
main()