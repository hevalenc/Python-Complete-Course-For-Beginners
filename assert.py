print('Assert sem mensagem de erro')
def avg(marks):
    assert len(marks) != 0
    return sum(marks) / len(marks)

mark1 = [11, 22, 33]
print(mark1)
print('Average of mark1: ', avg(mark1))

#mark1 = [] #esta condição gera erro
#print('Average of mark1: ', avg(mark1))

print('\nAssert com mensagem de erro')
def avg(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks) / len(marks)

mark2 = [55, 88, 78, 90, 79]
print(mark2)
print('Average of mark2: ', avg(mark2))

mark2 = [] #esta condição gera erro, porém tem uma mensagem para tratamento
print('Average of mark2: ', avg(mark2))
