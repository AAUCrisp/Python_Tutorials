

class Dog(object):
    
    #construtor
    def __init__(self, name, age):

        #attributes
        self.name = name
        self.age = age

    #methods
    def speak(self):
        print('Hello, my name is', self.name, 'and I am', self.age, 'years old')

    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age


tim = Dog('Balder', 8)
tim.set_age(9)
print(tim.get_age())