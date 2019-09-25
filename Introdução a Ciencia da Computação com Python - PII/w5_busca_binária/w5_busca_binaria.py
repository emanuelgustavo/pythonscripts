class Buscador:

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1
        while primeiro <= ultimo:            
            meio = (primeiro + ultimo) // 2
            #print('meio: ',meio)
            #print('lista[meio]: ',lista[meio])
            if lista[meio] == x:
                return [meio, lista[meio]]
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
            

def main():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    busca = Buscador()
    print(busca.busca_binaria(lista, 8))
    
main()
