print('Demonstração')
'''def make_decorated(func):
    def inner_function():
        print('I got decorated')
        func()
    return inner_function()

def simple_func():
    print('I am a simple function')

decor = make_decorated(simple_func)
decor()

def make_decorated(func):
    def inner_function():
        print('I got decorated')
        func()
    return inner_function()

@make_decorated
def simple_func():
    print('I am a simple function')

simple_func()'''

def my_smart_div(func):
    def inner_func(x, y):
        print('I am dividing ', x, ' and ', y)
        if y == 0:
            print('Ooops! Division by zero is illegal!!!!!')
            return

        return func(x, y)
    return inner_func

@my_smart_div
def go_divide(a, b): #devido ao decorador, esta função irá executar a função criada acima
    return a / b

print(go_divide(20, 2))
print(go_divide(20, 0))
