print('Iterando uma lista')
our_list = [44, 77, 11, 33]
our_iter = iter(our_list)

print(our_list)
print('Primeiro número da lista: ', next(our_iter))
print('Segundo número da lista: ', next(our_iter))
print('Terceiro número da lista: ', our_iter.__next__())
print('Quarto número da lista: ', our_iter.__next__())

print('\nCriando um iterador customizado')

class Pow_of_Two:
    '''Class to implement an iterator of powers of two'''
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print(Pow_of_Two.__doc__)
a = Pow_of_Two(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print('\nCriando um iterador infinito')

class Infinite_Iter:
    '''Infinite iterator to return all odd numbers'''
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

print(Infinite_Iter.__doc__)
i = Infinite_Iter()
a = iter(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
