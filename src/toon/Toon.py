from direct.actor.Actor import Actor
from panda3d.core import *
from .ToonHead import *
from .ToonDNA import *


toonTorsoTypes = {"ss": 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam',  # short shorts
                  "ms": 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam',  # medium shorts
                  "ls": 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam',  # long shorts
                  # short dress (Should be given this one and below if species is girl)
                  "sd": 'phase_3/models/char/tt_a_chr_dgs_skirt_torso_1000.bam',
                  "md": 'phase_3/models/char/tt_a_chr_dgm_skirt_torso_1000.bam',  # medium dress
                  "ld": 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_1000.bam',  # long dress
                  }

toonLegTypes = {"s": 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam',  # small
                "m": 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam',  # medium
                "l": 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam'  # long
                }


class Toon:
    '''Toon Actor, contains the body and the legs, but attaches on the head retrieved from ToonHead'''

    def __init__(self, species='r', headType='ss', hasEyelashes=False, torsoType='md', legSize='l', headColor='White', armColor='White', gloveColor='White', legColor='White', shirtTexture=None, shortTexture=None, skirtTexture=None, shirtColor='White', bottomColor='White', backpack=None, glasses=None, shoes_type=None, longBootTexture=None, shortBootTexture=None, shoes_texture=None, animation_type='Neutral', is60FPS=False, wearsShoes=False):
        # DNA based stuff
        self.toonActor = None
        self.species = species
        self.headtype = headType
        self.torsoType = torsoType
        self.legSize = legSize
        self.headColor = headColor
        self.armColor = armColor
        self.gloveColor = gloveColor
        self.legColor = legColor
        self.eyelashes = hasEyelashes

        # Clothing based stuff
        self.shirtTexture = shirtTexture
        self.shirtColor = shirtColor
        self.shortTexture = shortTexture
        self.skirtTexture = skirtTexture
        self.bottomColor = bottomColor

        # Accessory based stuff
        self.backpackType = backpack
        self.backpack_model = None
        self.hat_type = None
        self.hat_model = None
        # Also counts for mask since they're both the same.
        self.glassesType = glasses
        self.glasses_model = None

        self.shoeType = shoes_type
        self.shortBootTexture = shortBootTexture
        self.longBootTexture = longBootTexture
        self.shoeTexture = shoes_texture

        self.animationType = animation_type
        self.smoothEnabled = is60FPS
        self.wearsShoes = wearsShoes

        self.head = ToonHead(self.species, self.headtype, self.eyelashes)
        self.torso = toonTorsoTypes[self.torsoType]
        self.legs = toonLegTypes[self.legSize]

        self.generateActor()

    def generateActor(self):
        '''Updates Toon's pieces, and then creates an actor.'''

        if self.toonActor:
            self.toonActor = None

        self.toonActor = Actor(

            {
                'head': self.returnHead(),
                'torso': self.returnTorso(),
                'legs': self.returnLegs()
            },

            {
                'head': self.returnHeadAnim(self.headtype),
                'torso': self.returnTorsoAnim(self.torsoType),
                'legs':  self.returnLegsAnim(self.legSize)
            })

        self.toonActor.attach('head', 'torso', 'def_head')
        self.toonActor.attach('torso', 'legs', 'joint_hips')

        self.toonActor.reparentTo(render)
        self.toonActor.setPos(2, 35, 0)
        self.toonActor.setHpr(180, 0, 0)

        if self.smoothEnabled:
            self.toonActor.setBlend(frameBlend=True)
        else:
            pass

        self.toonActor.loop(self.animationType)

        # Add the coloring to the Toon based on its color variables.
        self.updateHeadColor(self.headColor)
        self.updateArmsColor(self.armColor)
        self.updateLegsColor(self.legColor)
        self.updateGloveColor(self.gloveColor)

        # Clothing related stuff
        if self.shirtTexture:
            self.setShirtTexture(self.shirtTexture)
        else:
            pass

        if self.torsoType:
            self.setShortTexture(self.shortTexture)
            self.setSkirtTexture(self.skirtTexture)
        else:
            pass

        if self.shirtColor:
            self.setShirtColor(self.shirtColor)
        else:
            pass

        if self.bottomColor:
            self.setBottomColor(self.bottomColor)
        else:
            pass

        # Accessory related stuff
        if self.backpackType:
            self.attachBackpack(self.backpackType)
        else:
            pass

        if self.glassesType:
            self.attachGlasses(self.glassesType)
        else:
            pass

        # Regardless of what happens, we hide the shoe pieces
        self.toonActor.find('**/*boots_short').hide()
        self.toonActor.find('**/*boots_long').hide()
        self.toonActor.find('**/*shoes').hide()

        if self.wearsShoes:
            self.attachShoes(self.shoeType)
        else:
            pass

        if self.shoeTexture:
            self.applyShoeTexture(self.shoeTexture)
        else:
            pass

        if self.shortBootTexture:
            self.applyShortBootTexture(self.shortBootTexture)
        else:
            pass

        if self.longBootTexture:
            self.applyLongBootTexture(self.longBootTexture)
        else:
            pass

        # Add shadow
        self.shadow = loader.loadModel("phase_3/models/props/drop_shadow.bam")
        self.shadow.reparentTo(self.toonActor.find('**/joint_shadow'))

        self.shadow.setSx(0.5)
        self.shadow.setSy(0.5)

