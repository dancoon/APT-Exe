#class(blueprint)
class Animal:
    #class attributes/state/data member/field of class
    def __init__(self):#constructor
        #instance attribute
        self.color = "Black"
        self.name = "Lulu"
    #method(function in class)
    def make_sound(self):
        print("{} making noise".format(self.name))
    
#instance(object)
cat = Animal()
print("{}  {}".format(cat.name, cat.color))
cat.make_sound()

#inheritance
class Pet(Animal):#pet is a child inheriting from Animal which is the parent
    pass

#instance
dog = Pet()
#override
dog.name = "Fery"
dog.color = "White"
print("{}  {}".format(dog.name, dog.color))