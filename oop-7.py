# Extend the Bus class to also contain an attribute of seating_capacity
# Add a method to calculate the price of a ticket.  This is calculated as 
# seating_capacity * 0.05 , with an extra 10% of the total of seating_capacity * 0.05 on top. 
# Instantiate a Bus instance and print the ticket price.

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
    print(f"The ticket price for {self.seating_capacity} seats is  £{self.ticketPrice}")

  def printINFO(self):
    print("Max Speed : ", self.maxSpeed, ", Color : ", self.color, ", Seat : ", self.seat)

getSeat = int(input("please Enter the number of Seat Capacity : "))
# newVehicle = Vehicle('300 MPH', 'Red')
newBus = Bus('200 MPH', 'Red', getSeat)

newBus.calculateTicketPrice()