meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Maio',
         'Junho',
         'Julho',
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

dia, mes, ano = str(input("Digite uma data: ")).split('/')
print(dia + " de " + meses[int(mes)-1] + " de " + ano)

