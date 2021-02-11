from Citizen import Citizen

class Tourist_Types:
    def __init__(self):
        self.touristTypes = [Loonie(), Earthie(), Mercurian(), Plutonian(), Jupitarian()]

class Loonie(Citizen):
    def __init__(self):
        super().__init__("bald","white", "black","square","short","lunar")       
    def return_type(self):
        return "Loonie"
        
class Earthie(Citizen):
    def __init__(self):
        super().__init__("brown", "beige", "blue", "round", "medium", "terrestric")
    def return_type(self):
        return "Earthie"
        
class Mercurian(Citizen):
    def __init__(self):
        super().__init__("red", "brown", "yellow", "round", "short", "mercuristic")      
    def return_type(self):
        return "Mercurian"
        
class Plutonian(Citizen):
    def __init__(self):
        super().__init__("blue", "blue", "green", "triangular", "tall", "intergalactic")       
    def return_type(self):
        return "Plutonian"
        
class Jupitarian(Citizen):
    def __init__(self):
        super().__init__("green", "turqoise", "green", "square", "medium", "ringlish")       
    def return_type(self):
        return "Jupitarian"
     
     

