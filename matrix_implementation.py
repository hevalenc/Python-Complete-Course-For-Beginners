print('Matriz 2-D com inteiros')
a = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75, 85, 100],
     ['Dave', 80, 80, 80,90, 95]]
print(a)

print('\nLista aninhada, mas não é uma matriz')
b = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75],
     ['Dave', 80, 80, 80,90, 95]]
print(b)

print('\nCriando uma matriz dinamicamente usando o loop FOR')
n = 3
m = 4
a = [0] * n
print(a)

for i in range(n):
    a[i] = [0] * m
print(a)

print('\nAcessando os elementos de uma matriz')
print(a)
print(a[0])
print(a[0][1])
print(a[1][2])

print('\nÍndice negativo')
print(a)
print(a[-1])
print(a[-1][-2])
print(a[-2][-3])

print('\nMudando os elementos de uma matriz')
print('a = ', a)
b = a[0]
print('b = ', b)

b[1] = 75
print('b = ', b)
print('a = ', a)

a[2] = ['Sam', 82, 79, 88, 97, 99]
print('a = ', a)
