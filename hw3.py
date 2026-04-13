class animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def animalvoice(self):
        print("the animal is sound ")

class dog(animal):
    def __init__(self, color, age):
        super().__init__(color, age)
    def info(self):
        print(self.color , self.age)

class sheep(animal):
    def __init__(self, color, age):
        super().__init__(color, age)

    def info(self):
        print(self.color , self.age)

dog_obj = dog("black", 3)
sheep_obj = sheep("white", 5)

dog_obj.info()
sheep_obj.info()

