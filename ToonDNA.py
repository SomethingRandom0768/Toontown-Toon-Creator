class ToonDNA():
    '''This entire class acts as data for the Toon. Toon.py will read from this and create a Toon'''
    def __init__(self, name='', gender='m', headType=0, torsoType=0, legsType=0, headColor=0, torsoColor=0, legsColor=0, glovesColor=0):
        self.name = name
        self.gender = gender 
        self.headType = headType
        self.torsoType =  torsoType
        self.legsType = legsType
        self.headColor = headColor
        self.torsoColor = torsoColor
        self.legsColor = legsColor
        self.glovesColor = glovesColor

    def __str__(self):
        dna_string  = f"""
        Name        : {self.name}
        Gender      : {self.gender}
        Head Type   : {self.headType}
        Torso Type  : {self.torsoType} 
        Legs Type   : {self.legsType}
        Head Color  : {self.headColor}
        Torso Color : {self.torsoColor}
        Legs Color  : {self.legsColor}
        Gloves Color: {self.glovesColor}
        """
        return dna_string
        
object = ToonDNA('Flippy', 'm', 1, 1, 1, 1, 1, 1, 1)