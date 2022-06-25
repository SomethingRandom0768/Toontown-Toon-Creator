from toon.Toon import *
from toon.npctoon.NPCToonList import *
from toon.npctoon.NPCToonDNA import *

# Just some conversions to reduce headache
NPCToonHeadConversions = {
    # Cats
    'cls': ('ca', 'ls'),
    'cll': ('ca', 'll'),
    'css': ('ca', 'ss'),
    'csl': ('ca', 'sl'),

    # Ducks
    'fls': ('du', 'ls'),
    'fll': ('du', 'll'),
    'fss': ('du', 'ss'),
    'fsl': ('du', 'sl'),

    # Monkeys
    'pls': ('mo', 'ls'),
    'pll': ('mo', 'll'),
    'pss': ('mo', 'ss'),
    'psl': ('mo', 'sl'),

    # Mice
    'mls' : ('mi', 'ls'),
    'mss' : ('mi', 'ss'),

    # Pigs
    'sls': ('p', 'ls'),
    'sll': ('p', 'll'),
    'sss': ('p', 'ss'),
    'ssl': ('p', 'sl'),

}


class NPCToon(Toon):
    def __init__(self):
        '''A child of Toon object with a few capabilities for generating NPCToons from Toontown Online'''
        self.NPCToon = super().__init__()

    def updateToonBody(self):
        '''Updates the Toon based on the new body'''
        self.toonActor.delete()
        self.generateActor()

    def convertNPCToToon(self, NPCID):
        '''Converts the NPC's dna string to a Toon Creator compatible Toon
        Returns Toon Creator compatible Toon tuple'''
        colorKeys = list(colorsList.keys())
        #print(NPCToonDict[NPCID])
        npcName = NPCToonDict[NPCID][1]
        npcHeadType = NPCToonDict[NPCID][2][0]
        npcTorsoType = NPCToonDict[NPCID][2][1]
        npcLegType = NPCToonDict[NPCID][2][2]
        npcGender = NPCToonDict[NPCID][2][3]
        npcArmColor = NPCToonDict[NPCID][2][4]
        npcGloveColor = NPCToonDict[NPCID][2][5]
        npcLegColor = NPCToonDict[NPCID][2][6]
        npcHeadColor = NPCToonDict[NPCID][2][7]
        npcTopTexture = NPCToonDict[NPCID][2][8]
        npcTopTextureColor = NPCToonDict[NPCID][2][9]
        npcSleeveTexture  = NPCToonDict[NPCID][2][10]
        npcSleeveTextureColor = NPCToonDict[NPCID][2][11]
        npcBottomTexture = NPCToonDict[NPCID][2][12]
        npcBottomTextureColor = NPCToonDict[NPCID][2][13]
        # print("Toon Name: " + npcName)
        # print("Toon Head Type: " + npcHeadType )
        # print("Toon Torso Type: " + npcTorsoType )
        # print("Toon Leg Type: " + npcLegType )
        # print("Toon Gender: " + npcGender )
        # print("Toon Arm Color: " + str(npcArmColor) )
        # print("Toon Glove Color: " + str(npcGloveColor) )
        # print("Toon Leg Color: " + str(npcLegColor) )
        # print("Toon Head Color: " + str(npcHeadColor) )
        # print("Toon Top Texture: " + str(npcTopTexture) )
        # print("Toon Bottom Texture : " + str(npcBottomTexture) )
        convertedSpecies = None
        convertedHeadType = None
        convertedEyelashes = None
        convertedShirt = None
        convertedShorts = None
        convertedSkirt = None

        # Head Type
        if npcHeadType in list( NPCToonHeadConversions.keys() ):
            convertedSpecies = NPCToonHeadConversions[npcHeadType][0]
            convertedHeadType = NPCToonHeadConversions[npcHeadType][1]
        else:
            convertedSpecies = npcHeadType[0]
            convertedHeadType = npcHeadType[1:3]
        
        # Eyelashes
        if npcGender == 'm':
            convertedEyelashes = False
        else:
            convertedEyelashes = True

        # Colors
        convertedHeadColor = colorKeys[npcHeadColor]
        convertedArmColor = colorKeys[npcArmColor]
        convertedGloveColor = colorKeys[npcGloveColor]
        convertedLegColor = colorKeys[npcLegColor]
        convertedShirtColor = colorKeys[npcTopTextureColor]
        convertedBottomColor = colorKeys[npcBottomTextureColor]

        shirtKeys = list ( shirt_dict.keys() )
        shortKeys = list (short_dict.keys() )
        skirtKeys = list (skirt_dict.keys() )
        shirtValues = list( shirt_dict.values() )
        shortValues = list( short_dict.values() )
        skirtValues = list( skirt_dict.values() )

        shirtToGetIndexOf = Shirts[npcTopTexture]
        sleeveToGetIndexOf = Sleeves[npcSleeveTexture]
        shortToGetIndexOf = BoyShorts[npcBottomTexture]
        skirtToGetIndexOf = GirlBottoms[npcBottomTexture]
        shirtIndex = 0
        shortIndex = 0
        skirtIndex = 0

        # Shirts
        for key in shirtKeys:
            if shirtToGetIndexOf in shirt_dict[key]:
                convertedShirt = shirtKeys[shirtIndex]
            else:
                shirtIndex += 1

        if npcTorsoType[-1] == 's':
            # Shorts
            for key in shortKeys:
                if shortToGetIndexOf in short_dict[key]:
                    convertedShorts = shortKeys[shortIndex]
                else:
                    shortIndex += 1
        else:
            # Skirts
            for key in skirtKeys:
                if skirtToGetIndexOf in skirt_dict[key]:
                    convertedSkirt = skirtKeys[skirtIndex]
                else:
                    skirtIndex += 1

     #   print(npcName, convertedSpecies, convertedHeadType, convertedEyelashes, npcTorsoType, npcLegType, convertedHeadColor, convertedArmColor, convertedGloveColor, convertedLegColor, convertedShirt )
     
        return (convertedSpecies, convertedHeadType, convertedEyelashes, npcTorsoType, npcLegType, convertedHeadColor, convertedArmColor, convertedLegColor, convertedShirt, convertedShirtColor, convertedShorts, convertedSkirt, convertedBottomColor) 

    def updateHeadColorData(self, colorToSet):
        '''This function updates the data for Toon's head color. It circumvents an issue in which the program will
        attempt to color a non-existent head and crash the program
        '''
        self.headColor = colorToSet

    def updateNPCToonInfo(self, species, headType, eyelashes, torsoType, legSize, headColor, armColor, legColor, shirtTexture, shirtTextureColor, shortTexture, skirtTexture, bottomColor):
        '''Updates the Toon's DNA with the arguments'''

        self.updateSpecies(species)
        self.updateHead(species, headType, eyelashes)
        self.updateTorso(torsoType)
        self.updateLegs(legSize)
        
        self.updateHeadColorData(headColor)
        self.updateArmsColor(armColor)
        self.updateLegsColor(legColor)
        
        self.setShirtTexture(shirtTexture)
        self.setShirtColor(shirtTextureColor)
        self.setShortTexture(shortTexture)
        self.setSkirtTexture(skirtTexture)
        self.setBottomColor(bottomColor)

