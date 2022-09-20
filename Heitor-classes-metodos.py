'''
Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva 
três ou mais objetos para testar o código.
Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo 
ao lado para que outros desenvolvedores possam analisá-lo.
'''

class Funcionario :
    contadorFuncionario = 0
    def __init__(self, nome, idade, faltas) :
        self.nome = nome
        self.idade = idade
        self.faltas = faltas
        Funcionario.contadorFuncionario += 1


f1 = Funcionario(input("Digite o nome do funcionario: "), input("Digite a idade do funcionario: "), input("Digite o número de faltas do funcionario: "))

f2 = Funcionario(input("Digite o nome do funcionario: "), input("Digite a idade do funcionario: "), input("Digite o número de faltas do funcionario: "))

f3 = Funcionario(input("Digite o nome do funcionario: "), input("Digite a idade do funcionario: "), input("Digite o número de faltas do funcionario: "))


print("O nome do funcionário é", f1.nome,", sua idade é", f1.idade, "e tem", f1.faltas, "faltas.")
print("O nome do funcionário é", f2.nome,", sua idade é", f2.idade, "e tem", f2.faltas, "faltas.")
print("O nome do funcionário é", f3.nome,", sua idade é", f3.idade, "e tem", f3.faltas, "faltas.")
print("O total de funcionários é", Funcionario.contadorFuncionario)
