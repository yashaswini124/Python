from abc import ABC,abstractmethod

class vehicle(ABC):             #creating abstract class
    @abstractmethod
    def start_engine(self):     #methods in abstract class cannot be called
        pass


class car(vehicle):
    def __init__(self,name):
        self.name=name
    def start_engine(self):                      #method in abstract class must be implemented in child 
        print(f"{self.name} is starting")                 #class eventhough it is not called


class bike(vehicle):
    def __init__(self,name):
        self.name=name
    def start_engine(self):              #method in abstract class must be implemented in child class eventhough it is not called
        print(f"{self.name} is starting")


b=bike("Royal enfield")
c=car("audi")

print(c.name)
print(b.name)
b.start_engine()
c.start_engine()