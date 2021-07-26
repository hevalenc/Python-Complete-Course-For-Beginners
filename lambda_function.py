a = lambda x: x * 2
print('Double of 10 is ', a(10))

print('\nCriando uma nova lista com números pares da lista antiga')
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
print(my_list)
new_list = list(filter(lambda  x: (x % 2 == 0), my_list))
print(new_list)

print('\nProgramar o dobro de cada item da lista usando o map()')
print(my_list)
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
