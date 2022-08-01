'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''

def calculadora(num1, num2, oper):
    if oper == 1 :
        return num1 + num2
    if oper == 2 :
        return num1 - num2
    if oper == 3 :
        return num1 * num2
    if oper == 4 :
        return num1 / num2
    if oper < 1 or oper > 4 :
        return 0

numero1 = float(input("Digite o primeiro número da operação: "))
numero2 = float(input("Digite o segundo número da operação: "))
operacao = int(input("Digite o código da operação: "))

resultado = calculadora(numero1, numero2, operacao)
print (resultado)