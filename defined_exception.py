class VotersElligibility(Exception):
    def __init__(self):
        super()

try:
    age = 12
    print('Age is ' + str(age))
    if age < 18:
        raise VotersElligibility
except VotersElligibility:
    print('Age is less than 18!!!')
else:
    print('Age is greater than or equal to 18!!!')
finally:
    print('End of program')

print()
try:
    age = 21
    print('Age is ' + str(age))
    if age < 18:
        raise VotersElligibility
except VotersElligibility:
    print('Age is less than 18!!!')
else:
    print('Age is greater than or equal to 18!!!')
finally:
    print('End of program')