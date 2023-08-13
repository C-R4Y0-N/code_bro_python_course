from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
        
    def stop(self):
        print("This car is stop")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    
    def stop(self):
        print("This motorcycle is stop")



#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()