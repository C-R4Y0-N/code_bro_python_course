class Duck:
    def walk(self):
        print("This duck is walking")
    
    def talk(self):
        print("This duck is qwacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
        
    def talk(self):
        print("This chicken is clucking")
    
class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)