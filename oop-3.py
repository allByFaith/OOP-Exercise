# Extend the Vehicle class to contain methods for the below: 
# Instantiate the class and call the two methods to update the attributes.
# Print the changes out:-
#   1) Change the value of max speed 
#   2) Change the car colour

class Vehicle():

    def __init__(self, inMaxSpeed='200 MPH', inColor='Black'):
        self.maxSpeed = inMaxSpeed
        self.color = inColor

    def changeMaxSpeed(self, inMaxSpeed):
        self.maxSpeed = inMaxSpeed

    def changeColor(self, inColor):
        self.color = inColor

class subClassVehicle(Vehicle):
        pass

# newVehicle = Vehicle('300 MPH', 'Red')
newVehicle = Vehicle()
newVehicle.changeMaxSpeed('500 MPH')
newVehicle.changeColor('White')
print(f"Speed of new vehicle is {newVehicle.maxSpeed} and color is {newVehicle.color}")

