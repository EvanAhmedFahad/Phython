class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")


person=Person("fahad khan")
print(person.name)
person.talk()
per= Person("rifat khan")
per.talk()