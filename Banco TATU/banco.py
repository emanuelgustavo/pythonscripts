from cliente import Cliente
from conta import Conta

nomeCliente = input('Digite o nome do cliente: ')
telefoneCliente = input('Digite o telefone do cliente: ')

cliente = Cliente(nomeCliente, telefoneCliente)

conta = Conta(cliente, 1, 1000)

conta.resumo()

conta.deposito(1000)
conta.saque(250)
conta.deposito(235)
conta.saque(700)
conta.saque(500)

conta.resumo()

conta.extrato()
        
