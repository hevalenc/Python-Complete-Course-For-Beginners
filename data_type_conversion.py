print('Conversão de tipo implícito')
num_int = 123
num_flo = 12.3

num_new = num_int + num_flo #conversão de tipo através de cálculo

print('Tipo do dado de num_int: ', type(num_int))
print('Tipo do dado de num_flo: ', type(num_flo))
print('Valor de num_new: ', num_new)
print('Tipo do dado de num_new: ', type(num_new))

print('\nAdição de uma string (maior) e um integer (menor)')
num_int = 123
num_str = '456'

print('Tipo do dado de num_int: ', type(num_int))
print('Tipo do dado de num_str: ', type(num_str))
#print(num_int + num_str) #não é possível fazer conversão implícita de string para integer

print('\nConversão de tipo explícito')
num_int = 123
num_str = '456'

print('Tipo do dado de num_int: ', type(num_int))
print('Tipo do dado de num_str antes da conversão: ', type(num_str))

num_str = int(num_str) #conversão do tipo string para integer
print('Tipo do dado de num_str após a conversão: ', type(num_str))

num_sum = num_int + num_str
print('Soma do num_int e num_str: ', num_sum)
print('Tipo do dado de num_sum: ', type(num_sum))

