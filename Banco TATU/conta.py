class Conta:

    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC número: {}\nTitular: {}\nSaldo: {}'.format(self.numero, self.clientes.nome, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
           self.saldo -= valor
           self.operacoes.append(['Saque: ', valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Deposito: ', valor])

    def extrato(self):
        print('----Extrato----')
        print('Titular: {}  CC: {}'.format(self.clientes.nome, self.numero))
        print('Tipo  Valor  Saldo'.format(self.clientes.nome, self.numero))
        for op in self.operacoes:
            print('{}  {}  {}'.format(op[0], op[1], self.saldo))
