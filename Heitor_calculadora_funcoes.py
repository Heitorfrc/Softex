'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando 
infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair
Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a 
mensagem “Essa opção não existe” e voltar ao menu de opções.
Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa 
executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar
'''

def calculadora(oper):
    if (oper < 0 or oper > 4):
        return "Essa código de operação não existe"
    num1, num2 = entra_valores()
    if oper == 1 :
        return num1 + num2
    elif oper == 2 :
        return num1 - num2
    elif oper == 3 :
        return num1 * num2
    elif oper == 4 :
        if num2 != 0 :
            return num1 / num2
        else :
            raise Exception("Não é possível dividir por zero")
    
def imprime_opcoes():
    print ("Esses são os codigos das operações:")
    print ("1: Soma")
    print ("2: Subtração")
    print ("3: Multiplicação")
    print ("4: Divisão")
    print ("0: Sair do programa")

def entra_valores():
    numero1 = float(input("Digite o primeiro valor da operação: "))
    numero2 = float(input("Digite o segundo valor da operação: "))
    return numero1, numero2

while True:
    imprime_opcoes()
    try :
        operacao = int(input("Digite o código da operação: "))
        if(operacao == 0):
            break
        resultado = calculadora(operacao)
        print ("Resultado: ", resultado)
    except Exception as e :
        print("Erro")
        print (e)
