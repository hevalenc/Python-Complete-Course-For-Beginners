print('Bloco TRY/EXCEPT')
try:
    '''O código que pode lançar um erro será escrito aqui'''
    a = 'hi'
    b = int(a)
except:
    print('Exception caught!!')

print('\nCapturando um erro específico')
try:
    a = 5
    b = 0
    c = a / b
except ZeroDivisionError:
    print('Division by zero is not possible!!')

print('\nExcessões também podem ser levantados')
try:
    raise TypeError
except TypeError:
    print('TypeError Exception caught!!')

print('\nBloco TRY/FINALLY')
try:
    print('In try block')
except:
    print('In except block')
finally:
    print('In the finally block')