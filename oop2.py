class Animal:
    teeth = 42 #class variable.
    #attributes of the class(static).
    def __init__(self, c, l):#constructor -> special method called automatically when instanciating an object: attributes of the object
        self.colour = c  #instance variable
        self.legs = l
        pass

    def update_teeth(self, t):
        self.teeth = t

cat = Animal("Black", 4)
dog = Animal("Brown", 4)
cat.teeth = 2

cat.update_teeth(34)

# print(Animal.teeth)
# print(Animal.legs)
# print(Animal.colour)
print(cat.colour)
print(cat.legs)
print(cat.teeth)
print()
print(dog.colour)
print(dog.legs)
print(dog.teeth)
