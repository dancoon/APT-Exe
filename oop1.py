#class(blueprint)
class Student:
    #class atttributes
    def __init__(self, name, regNo, year, course):
        #instance attributes
        self._name = name
        self.regNo = regNo
        self.year = year
        self.course = course
    #method
    def speak(self):
        print("My name is {}".format(self._name))
    #method
    def get_name(self):
        return self._name
    #method
    def set_name(self, new_name):
        self._name = new_name
    #special dunder methhod
    def __str__(self) -> str:
        pass
    #special method
    def __eq__(self, other) -> bool:
        pass

#instance(object)
student1 = Student("Dancun", "SCT221-0009/2022", 3, "BIT")
student1.set_name("Gathuru")
print("{}".format(student1.get_name()))
# student1.name = "Dancun"
# student1.regNo = "SCT221-0009/2022"
# student1.year = 3
# student1.course = "BIT"

# student2 = Student()
# student2.name = "Roy"
# student2.regNo = "RTE211-9292/2022"
# student2.year = 2
# student2.course = "Med"

# print(student1._name)
# print(student1.regNo)
# print(student1.year)
# print(student1.course)
# print()
# print(student2.name)
# print(student2.regNo)
# print(student2.year)
# print(student2.course)
# student1.speak()