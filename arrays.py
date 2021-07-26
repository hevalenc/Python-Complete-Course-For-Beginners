print('Criando um array e acessando os elementos pelo índice')
arr = [10, 20, 30, 40, 50]
print(arr)

print('Elemento do índice 0: ', arr[0])
print('Elemento do índice 1: ', arr[1])
print('Elemento do índice 2: ', arr[2])
print('Elemento do último índice: ', arr[-1])
print('Elemento do penúltimo índice: ', arr[-2])

brands = ["coke", "apple", "google", "microsoft", "toyota"]
print('\nNovo array: ', brands)

num_brands = len(brands)
print('Contando os elementos de um array: ', num_brands)

brands.append("intel")
print('Adicionando um alemento ao array: ', brands)

print('\nRemovendo um elemento do array')

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
print(colors)

del colors[4]
print('Removendo o elemento do índice 4: ', colors)

colors.remove('blue')
print('Removendo a cor azul: ', colors)

colors.pop(3)
print('Removendo o elemento do índice 3: ', colors)

print('\nModificando os elementos de um array')
fruits = ['apple', 'banana', 'mango', 'grapes', 'orange']
print(fruits)

fruits[1] = 'pineaple'
print('Mudando o índice 1: ', fruits)

fruits[-1] = 'guava' #modificando o último elemento
print('Mudando o último índice: ', fruits)

print('\nConcatenando dois arrays com o operador "+"')
concat = [1, 2, 3]
print(concat)

concat2 = concat + [4, 5, 6]
print(concat2)

print('\nRepetindo os elementos de um array')
repeat = ['a']
print(repeat)

repeat = repeat * 5
print(repeat)

print('\nFatiando um array')
fruits = ['apple', 'banana', 'mango', 'grapes', 'orange']
print(fruits)
print('Frutas entre os índices 1 ao 3: ', fruits[1:4])
print('Frutas entre os índices 0 ao 0: ', fruits[:3])
print('Frutas entre os índices 4 ao 1: ', fruits[-4:])
print('Frutas entre os índices 3 ao 2: ', fruits[-3:-1])

print('\nDeclarando e definindo um array multi-dimensional')
multd = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])

