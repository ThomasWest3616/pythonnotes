class Person:
    name = ""

    def __init__(self, personName):
        self.name = personName

    def showName(self):
        print(self.name)


class Student(Person): 				# Student inherits from Person superclass
    studentClass = ""

    def __init__(self, studentName, studentClass):
        Person.__init__(self, studentName)		# superclass constructor
        self.studentClass = studentClass  		# Student class specific

    def getStudentClass(self):
        return self.studentClass


person1 = Person("Dave")
person1.showName()                  # Dave
student1 = Student("Mary", "Maths")
print(student1.getStudentClass())   # Maths
student1.showName()