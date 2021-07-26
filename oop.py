print('Criando classe e objeto no Python')
class myBird:
    def __init__(self):
        print('... myBird class constructor is executing ...')

    def whatType(self):
        print('I am a Bird ...')

    def canSwim(self):
        print('I can swim ...')

class myParrot:
    species = 'bird'

    def __init__(self, name, age):
        print('... myParrot class constructor is executing ...')
        self.name = name
        self.age = age

    def canSing(self, thisSong):
        return '{} can sing {}.'.format(self.name, thisSong)

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')

    def whoisThis(self):
        print('I am a Penguin')

    def canRun(self):
        print('I can run faster')

print('\nInstanciando a classe myParrot')
mp1 = myParrot('MyParrot1', 10)
mp2 = myParrot('MyParrot2', 15)

print('\nAcessando os atributos da classe')
print('MP1 is a {}'.format(mp1.__class__.species))
print('MP2 is also a {}'.format(mp2.__class__.species))

print('\nAcessando as instâncias dos atributos')
print('{} is {} years of age'.format(mp1.name, mp1.age))
print('{} is {} years of age'.format(mp2.name, mp2.age))
print(mp1.canSing('Chirp'))

print('\nAcessando os atributos da classe filha (herança)')
pg1 = myPenguin()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()

print('\nEncapsulamento de dados')
class personalComputer:
    def __init__(self):
        self.maxComputerPrice = 20000

    def mySell(self):
        print('Selling price: {}'.format(self.maxComputerPrice))

    def setMaxComputerPrice(self, price):
        self.maxComputerPrice = price

pc = personalComputer()
pc.mySell()

pc.maxComputerPrice = 30000
pc.mySell()

pc.setMaxComputerPrice(40000)
pc.mySell()