# DNA Related functions

    def updateSpecies(self, species_to_change_to):
        self.species = species_to_change_to
        self.head = ToonHead(self.species, self.headtype, self.eyelashes)

    def updateHead(self, species, headType, hasEyelashes):
        '''Updates the head type.'''
        self.headtype = headType
        self.species = species
        self.eyelashes = hasEyelashes
        self.head = ToonHead(species, headType, hasEyelashes)

    def updateHeadColor(self, color_to_set):
        '''Updates the Toon's head color'''
        self.headColor = color_to_set

        if self.species == 'd':
            self.toonActor.find(
                '**/head').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front').setColor(colorsList[self.headColor])
        # Gotta account for Deers only having one head type.
        elif self.species == 'de':
            self.toonActor.find(
                '**/*ears-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-short').setColor(colorsList[self.headColor])
        elif self.species == 'du':  # Gotta account for ducks not having ears
            self.toonActor.find(
                '**/*head-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-long').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-long').setColor(colorsList[self.headColor])
        elif self.species == 'ri':  # Riggy only has one head type.
            self.toonActor.find(
                '**/*ears').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front').setColor(colorsList[self.headColor])
        elif self.species == 'mo':  # Monkeys can't get their ears colored.
            self.toonActor.find(
                '**/*head-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-long').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-long').setColor(colorsList[self.headColor])
        else:
            self.toonActor.find(
                '**/*ears-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-short').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-long').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*ears-long').setColor(colorsList[self.headColor])
            self.toonActor.find(
                '**/*head-front-long').setColor(colorsList[self.headColor])

    def updateTorso(self, torsoType):
        '''Updates the torso type'''
        self.torso = toonTorsoTypes[torsoType]
        self.torsoType = torsoType

    def updateArmsColor(self, color_to_set):
        self.armColor = color_to_set
        self.toonActor.find('**/arms').setColor(colorsList[self.armColor])
        self.toonActor.find('**/neck').setColor(colorsList[self.armColor])

    def updateLegs(self, legs_type):
        '''Updates the leg type'''
        self.legSize = legs_type
        self.legs = toonLegTypes[legs_type]

    def updateLegsColor(self, color_to_set):
        '''Update the Toon leg colors'''
        self.legColor = color_to_set
        self.toonActor.find('**/legs').setColor(colorsList[self.legColor])
        self.toonActor.find('**/feet').setColor(colorsList[self.legColor])

    def updateGloveColor(self, color_to_set):
        '''Colors the Toon's gloves'''
        self.gloveColor = color_to_set
        self.toonActor.find('**/hands').setColor(colorsList[self.gloveColor])

    def returnHead(self):
        '''Just returns the head'''
        return self.head.head_model

    def returnHeadAnim(self, headType):
        headSizeIndex = headType[0]

        if self.torsoType[1] == 's':
            if headSizeIndex == 'l':
                return long_head_shorts_anim_dict
            elif headSizeIndex == 'm':
                return medium_head_shorts_anim_dict
            elif headSizeIndex == 's':
                return short_head_shorts_anim_dict
        else:
            return medium_head_skirt_anim_dict

    def returnTorso(self):
        '''Returns the torso'''
        return self.torso

    def returnTorsoAnim(self, torsoType):

        if torsoType == 'ss':
            return short_torso_shorts_anim_dict
        elif torsoType == 'ms':
            return medium_torso_shorts_anim_dict
        elif torsoType == 'ls':
            return long_torso_anim_shorts_dict
        elif torsoType == 'sd':
            return short_torso_skirt_anim_dict
        elif torsoType == 'md':
            return medium_torso_skirt_anim_dict
        elif torsoType == 'ld':
            return long_torso_skirt_anim_dict
        else:
            raise "Strange torso type"

    def returnLegs(self):
        '''Returns the legs'''
        return self.legs

    def returnLegsAnim(self, legsType):
        legSizeIndex = legsType

        if legSizeIndex == 'l':
            return long_legs_anim_dict
        elif legSizeIndex == 'm':
            return medium_legs_anim_dict
        elif legSizeIndex == 's':
            return short_legs_anim_dict
        else:
            raise "Strange Legs type"

 # Clothing related functions
    def setShirtTexture(self, shirt):
        '''Sets the Toon's texture based on the shirt variable (the key in the ToonDNA dictionary)'''

        try:
            shirtTexturePath = shirt_dict[shirt][0]
            shirtTexture = loader.loadTexture(shirtTexturePath)
            self.toonActor.find('**/torso-top').setTexture(shirtTexture, 1)

            if len(shirt_dict[shirt]) == 2:
                sleeveTexturePath = shirt_dict[shirt][1]
                sleeveTexture = loader.loadTexture(sleeveTexturePath)
                self.toonActor.find('**/sleeves').setTexture(sleeveTexture, 1)
            elif len(shirt_dict[shirt]) == 3:
                sleeveTexturePath = shirt_dict[shirt][1]
                sleeveRGBTexturePath = shirt_dict[shirt][2]
                sleeveTexture = loader.loadTexture(sleeveTexturePath, sleeveRGBTexturePath)
                self.toonActor.find('**/sleeves').setTexture(sleeveTexture, 1)
                pass
        except:
            pass
            # If nothing happens when changing shirts, it's potentially misspelled, not in ToonDNA, or the correct dictionary.

    def setShortTexture(self, short):
        '''Sets the Toon's short texture. Used when generating the Toon'''
        if self.torsoType[-1] == 's':
            try:
                shortTexturePath = short_dict[short]
                shortTexture = loader.loadTexture(shortTexturePath)
                self.toonActor.find('**/torso-bot').setTexture(shortTexture, 1)
            except:
                pass
                # If nothing happens when changing shorts, it's potentially misspelled, not in ToonDNA, or the correct dictionary.
        else:
            pass

    def setSkirtTexture(self, skirt):
        '''Sets the Toon's short texture. Used when generating the Toon and through Options Menu'''
        if self.torsoType[-1] == 'd':
            try:
                if len( skirt_dict[skirt] ) == 1:
                    skirtTexturePath = skirt_dict[skirt][0]
                    skirtTexture = loader.loadTexture(skirtTexturePath)
                    self.toonActor.find('**/torso-bot').setTexture(skirtTexture, 1)
                elif len( skirt_dict[skirt] ) == 2:
                    skirtTexturePath = skirt_dict[skirt][0]
                    rgbTexturePath = skirt_dict[skirt][1]
                    skirtTexture = loader.loadTexture(skirtTexturePath, rgbTexturePath)
                    self.toonActor.find('**/torso-bot').setTexture(skirtTexture, 1)
            except:
                pass
                # If nothing happens when changing skirts, it's potentially misspelled, not in ToonDNA, or the correct dictionary.
        else:
            pass

    def setShirtColor(self, shirtColor):
        '''Colors the Toon's current shirt'''
        self.toonActor.find(
            '**/torso-top').setColorScale(colorsList[shirtColor])
        self.toonActor.find(
            '**/sleeves').setColorScale(colorsList[shirtColor])

    def setBottomColor(self, bottomColor):
        '''Colors the Toon's current bottom'''
        if self.torsoType == 'ls':
            self.toonActor.find(
                '**/torso-bot').setColor(colorsList[bottomColor])
        else:
            self.toonActor.find(
                '**/torso-bot').setColorScale(colorsList[bottomColor])

 # Accessory related functions
    def attachBackpack(self, backpack_to_attach):
        '''Attaches a backpack based on the type of backpack.'''

        # So if we already had a model before changing it, remove its node.
        if self.backpack_model:
            self.backpack_model.removeNode()
        else:
            pass

        # Doing this because some backpacks require a model and texture while others just need the bam file.
        if len(backpack_dict[backpack_to_attach]) == 5:
            self.backpack_model = loader.loadModel(
                backpack_dict[backpack_to_attach][0])
            self.backpack_model.reparentTo(
                self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][4])

            if backpack_to_attach == 'Pirate Sword':
                self.backpack_model.setHpr(180, 15, 30)
            elif backpack_to_attach == "Santa's Bag" or backpack_to_attach == 'Trash Lid (SPOILERS!)':
                self.backpack_model.setHpr(180, 0, 0)
            elif backpack_to_attach == 'Toonosaur Tail' or 'Shark Fin' == backpack_to_attach:
                self.backpack_model.setHpr(180, 20, 0)
            elif 'Bowtie' in backpack_to_attach:
                self.backpack_model.setHpr(180, -50, 0)
            elif backpack_to_attach == 'Oil Pale Pack':
                self.backpack_model.setHpr(180, 0, 0)
            else:
                self.backpack_model.setHpr(180, 0, 0)

            if self.torsoType[0] == 's':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][1])
            elif self.torsoType[0] == 'm':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][2])
            elif self.torsoType[0] == 'l':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][3])
            else:
                print("What kind of torso are you rockin?")

        # This is when we need to retexture something like the ToonFest backpacks, or scarves.
        elif len(backpack_dict[backpack_to_attach]) == 6:
            self.backpack_model = loader.loadModel(
                backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture(backpack_dict[backpack_to_attach][1])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(
                self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][5])
            self.backpack_model.setHpr(180, 0, 0)

            if self.torsoType[0] == 's':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][2])
            elif self.torsoType[0] == 'm':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][3])
            elif self.torsoType[0] == 'l':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][4])
            else:
                print("What kind of torso are you rockin?")

        # This is when we need to retexture something like the Jellybean Jar reskins, which have an RGB file.
        elif len(backpack_dict[backpack_to_attach]) == 7:
            self.backpack_model = loader.loadModel(
                backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture(
                texturePath=backpack_dict[backpack_to_attach][1], alphaPath=backpack_dict[backpack_to_attach][2])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(
                self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][6])
            self.backpack_model.setHpr(180, 0, 0)

            if self.torsoType[0] == 's':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][3])
            elif self.torsoType[0] == 'm':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][4])
            elif self.torsoType[0] == 'l':
                self.backpack_model.setPos(
                    backpack_dict[backpack_to_attach][5])
            else:
                print("What kind of torso are you rockin?")

    def returnBackpackPosition(self):
        return self.backpack_model.getPos()

    def returnGlassesPosition(self):
        return self.glasses_model.getPos()

    def attachGlasses(self, glasses_to_attach):
        '''Attaches glasses to the Toon.'''

        # If we already have glasses
        if self.glasses_model:
            self.glasses_model.removeNode()

        self.glassesType = glasses_to_attach

        if len(glasses_dict[glasses_to_attach]) == 1:  # Regular glasses model.
            self.glasses_model = loader.loadModel(
                glasses_dict[glasses_to_attach][0])
        # Glasses model with different texture
        elif len(glasses_dict[glasses_to_attach]) == 2:
            self.glasses_model = loader.loadModel(
                glasses_dict[glasses_to_attach][0])
            texture = loader.loadTexture(glasses_dict[glasses_to_attach][1])
            self.glasses_model.setTexture(texture, 1)
        # Glasses model with different texture and different rgb file
        elif len(glasses_dict[glasses_to_attach]) == 3:
            self.glasses_model = loader.loadModel(
                glasses_dict[glasses_to_attach][0])
            texture = loader.loadTexture(
                glasses_dict[glasses_to_attach][1], alphaPath=glasses_dict[glasses_to_attach][2])
            self.glasses_model.setTexture(texture, 1)

        self.glasses_model.reparentTo(self.toonActor.find('**/*def_head'))

        # Based on each species type, we'll move the glasses to a different place and scale it
        placement_list = glasses_placement_dict[self.species]

        self.glasses_model.setPos(placement_list[0])
        self.glasses_model.setHpr(180, 0, 0)
        self.glasses_model.setScale(placement_list[1])

        # Some of the glasses don't have correctly placed models, so we do them here.

        if 'Snowy Shades' in glasses_to_attach or 'Experimental Eyewear' == glasses_to_attach:
            if self.species == 'b':  # Bear
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'ca':  # Cat
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'cr':  # Crocodile
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'de':  # Deer
                self.glasses_model.setPos(0, 0.2, 0.2)
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.25)
            elif self.species == 'd':  # Dog
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'du':  # Duck
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.75)
            elif self.species == 'h':  # Horse
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'mo':  # Monkey
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'mi':  # Mouse/Mice
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.6, 1.5, 1.5)
                self.glasses_model.setPos(0, 0.2, 0.45)
            elif self.species == 'p':  # Pig
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'r':  # Rabbit
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.275)
            elif self.species == 'ri':  # Riggy
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.45)
            else:
                self.glasses_model.setHpr(0, 0, 0)
                self.glasses_model.setScale(1.25)
        elif 'Black Mask' in glasses_to_attach or 'Blue Mask' in glasses_to_attach:
            if self.species == 'b':  # Bear
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.5, 0)
            elif self.species == 'ca':  # Cat
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.5, 0)
            elif self.species == 'cr':  # Crocodile
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.39, -0.035)
            elif self.species == 'de':  # Deer
                self.glasses_model.setPos(0, 0.5, 0)
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
            elif self.species == 'd':  # Dog
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.4, 0.2)
            elif self.species == 'du':  # Duck
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.3, 0.3, 0.35)
                self.glasses_model.setPos(0, 0.5, -0.1)
            elif self.species == 'h':  # Horse
                self.glasses_model.setHpr(180, -15, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.3, 0.05)
            elif self.species == 'mo':  # Monkey
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.5, 0.05)
            elif self.species == 'mi':  # Mouse/Mice
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.3)
                self.glasses_model.setPos(0, 0.4, 0.15)
            elif self.species == 'p':  # Pig
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.2)
                self.glasses_model.setPos(0, 0.5, -0.09)
            elif self.species == 'r':  # Rabbit
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.2, 0.25)
                self.glasses_model.setPos(0, 0.4, -0.2)
            elif self.species == 'ri':  # Riggy
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.2, 0.25)
                self.glasses_model.setPos(0, 0.4, -0.2)
            else:
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(1.25)
        elif 'Bug-eyed Binoculars' == glasses_to_attach:  # Little higher than the head
            if self.species == 'b':  # Bear
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.3, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.2, 0.1)
            elif self.species == 'ca':  # Cat
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.25, 0)
            elif self.species == 'cr':  # Crocodile
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.3, 0.3)
                self.glasses_model.setPos(0, 0.25, 0)
            elif self.species == 'de':  # Deer
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.25, 0)
            elif self.species == 'd':  # Dog
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.25, 0.25)
            elif self.species == 'du':  # Duck
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.375, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.25, 0)
            elif self.species == 'h':  # Horse
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.3, 0.25, 0.35)
                self.glasses_model.setPos(0, 0.1, 0.05)
            elif self.species == 'mo':  # Monkey
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.35, 0.35, 0.35)
                self.glasses_model.setPos(0, 0.25, 0.05)
            elif self.species == 'mi':  # Mouse/Mice
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.4)
                self.glasses_model.setPos(0, 0.1, 0.25)
            elif self.species == 'p':  # Pig
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.35)
                self.glasses_model.setPos(0, 0.2, -0.1)
            elif self.species == 'r':  # Rabbit
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32)
                self.glasses_model.setPos(0, 0.1, -0.1)
            elif self.species == 'ri':  # Riggy
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32)
                self.glasses_model.setPos(0, 0.1, -0.1)
            else:
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(1.25)
        elif 'Groucho Glasses' == glasses_to_attach or 'Vintage Teashades' == glasses_to_attach:
            if self.species == 'd':
                self.glasses_model.setPos(0, 0.1, 0.25)
            elif self.species == 'ri':
                self.glasses_model.setPos(0, 0, -0.100)
            else:
                self.glasses_model.setPos(0, 0.1, -0.025)
        elif 'Heart Throbbers' == glasses_to_attach:
            if self.species == 'd':
                self.glasses_model.setPos(0, 0.1, 0.25)
            elif self.species == 'ri':
                self.glasses_model.setScale(0.3, 0.2, 0.3)
                self.glasses_model.setPos(0, 0.2, -0.125)
            else:
                self.glasses_model.setPos(0, 0.1, -0.025)
        elif 'The Fancy Focal' == glasses_to_attach:
            if self.species == 'b':  # Bear
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.3, 0.35, 0.35)
                self.glasses_model.setPos(0.175, 0.5, -0.15)
            elif self.species == 'ca':  # Cat
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32, 0.4, 0.3)
                self.glasses_model.setPos(0.2, 0.5, -0.15)
            elif self.species == 'cr':  # Crocodile
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.3, 0.3)
                self.glasses_model.setPos(0.2, 0.5, -0.15)
            elif self.species == 'de':  # Deer
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.32, 0.35, 0.35)
                self.glasses_model.setPos(0.2, 0.55, -0.2)
            elif self.species == 'd':  # Dog
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.25, 0.35, 0.35)
                self.glasses_model.setPos(0.2, 0.45, 0)
            elif self.species == 'du':  # Duck
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setPos(0.25, 0.55, -0.25)
            elif self.species == 'h':  # Horse
                self.glasses_model.setHpr(180, -15, 0)
                self.glasses_model.setScale(0.3, 0.25, 0.35)
                self.glasses_model.setPos(0.2, 0.35, -0.1)
            elif self.species == 'mo':  # Monkey
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setPos(0.25, 0.55, -0.2)
            elif self.species == 'mi':  # Mouse/Mice
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.5)
                self.glasses_model.setPos(0.25, 0.5, -0.1)
            elif self.species == 'p':  # Pig
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.35)
                self.glasses_model.setPos(0.15, 0.55, -0.25)
            elif self.species == 'r':  # Rabbit
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.35)
                self.glasses_model.setPos(0.25, 0.40, -0.25)
            elif self.species == 'ri':  # Riggy
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(0.35)
                self.glasses_model.setPos(0.25, 0.40, -0.25)
            else:
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setScale(1.25)
        # Gotta move these down a little bit.
        elif 'ToonFest 2020 Pink Glasses' == glasses_to_attach or 'ToonFest 2020 Blue Glasses' == glasses_to_attach:
            if self.species == 'd':
                self.glasses_model.setPos(0, 0.1, 0.25)
                self.glasses_model.setHpr(180, 0, 0)
            elif self.species == 'p':
                self.glasses_model.setScale(0.3, 0.32, 0.35)
                self.glasses_model.setPos(0, 0.2, -0.1)
                self.glasses_model.setHpr(180, 0, 0)
            elif self.species == 'r' or self.species == 'ri':
                self.glasses_model.setScale(0.35, 0.32, 0.35)
                self.glasses_model.setPos(0, 0.1, -0.1)
                self.glasses_model.setHpr(180, 0, 0)
            else:
                self.glasses_model.setHpr(180, 0, 0)
                self.glasses_model.setPos(0, 0.25, 0.05)

    def attachShoes(self, shoeType):
        '''Attaches the shoe based on the type of shoe given.'''

        if shoeType == 1:  # Shoes
            self.toonActor.find('**/*shoes').show()
            self.toonActor.find('**/*boots_short').hide()
            self.toonActor.find('**/*boots_long').hide()
            self.toonActor.find('**/*feet').hide()
        elif shoeType == 2:  # Short boots
            self.toonActor.find('**/*shoes').hide()
            self.toonActor.find('**/*boots_short').show()
            self.toonActor.find('**/*boots_long').hide()
            self.toonActor.find('**/*feet').hide()
        elif shoeType == 3:  # Long boots
            self.toonActor.find('**/*shoes').hide()
            self.toonActor.find('**/*boots_short').hide()
            self.toonActor.find('**/*boots_long').show()
            self.toonActor.find('**/*feet').hide()
        else:
            self.hideShoePieces()

    def hideShoePieces(self):
        self.toonActor.find('**/*boots_short').hide()
        self.toonActor.find('**/*boots_long').hide()
        self.toonActor.find('**/*shoes').hide()
        self.toonActor.find('**/*feet').show()

    def applyLongBootTexture(self, longBootTexture):
        '''Applies the long boot texture to the long boot node'''
        try:
            if len(boot_long_texture_dict[longBootTexture]) == 1:
                texture = loader.loadTexture(
                    boot_long_texture_dict[longBootTexture][0])
                self.toonActor.find('**/*boots_long').setTexture(texture, 1)
            elif len(boot_long_texture_dict[longBootTexture]) == 2:
                texture = loader.loadTexture(
                    boot_long_texture_dict[longBootTexture][0], boot_long_texture_dict[longBootTexture][1])
                self.toonActor.find('**/*boots_long').setTexture(texture, 1)
        except:
            pass

    def applyShortBootTexture(self, shortBootTexture):
        try:
            texture = loader.loadTexture(shoeTexture_dict[shortBootTexture])
            self.toonActor.find('**/*boots_short').setTexture(texture, 1)
        except:
            pass

    def applyShoeTexture(self, shoeTexture):

        '''Applies the shoe texture to the shoe nodes'''
        try:
            texture = loader.loadTexture(shoeTexture_dict[shoeTexture])
            self.toonActor.find('**/*shoes').setTexture(texture, 1)
        except:
            pass

