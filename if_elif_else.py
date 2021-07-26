print('IF ... ELIF ... ELSE')
age = int(input('Please enter the age of the person: '))
if age < 5:
    print('Too young!')
elif age == 5:
    print('Kindergarten')
elif ((age > 5) and (age <= 17)):
    grade = age - 5
    print('Go to {} grade'.format(grade))
else:
    print('Go to college')

print('\nIF aninhado')
'''Neste programa, será inserido um número verificar se o número é positivo
ou negativo ou zero e mostrar uma mensagem apropriada'''
num = float(input('Enter the number: '))
if num > 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative mumber')