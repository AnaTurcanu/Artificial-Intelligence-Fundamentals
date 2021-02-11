class Citizen(object):
    
    def __init__(self, hair, skin, eyes, headshape, height, language):
        self.hair = hair
        self.skin = skin
        self.eyes = eyes
        self.headshape = headshape
        self.height = height
        self.language = language

        
    def compliance_degree(self, person):
        complianceDegree = 0
        
        if(isinstance(person, Citizen)):
            if self.hair == person.hair:
                complianceDegree += 1

            if self.skin == person.skin:
                complianceDegree += 1
                
            if self.eyes == person.eyes:
                complianceDegree += 1
                
                
            if self.headshape == person.headshape:
                complianceDegree += 1
                
            if self.height == person.height:
                complianceDegree += 1
                
                
            if self.language == person.language:
                complianceDegree += 1
                
                
            return complianceDegree
        
        else:
            raise TypeError("Oops! Mistyped. Try again!")
