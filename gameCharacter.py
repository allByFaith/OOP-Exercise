class basePrototype():

    def __init__(self, model, type, function, iWeapon):
        self.model = model
        self.type = type
        self.function = function
        self.iWeapon = iWeapon
        self.uniqueAccessCode = 'normal01'

    def get_DefaultInfo(self):
        print(self.uniqueAccessCode)

    def printDetail(self):
        print(self.model)
        print(self.type)
        print(self.function)
        print(self.iWeapon)
        self.get_DefaultInfo()

    # for Encapsulation
    def accessCode(self, inAccessCode):
        self.uniqueAccessCode = inAccessCode
        print("my code is --> " + inAccessCode)
    
    # Polymorphism
    def weapon(self, inWeapon):
        self.weapon = inWeapon


class baseWeapon:
      pass

class advancePrototype(basePrototype):

    def __init__(self, model, type, function, iWeapon):
        super().__init__(model, type, function, iWeapon)
        self.model = model
        self.type = type
        self.function = function
        self.iWeapon = iWeapon
        self.uniqueAccessCode ='fight02'
        self.energyLevel = 'middle energy leve'
        self.maxFightDuration = 'max duration for 3h'
    

        def weapon(self, inWeapon, inPower):
            self.weapon = inWeapon
            self.power = inPower
        
    def get_DefaultInfo(self):
        print(self.uniqueAccessCode)
        print(self.energyLevel)
        print(self.maxFightDuration)

        def printDetail(self):
            print(self.model)
            print(self.type)
            print(self.function)
            print(self.iWeapon)
            self.get_DefaultInfo()
        
Terminator01 = basePrototype('Terminator', 'Type One', 'Fight Mode', 'Sword' )
Terminator02 = advancePrototype('Terminator', 'Type Two', 'Advance Fight Mode', 'Electric Gun')

Terminator01.printDetail()
print("\n")
Terminator02.printDetail()
