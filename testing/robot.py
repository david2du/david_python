import datetime

class Golem:
    
    def __init__(self, name = None):
        self.name = name
        self.build_year = datetime.date.today().year

    def say_hi(self):
        print('Hi!')

class Running_Golem(Golem):
    
    def run(self):
        print("Can't you see? I'm running!")

rg = Running_Golem("Clay")

rg.run
rg.run()
rg.name
rg.build_year
rg.say_hi()