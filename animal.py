class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        print("The dog is running ")

class Bird(Animal):
    def move(self):
        print("The bird is flying in the sky.")

class Fish(Animal):
    def move(self):
        print(" The fish is swimming in the water.")

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  
