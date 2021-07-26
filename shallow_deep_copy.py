print('Copiando uma lista')
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = list1

print('List 1: ', list1)
print('List 2: ', list2)
print('id of list 1: ', id(list1))
print('id of list 2: ', id(list2))

list1.append([10, 11, 12])
print('List 1: ', list1)
print('List 2: ', list2)

print('\nCriando uma cópia usando o Shallow Copy')
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print('Old list: ', old_list)
print('New list: ', new_list)
print('id of Old list: ', id(old_list))
print('id of New list: ', id(new_list))

print('\nAdicionando elementos para a old_list')
old_list.append([4, 4, 4])
print('Old list: ', old_list)
print('New list: ', new_list)

print('\nAdicionando novo objeto aninhado')
old_list[1][1] = 'AA'
print('Old list: ', old_list)
print('New list: ', new_list)
old_list[3][1] = 'BB'
print('Old list: ', old_list)
print('New list: ', new_list)

print('\nCopiando uma lista com o Deep Copy')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
print('Old list: ', old_list)
print('New list: ', new_list)
print('id of Old list: ', id(old_list))
print('id of New list: ', id(new_list))


print('\nAdicionando um ovo objeto aninhdo na old_list')
old_list[1][0] = 'BB'
print('Old list: ', old_list)
print('New list: ', new_list)
