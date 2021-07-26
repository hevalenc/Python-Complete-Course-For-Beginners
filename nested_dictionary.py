print('Declarando um dicionário aninhado')
people = {1:{'name':'John', 'age':'27', 'sex':'Male'},
          2:{'name':'Marie', 'age':'22', 'sex':'Female'}}

print(people)

print('\nAcessando os elementos do dicionário')
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

print('\nAdicionando elementos ao dicionário')
people[3] = {}
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people)

print('\nAdicionando um dicionário a um dicionário aninhado')
people[4] = {'name':'Peter', 'age':'29', 'sex':'Male', 'married':'Yes'}
print(people[4])
print(people)

print('\nRemovendo elementos de um dicionário')
print(people[3])
print(people[4])

del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])

print('\nRemovendo um dicionário de um dicionário aninhado')
del people[3], people[4]
print(people)

print('\nIterando em um dicionário aninhado')
print(people.items())

for p_id, p_info in people.items():
    print('\nPerson ID: ', p_id)

    for key in p_info:
        print(key + ': ', p_info[key])
