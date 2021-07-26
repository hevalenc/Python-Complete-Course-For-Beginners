print('Criando um loop com While')
i = 3
while i > 0:
    print(i)
    i -= 1

print()
while i < 10:
    print(i)
    i += 1
else:
    print('Displayed Successfully!!!')

print('\nPrograma para mostrar um padrão usando loops')
n = int(input('Please enter the number of layers: '))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print('.', end = "")
        j += 1

    j = 1
    while j <= 2 * i - 1:
        print('*', end = "")
        j += 1

    print()
    i = i + 1

print()
n = int(input('Please enter the number of layers: '))
m = (n + 1) / 2
i = 1
while i <= n:
    if (i > m):
        b = n - i
        s = 2 * (i - m) + 1
    else:
        b = i - 1
        s = 2 * (m - i)

    j = 1
    while j <= b:
        print('.', end = "")
        j += 1

    j = 1
    while j <= s:
        print('*', end = "")
        j += 1

    print()
    i = i + 1
