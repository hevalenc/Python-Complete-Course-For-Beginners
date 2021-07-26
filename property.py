print('Demonstrando o uso da propriedade')
class Temp_Celsius:
    def __init__(self, temperature = 0):
        print('Assigning temperature value')
        self._temperature = temperature

    def convert_to_farenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self):
        print('Getting temperature value')
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        print('Setting temperature value')
        self._temperature = value

    #property() is a built-in function, creates and returns a property object
    #property(fget = None, fset = None, fdel = None, doc = None)
    #property object has three methods, getter(), setter() and delete()
    temperature = property(get_temperature, set_temperature)

    #make empty property
    #temperature = property()
    #assign fget
    #temperature = temperature.getter(get_temperature)
    #assign fset
    #temperature = temperature.setter(set_temperature)

c = Temp_Celsius(5)
print(c.temperature)
c.temperature = 100
print(c.temperature)
print(c.__dict__['_temperature'])

print('\nDemonstrando o uso da propriedade como um decorador')
class Temp_Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def convert_to_farenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print('Getting temperature')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        print('Setting temperature')
        self._temperature = value

c = Temp_Celsius(5)
print(c.temperature)
c.temperature = 100
print(c.temperature)
