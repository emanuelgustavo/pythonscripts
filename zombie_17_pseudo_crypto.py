'''
pseudo crypto

Leia mensagem.txt e grave cript.txt com todas as vogais trocadas por '*'
'''

with open('mensagem.txt', 'r') as mensagem:
    texto = mensagem.read()

novoTexto = ''

for vogal in texto:
    if vogal in 'aeiou':
        novoTexto += '*'
    else:
        novoTexto += vogal

with open('crypto.txt', 'w') as crypto:
    crypto.write(novoTexto)
