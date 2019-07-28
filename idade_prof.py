import datetime

class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.idade = self.idade()
        return super().__init__(nome, nascimento)
    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int(delta.days/365)
    def __str__(self):
        return '{}, {} anos'.format(self.nome, self.idade)

emanuel = Pessoa('Emanuel G Vierne', datetime.date(1991,8,30))
print(emanuel.idade)
print(emanuel)
