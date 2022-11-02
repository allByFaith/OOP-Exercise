# Create a child class Bus that will inherit all of the variables and
# methods of the Vehicle class and nothing else. Instantiate a Bus instance and 
# print out the attributes.

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
newVehicle = bus()
# newVehicle.changeMaxSpeed('500 MPH')
# newVehicle.changeColor('White')
print(f"Speed of Bus is {newVehicle.maxSpeed} and color is {newVehicle.color}")

