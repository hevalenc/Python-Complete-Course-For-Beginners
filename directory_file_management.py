import os

print(os.getcwd()) #returns the working directory
print(os.getcwdb()) #returns the working directory as a byte object (deprecated)

os.chdir('E:\\EngSoft') #use to cahnage directory
print(os.listdir())

#os.mkdir('Test') #used to make a new directory

#os.rename('Test', 'NewOne') #used to rename a directory

os.remove('test.txt') #used to remove a file
os.rmdir('NewOne') #used to remove a directory

os.chdir('E:\\EngSoft\\Cursos\\Udemy')
