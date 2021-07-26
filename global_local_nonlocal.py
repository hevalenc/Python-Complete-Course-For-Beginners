print('Alterando a variável Global com uma função')
x = 'global'

def function1():
    global x
    y = 'Local'
    x = x * 2
    print('x: ', x)
    print('y: ', y)

print('Global x: ', x)
function1()
print('Global x: ', x) #a função alterou a variável x

print('\nGlobal e Local sem alterações')
a = 5

def function2():
    a = 10
    print('Local a: ', a)

print('Global a: ', a)
function2()
print('Global a: ', a)

print('\nCriando e usando uma variável NonLocal')
def outer():
    x = 'Local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)

outer()