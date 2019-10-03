class Person(object):
    def __init__(self, name, age):  # constructor
        self.name = name  # data members/ attributes
        self.age = age

    def get_person(self, ):  # member function
        return "<Person (%s, %s)>" % (self.name, self.age)

if __name__ == '__main__':
    p = Person("John", 32)  # p is an object of type Person
    print("Type of Object:", type(p), "Memory Address:", id(p))
    pass