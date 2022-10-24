class Tile:
    def __init__(self, name, cost, rent, housePrice, bought, owner):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.housePrice = housePrice
        self.bought = bought
        self.owner = owner

    def show(self):
        print(self.name, self.cost, self.rent)
    def getName(self):
        return(self.name)
    def getOwner(self):
        return(self.owner)
    def getCost(self):
        return(self.cost)
    def updateOwner(self, newOwner):
        self.owner = newOwner
    def getRent(self):
        return(self.rent)