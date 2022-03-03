from direct.actor.Actor import Actor
from panda3d.core import *
from ToonHead import *
from ToonDNA import *

toonTorsoTypes = {
    "ss": 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam',  # short shorts
    "ms": 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam',  # medium shorts
    "ls": 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam',  # long shorts
    "sd": 'phase_3/models/char/tt_a_chr_dgs_skirt_torso_1000.bam',  # short dress
    "md": 'phase_3/models/char/tt_a_chr_dgm_skirt_torso_1000.bam',  # medium dress
    "ld": 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_1000.bam',  # long dress
}

toonLegTypes = {
    "s": 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam',  # small
    "m": 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam',  # medium
    "l": 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam'  # long
}


class Toon:
    """Toon Actor, contains the body and the legs, but attaches on the head retrieved from ToonHead"""

    def __init__(self, species, head_type=None, has_eyelashes=False, torso_type=None, leg_size=None, gender=None,
                 head_color='White', arm_color='White', glove_color='White', leg_color='White', shirt_texture=None,
                 short_texture=None, skirt_texture=None, shirt_color='White', bottom_color='White', backpack=None,
                 glasses=None, animation_type=None, is60FPS=None, wearsShoes=None):
        # DNA based stuff
        self.toonActor = None
        self.species = species
        self.headtype = head_type
        self.torso_type = torso_type
        self.leg_size = leg_size
        self.gender = gender
        self.head_color = head_color
        self.arm_color = arm_color
        self.glove_color = glove_color
        self.leg_color = leg_color
        self.eyelashes = has_eyelashes

        # Clothing based stuff
        self.shirt_texture = shirt_texture
        self.shirt_color = shirt_color
        self.short_texture = short_texture
        self.skirt_texture = skirt_texture
        self.bottom_color = bottom_color

        # Accessory based stuff
        self.backpack_type = backpack
        self.backpack_model = None
        self.hat = None
        # Also counts for mask since they're both the same.
        self.glasses_type = glasses
        self.glasses_model = None

        self.animationType = animation_type
        self.smooth_enabled = is60FPS
        self.wearsShoes = wearsShoes

        self.head = ToonHead(self.species, self.headtype, self.eyelashes)
        self.torso = toonTorsoTypes[self.torso_type]
        self.legs = toonLegTypes[self.leg_size]

        self.generateActor()

    def generateActor(self):
        """Updates Toon's pieces, and then creates an actor."""
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
                'torso': self.returnTorsoAnim(self.torso_type),
                'legs': self.returnLegsAnim(self.leg_size)
            }
        )

        self.toonActor.attach('head', 'torso', 'def_head')
        self.toonActor.attach('torso', 'legs', 'joint_hips')

        self.toonActor.reparentTo(render)
        self.toonActor.setPos(2, 35, 0)
        self.toonActor.setHpr(180, 0, 0)

        if self.smooth_enabled:
            self.toonActor.setBlend(frameBlend=True)
        else:
            pass

        self.toonActor.loop(self.animationType)

        # Remove shoes
        if self.wearsShoes:
            pass
        else:
            self.toonActor.find('**/*shoes').hide()
            self.toonActor.find('**/*boots_short').hide()
            self.toonActor.find('**/*boots_long').hide()

        # Add the coloring to the Toon based on its color variables.
        self.updateHeadColor(self.head_color)
        self.updateArmsColor(self.arm_color)
        self.updateLegsColor(self.leg_color)
        self.updateGloveColor(self.glove_color)

        # Clothing related stuff
        if self.shirt_texture:
            self.setShirtTexture(self.shirt_texture)
        else:
            pass

        if self.torso_type:
            self.setShortTexture(self.short_texture)
            self.setSkirtTexture(self.skirt_texture)
        else:
            pass

        if self.shirt_color:
            self.setShirtColor(self.shirt_color)
        else:
            pass

        if self.bottom_color:
            self.setBottomColor(self.bottom_color)
        else:
            pass

        # Accessory related stuff
        if self.backpack_type:
            self.attachBackpack(self.backpack_type)
        else:
            pass

        if self.glasses_type:
            self.attachGlasses(self.glasses_type)
        else:
            pass

        # Add shadow
        shadow = loader.loadModel("phase_3/models/props/drop_shadow.bam")
        shadow.reparentTo(self.toonActor.find('**/joint_shadow'))

        shadow.setSx(0.5)
        shadow.setSy(0.5)

    # DNA Related functions

    def updateSpecies(self, species_to_change_to):
        self.species = species_to_change_to
        self.head = ToonHead(self.species, self.headtype, self.eyelashes)

    def updateHead(self, species, head_type, has_eyelashes):
        """Updates the head type."""
        self.headtype = head_type
        self.species = species
        self.eyelashes = has_eyelashes
        self.head = ToonHead(species, head_type, has_eyelashes)

    def updateHeadColor(self, color_to_set):
        """Updates the Toon's head color"""
        self.head_color = color_to_set

        if self.species == 'd':
            self.toonActor.find('**/head').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front').setColor(colorsList[self.head_color])
        elif self.species == 'de':  # Gotta account for Deers only having one head type.
            self.toonActor.find('**/*ears-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
        elif self.species == 'du':  # Gotta account for ducks not having ears
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-long').setColor(colorsList[self.head_color])
        elif self.species == 'ri':  # Riggy only has one head type.
            self.toonActor.find('**/*ears').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front').setColor(colorsList[self.head_color])
        elif self.species == 'mo':  # Monkeys can't get their ears colored.
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-long').setColor(colorsList[self.head_color])
        else:
            self.toonActor.find('**/*ears-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*ears-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-long').setColor(colorsList[self.head_color])
        self.toonActor.find('**/neck').setColor(colorsList[self.head_color])

    def updateTorso(self, torso_type):
        """Updates the torso type"""
        self.torso = toonTorsoTypes[torso_type]
        self.torso_type = torso_type

    def updateArmsColor(self, color_to_set):
        self.arm_color = color_to_set
        self.toonActor.find('**/arms').setColor(colorsList[self.arm_color])

    def updateLegs(self, legs_type):
        """Updates the leg type"""
        self.leg_size = legs_type
        self.legs = toonLegTypes[legs_type]

    def updateLegsColor(self, color_to_set):
        """Update the Toon leg colors"""
        self.leg_color = color_to_set
        self.toonActor.find('**/legs').setColor(colorsList[self.leg_color])
        self.toonActor.find('**/feet').setColor(colorsList[self.leg_color])

    def updateGloveColor(self, color_to_set):
        """Colors the Toon's gloves"""
        self.glove_color = color_to_set
        self.toonActor.find('**/hands').setColor(colorsList[self.glove_color])

    def returnHead(self):
        """Just returns the head"""
        return self.head.head_model

    def returnHeadAnim(self, headType):
        headSizeIndex = headType[0]

        if self.torso_type[1] == 's':
            if headSizeIndex == 'l':
                return long_head_shorts_anim_dict
            elif headSizeIndex == 'm':
                return medium_head_shorts_anim_dict
            elif headSizeIndex == 's':
                return short_head_shorts_anim_dict
        else:
            return medium_head_skirt_anim_dict

    def returnTorso(self):
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
        """Sets the Toon's texture based on the shirt variable (the key in the ToonDNA dictionary)"""

        try:
            shirtTexturePath = shirt_dict[shirt][0]
            shirtTexture = loader.loadTexture(shirtTexturePath)
            self.toonActor.find('**/torso-top').setTexture(shirtTexture, 1)

            if len(shirt_dict[shirt]) == 2:
                sleeveTexturePath = shirt_dict[shirt][1]
                sleeveTexture = loader.loadTexture(sleeveTexturePath)
                self.toonActor.find('**/sleeves').setTexture(sleeveTexture, 1)
            else:
                pass
        except:
            print(
                f"Your Shirt Texture {shirt} will result in a crash. Please check either ToonDNA.py or the main file.")

    def setShortTexture(self, short):
        """Sets the Toon's short texture. Used when generating the Toon"""
        if self.torso_type[-1] == 's':
            try:
                shortTexturePath = short_dict[short]
                shortTexture = loader.loadTexture(shortTexturePath)
                self.toonActor.find('**/torso-bot').setTexture(shortTexture, 1)
            except:
                print(
                    f"Your Short Texture {short} will result in a crash. Please check either ToonDNA.py or the main file.")
        else:
            pass

    def setSkirtTexture(self, skirt):
        """Sets the Toon's short texture. Used when generating the Toon"""
        if self.torso_type[-1] == 'd':
            try:
                skirtTexturePath = skirt_dict[skirt]
                skirtTexture = loader.loadTexture(skirtTexturePath)
                self.toonActor.find('**/torso-bot').setTexture(skirtTexture, 1)
            except:
                print(
                    f"Your Short Texture {skirt} will result in a crash. Please check either ToonDNA.py or the main file. ")
        else:
            pass

    def setShirtColor(self, shirt_color):
        """Colors the Toon's current shirt"""
        self.toonActor.find('**/torso-top').setColorScale(colorsList[shirt_color])
        self.toonActor.find('**/sleeves').setColorScale(colorsList[shirt_color])

    def setBottomColor(self, bottom_color):
        """Colors the Toon's current bottom"""
        if self.torso_type == 'ls':
            self.toonActor.find('**/torso-bot').setColor(colorsList[bottom_color])
        else:
            self.toonActor.find('**/torso-bot').setColorScale(colorsList[bottom_color])

    # Accessory related functions
    def attachBackpack(self, backpack_to_attach):
        """Attaches a backpack based on the type of backpack."""

        # So if we already had a model before changing it, remove its node.
        if self.backpack_model:
            self.backpack_model.removeNode()
        else:
            pass

        # Doing this because some backpacks require a model and texture while others just need the bam file.
        if len(backpack_dict[backpack_to_attach]) == 5:
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][4])

            if 'Sword' in backpack_to_attach:
                self.backpack_model.setHpr(180, 15, 30)
            elif "Bag" in backpack_to_attach:
                self.backpack_model.setHpr(0, 0, 0)
            elif 'Tail' in backpack_to_attach or 'Fin' in backpack_to_attach:
                self.backpack_model.setHpr(180, 20, 0)
            elif 'Bowtie' in backpack_to_attach:
                self.backpack_model.setHpr(180, -50, 0)
            elif 'Oil Pale Pack' in backpack_to_attach:
                self.backpack_model.setHpr(180, 0, 0)
            else:
                self.backpack_model.setHpr(180, 0, 0)

            if self.torso_type[0] == 's':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][1])
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][2])
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][3])
            else:
                print("What kind of torso are you rockin?")

        elif len(backpack_dict[
                     backpack_to_attach]) == 6:  # This is when we need to retexture something like the ToonFest backpacks, or scarves.
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture(backpack_dict[backpack_to_attach][1])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][5])
            self.backpack_model.setHpr(180, 0, 0)

            if self.torso_type[0] == 's':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][2])
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][3])
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][4])
            else:
                print("What kind of torso are you rockin?")

        elif len(backpack_dict[
                     backpack_to_attach]) == 7:  # This is when we need to retexture something like the Jellybean Jar reskins, which have an RGB file.
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture(texturePath=backpack_dict[backpack_to_attach][1],
                                         alphaPath=backpack_dict[backpack_to_attach][2])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale(backpack_dict[backpack_to_attach][6])
            self.backpack_model.setHpr(180, 0, 0)

            if self.torso_type[0] == 's':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][3])
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][4])
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos(backpack_dict[backpack_to_attach][5])
            else:
                print("What kind of torso are you rockin?")

    def attachGlasses(self, glasses_to_attach):
        """Attaches glasses to the Toon."""

        # If we already have glasses
        if self.glasses_model:
            self.glasses_model.removeNode()

        self.glasses_type = glasses_to_attach

        if len(glasses_dict[glasses_to_attach]) == 1:  # Regular glasses model.
            self.glasses_model = loader.loadModel(glasses_dict[glasses_to_attach][0])
        elif len(glasses_dict[glasses_to_attach]) == 2:  # Glasses model with different texture
            self.glasses_model = loader.loadModel(glasses_dict[glasses_to_attach][0])
            texture = loader.loadTexture(glasses_dict[glasses_to_attach][1])
            self.glasses_model.setTexture(texture, 1)
        elif len(glasses_dict[glasses_to_attach]) == 3:  # Glasses model with different texture and different rgb file
            self.glasses_model = loader.loadModel(glasses_dict[glasses_to_attach][0])
            texture = loader.loadTexture(glasses_dict[glasses_to_attach][1],
                                         alphaPath=glasses_dict[glasses_to_attach][2])
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
        elif 'ToonFest 2020 Pink Glasses' == glasses_to_attach or 'ToonFest 2020 Blue Glasses' == glasses_to_attach:  # Gotta move these down a little bit.
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
