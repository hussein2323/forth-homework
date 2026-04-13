class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greeting(self):
        print("good morning" , self.name)

name = input("Enter your name : ")
per = person(name , 23)
per.greeting()