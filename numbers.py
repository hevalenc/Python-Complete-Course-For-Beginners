print('Número do tipo Integer - inteiro')
value1 = 100

print(type(value1))
print('O dado value1 é int: ', isinstance(value1, int))
print('O dado value1 é float: ', isinstance(value1, float))
print('O dado value1 é complex: ', isinstance(value1, complex))

print('\nNúmero do tipo Float - ponto flutuante')
value2 = 100.24

print(type(value2))
print('O dado value2 é int: ', isinstance(value2, int))
print('O dado value2 é float: ', isinstance(value2, float))
print('O dado value2 é complex: ', isinstance(value2, complex))

print('\nNúmero do tipo Complex - um número complexo com parte real e parte imaginária')
value3 = 50 + 6j

print(type(value3))
print('O dado value3 é int: ', isinstance(value3, int))
print('O dado value3 é float: ', isinstance(value3, float))
print('O dado value3 é complex: ', isinstance(value3, complex))

print('\nRepresentação em outras unidades núméricas para decimal')
print('Representação binária (0b1101): ', 0b1101)  #0b - binário
print('Representação hexadecimal (0xab): ', 0xab)  #0x - hexadecimal
print('Representação octal (0o23): ', 0o23)  #0o - octal

print('\nConversão de tipo')
print('Float para int (10.5): ', int(10.5))
print('Float para int (-20.99): ', int(-20.99))
print('Int para float (10): ', float(10))

"""
print('\nDecimal em Python')
print(0.1 + 0.2)
print(1.20 * 2.50)

from decimal import Decimal as D
print(D('0.1') + D('0.2'))
print(D('1.2') * D('2.5'))

print('\nFrações em Python')
from fractions import Fraction as F

print(F(1.5))
print(F(5))
print(F(1,5))
"""

print('\nMatemática no Python')
import math
print('PI: ', math.pi)
print('Cosseno de 10: ', math.cos(10))
print('Log de 10: ', math.log(10))  #Com um argumento, retorna o logaritmo natural de x (para base e).
print('Log10 de 10: ', math.log10(10))  #Retorna o logaritmo de base 10 de x. Isso geralmente é mais preciso do que log(x, 10).
print('Exponencial de 10: ', math.exp(10))  #Retorna e elevado à potência x, onde e = 2.718281… é a base dos logaritmos naturais.
print('Fatorial de 5: ', math.factorial(5))  #Retorna x fatorial como um inteiro.
print('Seno hiperbólico de 10: ', math.sinh(10))

print('\nNúmeros aleatórios em Python - Random')
import random

print('Número aleatório entre 5 e 15: ', random.randrange(5, 15))
print('Número aleatório entre 5 e 15: ', random.randrange(5, 15))
print('Número aleatório entre 5 e 15: ', random.randrange(5, 15))
print('Número aleatório entre 5 e 15: ', random.randrange(5, 15))

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print('Escolha aleatória do dia da semana: ', random.choice(day))

print('Dias da semana antes do shuffle: ', day)
random.shuffle(day)
print('Dias da semana após o shuffle: ', day)

print('Número aleatório gerado pelo random: ', random.random())

