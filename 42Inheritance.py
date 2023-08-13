class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This animal can run")
class Hawk(Animal):
    def fly(self):
        print("This animal can fly")

class Fish(Animal):
    def swim(self):
        print("this animal can swim")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.slumber()
rabbit.run()
hawk.fly()
fish.swim()