'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. 
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando
até que um valor correto seja preenchido
'''

def idadeCalc(num) :
    return 2022 - num

nome = str(input("Digite seu nome completo: "))

perguntas = True
while(perguntas) :
    try :
        ano = int(input("Digite seu ano de nascimento: "))
        if ano < 1922 or ano > 2021 :
            print("O ano inserido deve ser entre 1922 e 2021")
        else :
            print(idadeCalc(ano))
            perguntas = False
    except Exception as e :
        print("Erro, valor inserido incorretamente")
        print(e)
        
