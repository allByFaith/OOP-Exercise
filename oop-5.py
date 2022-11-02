# Use one of the built-in Python functions to print out the underlying object type 
# of the Bus object.

class Vehicle():
    def __init__(self, inMaxSpeed='200 MPH', inColor='Black'):
        self.maxSpeed = inMaxSpeed
        self.color = inColor

    def changeMaxSpeed(self, inMaxSpeed):
        self.maxSpeed = inMaxSpeed

    def changeColor(self, inColor):
        self.color = inColor

class bus(Vehicle):
    def __init_(self):
        pass


# newVehicle = Vehicle('300 MPH', 'Red')
newBus = bus()
# newVehicle.changeMaxSpeed('500 MPH')
# newVehicle.changeColor('White')
print(f"Speed of Bus is {newBus.maxSpeed} and color is {newBus.color}")
print("The type of newBus object is" + str(type(newBus)))

