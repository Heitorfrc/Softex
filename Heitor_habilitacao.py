'''
Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;  A
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;  B
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;  C
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;  D
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.  E
'''
#Nesse exercício algumas categorias se sobrepoem, vamos usar o bom senso e escolher a melhor categoria pela ordem que foi dada

rodas = int(input("Digite o número de rodas do veículo: "))
peso = float(input("Digite o peso bruto em Kg do veículo: "))
pessoas = int(input("Digite o número de pessoas no veículo: "))

if rodas == 4 and pessoas <= 8 and peso <= 3500 :
    print("A categoria de habilitaçâo do veículo é B")
elif rodas >= 4 and peso <= 6000 :
    print("A categoria de habilitaçâo do veículo é C")
elif rodas >= 4 and pessoas > 8 :
    print("A categoria de habilitaçâo do veículo é D")
elif rodas >= 4 and peso > 6000 :
    print("A categoria de habilitaçâo do veículo é E")
elif rodas < 4 and rodas > 1 :
    print("A categoria de habilitaçâo do veículo é A")
else :
    print("Escolha um veículo que possa ser habilitado")
