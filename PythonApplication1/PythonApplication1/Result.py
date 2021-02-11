from Citizen import Citizen
from TouristTypes import Tourist_Types

touristTypes = Tourist_Types()

print("What characteristics does the citizen have?")
ans = input("Hair (bald, brown, red, blue, green):\n")
hair = ans.lower()
ans = input("Skin (white, beige, red, blue, turqoise):\n")
skin = ans.lower()
ans = input("Eyes (black, blue, yellow, green):\n")
eyes = ans.lower()
ans = input("Headshape(square, round, triangular):\n")
headshape = ans.lower()
ans = input("Height(short, medium, tall):\n")
height = ans.lower()
ans = input("Language spoken(lunar, terrestric, mercuristic, intergalactic, ringlish): ")
language = ans.lower()

randomCitizen = Citizen(hair, skin, eyes, headshape, height, language)

bestComplianceValue = 0
bestComplianceType = None

for touristType in touristTypes.touristTypes:
    complianceDegree = touristType.compliance_degree(randomCitizen)
    if complianceDegree > bestComplianceValue:
        bestComplianceValue = complianceDegree
        bestComplianceType = touristType
    
print("The citizen is " + bestComplianceType.return_type())
