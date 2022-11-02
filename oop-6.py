# Use one of the built-in Python functions to print out 
# if the Bus object is an instance of Vehicle
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

result = isinstance(newBus, Vehicle)
if result:
    print("Yes, the newBus is an instance of Vehicle")
else:
    print("No, the newBus is an instance of Vehicle")


