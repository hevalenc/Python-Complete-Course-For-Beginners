print('Modos diferentes de definir uma String')
mystr1 = 'Welcome'
print('Com aspas simples: ', mystr1)

mystr2 = "Welcome"
print('Com aspas duplas: ', mystr2)

mystr3 = '''Welcome'''
print('Com 3 aspas simples: ', mystr3)

mystr4 = """Welcome
to the world of
Python programming""" #3 aspas duplas podem extender múltiplas linhas
print('Com 3 aspas duplas: ', mystr4)

print('\nAcessando os caracteres de uma string')
mystr = 'language'
print(mystr)

print('Caracter no índice 0: ', mystr[0])
print('Caracter no último índice: ', mystr[-1])
print('Caracter entre os índices 1 ao 4: ', mystr[1:5])
print('Caracter entre os índices 5 e -3: ', mystr[5:-2])
#print('Caracter no índice 10: ', mystr[10]) #se o índice não existir, será lançado um erro

print('\nConcatenação de duas strings')
mystr1 = 'Welcome'
mystr2 = ' to all'
print(mystr1)
print(mystr2)
print('União das duas strings: ', mystr1 + mystr2)
print('Repetição de uma string: ', mystr1 * 3)

print('\nIterando através de uma string')
letter_count = 0
for letters in 'Hello World':
    if (letters == 'l'):
        letter_count += 1
print('Quantas vezes foram encontrados a letra l: ', letter_count)

print('\nMembro de uma string')
print('A letra l está na palavra hello: ', 'l' in 'hello')
print('A letra l não está na palavra hello: ', 'l' not in 'hello')
print('A letra b está na palavra hello: ', 'b' in 'hello')
print('A letra b não está na palavra hello: ', 'b' not in 'hello')

print('\nBuilt-in functions')
mystr = 'university'
print(mystr)
my_list_enumerate = list(enumerate(mystr))
print('Enumerando os caracteres de uma string: ', my_list_enumerate)
print('Tamanho da string em caracteres: ', len(mystr))

print('\nManeiras de escrever uma string com aspas')
print('''Tell me "What's your name?"''')
print('Tell me "What\'s your name?"')
print("Tell me 'What's your name?'")
print("Tell me \"What's your name?\"")

print("C:\\User\\user\\mydata.txt")
print("this line is having a new line \ncharacter")
print("this line is having a tab \t character")
print("ABC written in \x41\x42\x43 (HEX) representation")

print('\nMétodo de formatação - format() method')
default_order = '{} {} and {}'.format('Today', 'is', 'Sunday')
print("'{} {} and {}'.format('Today', 'is', 'Sunday'): ", default_order)

positional_order = '{1} {0} and {2}'.format('is', 'Today', 'Sunday')
print("'{1} {0} and {2}'.format('Today', 'is', 'Sunday'): ", positional_order)

keyword_order = '{t} {i} and {s}'.format(i = 'is', t = 'Today', s = 'Sunday')
print("'{t} {i} and {s}'.format(i = 'is', t = 'Today', s = 'Sunday'): ", keyword_order)

print('\nFormatação de números')
print('Required binary representation of {0} is {0:b}'.format(20)) #:b - representação em números binários
print('Exponent representation: {0:e}'.format(1566.345)) #:e - representação em notação científica
print('Onethird is: {0:.3f}'.format(1/3)) #:. - representação de número decimal ; 3f - número de casas decimais

print('\nMétodos de string')
print('gOOD moRNing tO alL'.lower()) #passar tudo para minúsculo
print('gOOD moRNing tO alL'.upper()) #passar tudo para maiúsculo
#os comandos find e replace são case sensitive
print('gOOD moRNing tO alL'.find('tO')) #mostrar a localização de uma palavra ou caracter.
print('gOOD moRNing tO alL'.find('to')) #se a palavra ou caracter não seja encontrado, retornará -1
print('gOOD moRNing tO alL'.replace('alL', 'everbody'))
print('gOOD moRNing tO alL'.replace('all', 'everbory'))