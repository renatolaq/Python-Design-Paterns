from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class Personal(Section):
    def describe(self):
        print("Personal Section")

class Album(Section):
    def describe(self):
        print("Album Section")

class Patent(Section):
    def describe(self):
        print("Patent Section")

class Publication(Section):
    def describe(self):
        print("Publication Section")

##factory defined
class DescribeFactory(object):
    def make_describe(self, object_type):
        return eval(object_type)().describe()

if __name__ == '__main__':
    ff = DescribeFactory()
    describe = input("Which Profile you'd like Describe? [Personal, Album, Patent, Publication]?")
    ff.make_describe(describe)
