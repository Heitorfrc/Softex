'''Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números. 
'''

import cmath

a = 4 + 2j
b = 7 + 6j

c = a + b
print ("A parte real do número somado é : ", c.real)
print ("A parte imaginária do número somado é : ", c.imag)

d = a - b
print ("A parte real do número subtraído é : ", d.real)
print ("A parte imaginária do número subtraído é : ", d.imag)

e = a * b
print ("A parte real do número dividido é : ", e.real)
print ("A parte imaginária do número dividido é : ", e.imag)

f = a / b
print ("A parte real do número multiplicado é : ", f.real)
print ("A parte imaginária do número multiplicado é : ", f.imag)



