print('Criando um Set que é uma collection que representa conjunto')
my_set1 = {11, 33, 66, 55, 44, 22}
print('Set de inteiros: ', my_set1)

my_set2 = {101, "Angibha", (21, 2, 1994)}
print('Set de dados mistos: ', my_set2)

my_set3 = {11, 22, 33, 33, 44, 22}
print('Números repetidos não são aceitos: ', my_set3)

my_set4 = set([1, 2, 3, 2])
print('Set feito com uma lista: ', my_set4)
print(type(my_set4))

my_list1 = list({11, 22, 33, 44})
print('Lista feita com um set: ', my_list1)
print(type(my_list1))

print('\nOperações com Set ADD e UPDATE, um set não suporta indexação')
my_set1 = {11, 33, 44, 66, 55}
print(my_set1)

my_set1.add(77)
print('Adicionando um elemento ao set: ', my_set1)

my_set1.update([88, 99, 22])
print('Adicionando vários elementos ao set: ',my_set1)

my_set1.update([100, 102], {102, 104, 105})
print('Adicionando uma lista e um set: ', my_set1)

print('\nDISCARD e REMOVE')
my_set1 = {11, 33, 44, 66, 55}
print(my_set1)

my_set1.discard(4) #se o elemento não estiver no set, não haverá erro
print(my_set1)

#my_set1.remove(6) #se o elemento não estiver no set, retornará um erro

my_set1.discard(44)
my_set1.remove(66)
print(my_set1)

print('\nPOP e CLEAR, pop remove o primeiro elemento do set e o clear limpa o set')
my_set1 = {11, 33, 44, 66, 55}
print(my_set1)
print(my_set1.pop())
print(my_set1.pop())
print(my_set1)

my_set1.clear()
print(my_set1)

print('\nOperações com set - UNION')
my_set1 = {0, 1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8, 9}
print('Set 1: ', my_set1)
print('Set 2: ', my_set2)
print(my_set1 | my_set2)
print(my_set2 | my_set1)
print(my_set1.union(my_set2))
print(my_set2.union(my_set1))

print('\nOperações com set - INTERSECTION')
print('Set 1: ', my_set1)
print('Set 2: ', my_set2)
print(my_set1 & my_set2)
print(my_set2 & my_set1)
print(my_set1.intersection(my_set2))
print(my_set2.intersection(my_set1))

print('\nOperações com set - DIFFERENCE')
print('Set 1: ', my_set1)
print('Set 2: ', my_set2)
print(my_set1.difference(my_set2))
print(my_set2.difference(my_set1))

print('\nOperações com set - SYMMETRIC DIFFERENCE')
print('Set 1: ', my_set1)
print('Set 2: ', my_set2)
print(my_set1.symmetric_difference(my_set2))
print(my_set2.symmetric_difference(my_set1))

print('\nVerificar se um elemento pertence a um set')
my_set1 = {0, 1, 2, 3, 4, 5}
print(my_set1)
print('O número 2 está no set: ', 2 in my_set1)
print('O número 6 está no set: ', 6 in my_set1)
print('O número 2 não está no set: ', 2 not in my_set1)
print('O número 6 não está no set: ', 6 not in my_set1)

print('\nIterando em um set')
for letters in set('welcome'):
    print(letters) #não irá aparecer as letras na sequência correta

print('\nBuilt-in functions')
my_set1 = {0, 11, 2, 33, 4, 5}
print(my_set1)
print('Maior número: ', max(my_set1))
print('Menor número: ', min(my_set1))
print('Set ordenado: ', sorted(my_set1))
print('Tamanho do set: ', len(my_set1))

print('\nPython Frozenset:')
print('is the same as set except the forzensets are immutable which means that elements'
      ' from the frozenset cannot be added or removed once created.')
my_set1 = frozenset([1, 2, 3, 4])
my_set2 = frozenset([3, 4, 5, 6])
print('Set 1: ', my_set1)
print('Set 2: ', my_set2)
print(my_set1.difference(my_set2))
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.symmetric_difference(my_set2))
