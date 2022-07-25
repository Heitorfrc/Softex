'''
Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou 
reprovado de acordo com as especificações:

- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.

No sistema, todos os valores devem estar armazenados em variáveis.

'''

nomeAluno = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

media = (nota1 + nota2)/2


if faltas > 3:
    print(nomeAluno, "está reprovado por faltas")
else:
    if media < 7:
     print(nomeAluno, "está reprovado por média")
    else:
     print(nomeAluno, "está aprovado por média")