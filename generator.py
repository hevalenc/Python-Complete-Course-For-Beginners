print('Função Gerador Simples')
def my_generator():
    n = 1
    print('This is printed first')
    '''generator function contains yield statements'''
    yield n #produce or provide -> usado como um acumulador

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed last')
    yield n

a = my_generator()
'''Interação usando o next'''
next(a)
next(a)
next(a)

print('Using for loop ...')
for item in my_generator():
    print(item)

print('\nGeradores com um Loop')
def reverse_string(my_string):
    length = len(my_string)
    for i in range(length -1, -1, -1): #range(start, stop[, step]) -> contador reverso
        yield my_string[i]

for char in reverse_string('WORLD'):
    print(char)

