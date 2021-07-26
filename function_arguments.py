print('Funções com argumentos')

def findMax(a, b):
    if a > b:
        return a
    else:
        return b

print('O maior número entre 10 e 20 é: ', findMax(10, 20))

print('\nFunção com parâmetro padrão')

def hello(name, msg = ', how are you?'):
    print('Hello ', name, msg)

hello('Heitor', ', have a nice day')
hello('Heitor') #na falta do segundo argumento passado pelo usuário, será usado o argumento padrão da função

print('\nFunção com argumentos arbitrários')

def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print('Soma de todos os inteiros de 1 a 5 é: ', sumAll(1, 2, 3, 4, 5))

print('\nFunção com parâmetro padrão')

def defaultArg(a = 100, b = 200, c = 300):
    print('a = {}, b = {}, c = {} ... '.format(a, b, c))

defaultArg(10, 20, 30)
defaultArg(20, 30)
defaultArg()
defaultArg(b = 222, c = 333, a = 111)
defaultArg(b = 222, a = 111)
