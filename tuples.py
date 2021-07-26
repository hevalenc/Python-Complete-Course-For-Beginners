print('Criando tuplas, similar a lista, e são imutáveis')
tuple1 = ()
print('Tupla vazia: ', tuple1)

tuple2 = (1, 2, 3)
print('Tupla com números: ', tuple2)

tuple3 = (101, 'Anirban', 20000.00, 'HR Dept')
print('Tupla mista: ', tuple3)

tuple4 = ('points', [1, 4, 3], (7, 8, 6))
print('Tupla aninhada (nested): ', tuple4)

tuple5 = 101, 'Anirban', 20000.00, 'HR Dept'
print('Tupla criada sem parentesis: ', tuple5)

empid, empname, empsal, empdep = tuple5 #nomeando os índices da tupla
print(empid)
print(empname)
print(empsal)
print(empdep)
print(type(tuple5))

print('\nAcessando os elementos de uma tupla')
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])

nest_tuple = ('point', [1, 3, 4], (8, 7, 9))
print(nest_tuple)
print(nest_tuple[0][3])
print(nest_tuple[1][2])
print(nest_tuple[2][2])

print('\nFatiando uma tupla')
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])

print('\nPodem ser renomeadas, porém são imutáveis')
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
#tuple1[2] = 'x' #gera erro de código

tuple1 = ('g', 'o', 'o', 'd', ' ', 'b', 'y','e')
print(tuple1)

print('\nConcatenando as tuplas')
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o', 'm', 'e')
print(tuple2)
print(tuple3)
print(tuple2 + tuple3)

print(('again', ) * 4)

print('\nMétodos em tuplas')
tuple5 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple5)
print('Quantos letras "e" tem na tupla: ', tuple5.count('e'))
print('Qual é o índice da letra "c": ', tuple5.index('c'))

print('A letra "c" está na tupla: ', 'c' in tuple5)
print('A letra "c" não está na tupla: ', 'c' not in tuple5)
print('A letra "a" está na tupla: ', 'a' in tuple5)
print('A letra "a" não está na tupla: ', 'a' not in tuple5)

print('\nIteração nos elementos da tupla')
tuple5 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
for letters in tuple5:
    print('letter is -> ', letters)

print('\nBuilt-in functions')
tuple7 = (22, 33, 55, 44, 77, 66, 11)
print(tuple7)
print('Maior número: ', max(tuple7))
print('Menor número: ', min(tuple7))
print('Tupla ordenada: ', sorted(tuple7))
print('Tamanho da tupla: ', len(tuple7))
