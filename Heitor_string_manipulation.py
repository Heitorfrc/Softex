'''
Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado.
'''

from tokenize import String


frase = str(input("Escreva uma frase: "))
maiusculo = frase.upper()
titulo = frase.title()
qntDoCaractere = frase.count("a")
qntLetras = frase.

print("Sua frase gritando:")
print(maiusculo, "!!", sep="")

print("Sua frase como título de um livro:")
print(titulo)

print("Quantas vezes voce utilizou o caractere 'a':")
print(qntDoCaractere)