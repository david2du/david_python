#from IPython.core.interactiveshell import Interactiveshell
#Interactiveshell.ast_node_interactivity = "all"


class people:

    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        #print("%s 说: 我 %d 岁。" %(self.name,self.age))
        print(f"{self.name} says: I am {self.age} years old")


p = people('runoob', 10, 30)
p.speak()