# Toon Functions

    def updateToonInfo(self, species, headType, hasEyelashes, torsoType, legSize, headColor, armColor, gloveColor, legColor, shirtTexture, shortTexture, skirtTexture, shirtColor, bottomColor, backpack, glasses, shoes_type, longBootTexture, shortBootTexture, shoes_texture, animation_type, is60FPS, wearsShoes):
        '''Updates the Toon's DNA with the arguments'''

        self.updateSpecies(species)
        self.updateHead(species, headType, hasEyelashes)
        self.updateTorso(torsoType)
        self.updateLegs(legSize)
        
        self.updateHeadColor(headColor)
        self.updateArmsColor(armColor)
        self.updateGloveColor(gloveColor)
        self.updateLegsColor(legColor)
        
        self.setShirtTexture(shirtTexture)
        self.setShortTexture(shortTexture)
        self.setSkirtTexture(skirtTexture)

        self.setShirtColor(shirtColor)
        self.setBottomColor(bottomColor)

        self.attachBackpack(backpack)
        self.attachGlasses(glasses)
        self.attachShoes(shoes_type)

        self.applyShoeTexture(shoes_texture)
        self.applyShortBootTexture(shortBootTexture)
        self.applyLongBootTexture(longBootTexture)

        self.animationType = animation_type
        self.smoothEnabled = is60FPS

        self.wearsShoes = wearsShoes



    def setPosition(self, x, y, z):
        '''Sets the position of the Toon's actor'''
        self.toonActor.setPos(x,y,z)

    def __str__(self) -> str:
        '''String representation of a Toon object'''
        #toonString = ', {self.shirtTexture}, {self.shortTexture}, {self.skirtTexture}, '{self.bottomColor}', {self.shoeType}, {self.shoeTexture}, {self.longBootTexture}, {self.shortBootTexture}, {self.backpackType}, {self.glassesType}, {self.smoothEnabled}, {self.wearsShoes})"
        toonString = ''
        toonString += f"Toon('{self.species}', "
        toonString += f"'{self.headtype}', "
        toonString += f"{str(self.eyelashes)}, "
        toonString += f"'{self.torsoType}', "
        toonString += f"'{self.legSize}', "
        toonString += f"'{self.headColor}', "
        toonString += f"'{self.armColor}', "
        toonString += f"'{self.gloveColor}', "
        toonString += f"'{self.legColor}', "
        
        if self.shirtTexture:
            toonString += f"'{self.shirtTexture}', "
        else:
            toonString += f"{self.shirtTexture}, "

        if self.shortTexture:
            toonString += f"'{self.shortTexture}', "
        else:
            toonString += f"{self.shortTexture}, "

        if self.skirtTexture:
            toonString += f"'{self.skirtTexture}', "
        else:
            toonString += f"{self.skirtTexture}, "
        
        toonString += f"'{self.shirtColor}', "
        toonString += f"'{self.bottomColor}', "
        
        if self.backpackType:
            toonString += f"'{self.backpackType}', "
        else:
            toonString += f"{self.backpackType}, "

        if self.glassesType:
            toonString += f"'{self.glassesType}', "
        else:
            toonString += f"{self.glassesType}, "

        if self.shoeType:
            toonString += f"{self.shoeType}, "
        else:
            toonString += f"{self.shoeType}, "

        if self.longBootTexture:
            toonString += f"'{self.longBootTexture}', "
        else:
            toonString += f"{self.longBootTexture}, "

        if self.shortBootTexture:
            toonString += f"'{self.shortBootTexture}', "
        else:
            toonString += f"{self.shortBootTexture}, "

        if self.shoeTexture:
            toonString += f"'{self.shoeTexture}', "
        else:
            toonString += f"{self.shoeTexture}, "

        if self.animationType:
            toonString += f"'{self.animationType}', "
        else:
            toonString += f"{self.animationType}, "

        if self.smoothEnabled:
            toonString += f"{self.smoothEnabled}, "
        else:
            toonString += f"{self.smoothEnabled}, "

        if self.wearsShoes:
            toonString += f"{self.wearsShoes}"
        else:
            toonString += f"{self.wearsShoes}"

        toonString+= ')'

        return toonString
