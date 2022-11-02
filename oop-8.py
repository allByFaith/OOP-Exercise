# Research how to print a Bus object in a printable representation. 
# Hint: Look into the built-in repr() function. It should print 
# something like Max speed: 120, Colour: white, Seating capacity: 40.

class Vehicle:
  def __init__(self, inMaxSpeed, inColor):
    self.maxSpeed = inMaxSpeed
    self.color = inColor

  def changeMaxSpeed(self, inMaxSpeed):
    self.maxSpeed = inMaxSpeed

  def changeColor(self, inColor):
    self.color = inColor

  def printINFO(self):
    print(self.maxSpeed, self.color)

class Bus(Vehicle):
  def __init__(self, inMaxSpeed, inColor, inSeat):
    super().__init__(inMaxSpeed, inColor)
    self.seat = inSeat
    self.seating_capacity = inSeat
    self.ticketPrice = 0

  def getSeatingCapacity(self, inSeat):
    self.seating_capacity = inSeat

  def calculateTicketPrice(self):
    self.getSeatingCapacity(getSeat)
    self.ticketPrice = (self.seating_capacity * 0.05) * 1.1
    print(f"The ticket price for {self.seating_capacity} seats is £{self.ticketPrice}")

  def __repr__(self):
    return repr('MAX Speed : ' + self.maxSpeed + ', Color : ' + self.color + ', Seating Capacity : ' + self.seating_capacity)

  def printINFO(self):
    print("Max Speed : ", self.maxSpeed, ", Color : ", self.color, ", Seat : ", self.seat)

getSeat = int(input("please Enter the number of Seat Capacity : "))
# newVehicle = Vehicle('300 MPH', 'Red')
newBus = Bus('200 MPH', 'Red', getSeat)

newBus.calculateTicketPrice()

# Use repr() to print the bus object
printNewBusObj = repr(Bus('200 MPH', 'Red', str(getSeat)))
print(printNewBusObj)
