class PartyAnimal:
    x = 0 
    
    def __init__(self):
        print("I am constructed")
        
    def party(self):
        self.x = self.x + 1    
        print("So far", self.x)
        
    def __del__(self):
        print("I am destructed", self.x)
        
        
an = PartyAnimal()
an.party()
an.party()
an = 42
print("An contains", an)
        
        

        
        
class PartyAnimal:
    x = 0 
    name = ""
    def __init__(self,nam):
        self.name = nam
        print(f"{self.name} is constructed")
        
    def party(self):
        self.x = self.x + 1    
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)