print('Iterando uma string em uma lista através de um loop')
h_letters = []

for letter in 'human':
    h_letters.append(letter)
    print(h_letters)

print(h_letters)

print('\nUsando o Comprehension')
h_letters = [letter for letter in 'human']
print(h_letters)

print('\nList Comprehensions vs Lambda Function')
h_letters = list(map(lambda x: x, 'human'))
print(h_letters)

print('\nIf com List Comprehension')
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

print('\nIf aninhado com List Comprehension')
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

print('\nIf e Else com List Comprehension')
obj = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
print(obj)

print('\nTranspondo uma matriz usando List Comprehension')
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(matrix)
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)