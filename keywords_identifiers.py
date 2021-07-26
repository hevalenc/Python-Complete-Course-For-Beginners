print('True or False')
print('5 é igual a 5: ',5 == 5)
print('5 é maior que 5: ',5 > 5)
print('None == 0: ',None == 0)
print('None == False: ', None == False)
print('None == []: ', None == [])
print('None == None: ', None == None)

print('\nFunção sem a condição "return" retorna None')
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print('Sem "return" na função: ', x)

def a_void_function():
    a = 1
    b = 2
    c = a + b
    return(c)
y = a_void_function()
print('Com "return" na função: ', y)

print('\nOperadores lógicos: AND, OR e NOT')
print('True and False: ', True and False)
print('True or False: ', True or False)
print('not False: ', not False)

print('\nImportando uma biblioteca com um apelido:')
import math as myMath
print('Cosseno de pi: ', myMath.cos(myMath.pi))

print('\nAção BREAK e CONTINUE')
print('Contador de 1 a 8, porém vai parar quando chegar em 5 por causa do break')
for i in range(1, 8):
    if i == 5:
        break
    print(i)

print('Contador de 1 a 8, porém não vai parar quando chegar em 5 por causa do continue')
for i in range(1, 8):
    if i == 5:
        continue
    print(i)

print('\nDeclaração de Classe')
class ExampleClass:
    def function1(parameters):
        print('function1() executing ...')
    def function2(parameters):
        print('function2() executing ...')

ob1 = ExampleClass()
ob1.function1()
ob1.function2()

print('\nAção "Pass"')
def function_name():
    pass

function_name()
print('A ação "pass" não executa nada')

print('\nFunções: IF, ELIF e ELSE')
num = 2
if num == 1:
    print('One')
elif num == 2:
    print('Two')
else:
    print('Something else')

print('\nFunções: TRY, RAISE, CATCH e FINALLY')
print('O bloco try lança uma tentativa que, quando ocorrer uma falha, lança o erro tratado')
try:
    x = 9
    raise ZeroDivisionError #a função raise levanta uma condição
except ZeroDivisionError:
    print('Division cannot be performed')
finally:
    print('Execution successfully')

print('\nLoop com FOR')
for i in range(1, 5):
    print(i)

for i in range(1, 10, 2): #imprimir de 2 em 2
    print(i)

print('\nFrom e Import')
import math #importa a biblioteca completa
from math import cos #importa uma função específica da biblioteca
print(cos(10))

print('\nVariável Global')
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar #função para acessar uma variável externa
    globvar = 5
def write2():
    globvar = 15 #não ocorrerá nenhuma alteração na variável externa, porque não foi invocada
read1()
write1()
read1()
write2()
read1()

print('\nFunção IN, verificar se um elemento pertence a uma lista ou array')
a = [1, 2, 3, 4]
print(a)
print('O número 4 pertence ao array a: ', 4 in a)
print('O número 44 pertence ao array a: ', 44 in a)

print('\nFunção IS')
print('True is True: ', True is True)

print('\nFunção lambda (anônima)')
a = lambda x: x * 2
for i in range(1, 6):
    print(i, a(i))

print('\nVariável que não é local')
def outer_function():
    a = 5
    def inner_function():
        nonlocal a #invocando a variável da função externa
        a = 10 #a variável a irá receber um novo valor
        print('Inner function: ', a)
    inner_function()
    print('Outer function: ', a)

outer_function()

print('\nLoop com WHILE')
i = 5
while(i > 0):
    print(i)
    i -= 1

print('\nFunção WITH')
with open('example.txt', 'w') as my_file: #abrir um arquivo se existir, caso não, será criado
    my_file.write('Hello World!!')

print('\nFunção YIELD (acumulador)')
def generator():
    for i in range(6):
        yield i * i #utilizado como acumulador

g = generator()
for i in g:
    print(i)

