print('Herança em Python')
'''Criando um classe e um objeto em Python'''

class myBird:
    def __init__(self):
        print('... myBird class constructor is executing ...')

    def whatType(self):
        print('I am a Bird ...')

    def canSwim(self):
        print('I can swim ...')

'''A classe myPenguin herdando os atributos da classe myBird'''

class myPenguin(myBird):
    def __init__(self):
        super().__init__()
        print('... myPenguin class constructor is executing ...')

    def whoisThis(self):
        print('I am a Penguin ...')

    def canRun(self):
        print('I can run faster ...')

print('\nAcessando os atributos da classe filha (herança)')
pg1 = myPenguin()
pg1.whatType()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()

print('\nPoliformismo')

class myParrot:
    def canFly(self):
        print('Parrot can fly ...')

    def canSwin(self):
        print('Parrot can´t swim ...')

class myPenguin:
    def canFly(self):
        print('Penguin can´t fly ...')

    def canSwin(self):
        print('Penguin can swim ...')

'''Interface comum'''
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwin()

'''instanciando os objetos'''
bird_parrot = myParrot()
bird_penguin = myPenguin()

'''passando os objetos'''
flying_bird_test(bird_parrot)
print()
flying_bird_test(bird_penguin)
