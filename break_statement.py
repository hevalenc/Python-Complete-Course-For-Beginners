import random as r

rand_num = r.randrange(1, 20)
print('Primeiro número sugerido: ', rand_num)

i = 1

while True:
    print('Número sugerido: ', i)
    if (i == rand_num):
        print('Número sugerido aleatoriamente com sucesso!!!')
        break #o loop será interrompido quando a condição for satisfeita
    i += 1