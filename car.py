class Car:
    make = None
    model = None
    year = None
    color = None
    
    wheels = 4 #Class variable
    
    def __init__(self,make,model,year,color):
        self.make = make  #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable
    
    def drive(self):
        print("This "+self.model+ "  is driving")
    
    def stop(self):
        print("This "+self.model+" is stopped")