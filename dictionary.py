print('Criando um dicionário e acessando pelo índice')
new_dict = {1:'Hello', 2:'Hi', 3:'Hola'}
print(new_dict)
print('Elemento da chave 1: ', new_dict[1])
print('Elemento da chave 2: ', new_dict.get(2))

new_dict[1] = 'Hey'
print('Alterando o valor da chave 1: ', new_dict)

new_dict[4] = 'Namaste'
print('Adicionando um novo chave/valor: ', new_dict)

print('\n')
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)
print('Removendo a chave 4: ', squares.pop(4))
print('Removendo uma chave/valor de forma arbitrária: ', squares.popitem())

del squares[1]
print('Removido a chave 1: ', squares)

squares.clear() #limpando um dicionário
print(squares)

del squares #removendo o dicionário

print('\nCriando um dicionário por "Comprehension"')
squares = {x: x * x for x in range(6)}
print(squares)

print('\nTeste com membros do dicionário')
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print('O número 1 está na chave do dicionário: ', 1 in squares)
print('O número 2 não está na chave do dicionário: ', 2 not in squares)
print('O número 49 está na chave do dicionário: ', 49 in squares)

print('\nIterando no dicionário')
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i]) #valor de cada chave

print('\nBuilt-in functions')
squares = {9:81, 1:1, 3:9, 5:25, 7:49}
print(squares)
print('Chaves do dicionário ordenada: ', sorted(squares))
print('Tamanho do dicionário: ', len(squares))
