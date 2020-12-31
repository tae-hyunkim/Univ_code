from person import Person

class Manager(Person):
    def giveRaise(self,percent,bonus=.1):
        Person.giveRaise(self,percent + bonus)

if __name__ == "__main__":
    tom = Manager("Tom Jones", "mgr",50000)
    tom.giveRaise(.1)
    print(tom.last_name())
    print(tom)