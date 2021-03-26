

class Dog(object):
    


    #construtor
    def __init__(self, name, age):

        #attributes
        self.name = name
        self.age = age

    #methods
    def speak(self):
        print('Hello, my name is', self.name, 'and I am', self.age, 'years old')

    @classmethod
    def talk(cls):
        print("Wuf wuf")

    @staticmethod
    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age



class Cat(Dog): #inheritance from Dog class

    #construtor
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

jim = Dog('Spring', 9)
jim.talk()

tim = Cat('Snow', 6,'grey')
tim.speak()