from direct.actor.Actor import Actor
from panda3d.core import *
from ToonHead import *
from ToonDNA import *


toonTorsoTypes = { "ss": 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_1000.bam', # short shorts
                   "ms": 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam', # medium shorts
                   "ls": 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_1000.bam', # long shorts
                   "sd": 'phase_3/models/char/tt_a_chr_dgs_skirt_torso_1000.bam', # short dress (Should be given this one and below if species is girl) 
                   "md": 'phase_3/models/char/tt_a_chr_dgm_skirt_torso_1000.bam', # medium dress
                   "ld": 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_1000.bam', # long dress
                 } 

toonLegTypes = { "s":'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam', # small
                 "m":'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam', # medium
                 "l":'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam'  # long
                } 

class Toon:
    '''Toon Actor, contains the body and the legs, but attaches on the head retrieved from ToonHead'''
    def __init__(self, species, head_type=None, has_eyelashes=False, torso_type=None, leg_size=None, gender=None, head_color='White', arm_color='White', glove_color='White', leg_color='White', shirt_texture=None, bottom_texture=None, backpack=None, glasses = None, animation_type=None, is60FPS=None, wearsShoes=None):
        # DNA based stuff
        self.toonActor = None
        self.species = species
        self.headtype = head_type 
        self.torso_type = torso_type
        self.leg_size = leg_size
        self.gender= gender
        self.head_color = head_color
        self.arm_color = arm_color
        self.glove_color = glove_color
        self.leg_color = leg_color
        self.eyelashes = has_eyelashes
    
        # Clothing based stuff
        self.shirt_texture = shirt_texture
        self.bottom_texture = bottom_texture

        # Accessory based stuff
        self.backpack_type = backpack
        self.backpack_model = None
        self.hat = None
        self.glasses_type = glasses # Also counts for mask since they're both the same.
        self.glasses_model = None

        self.animationType = animation_type
        self.smooth_enabled = is60FPS
        self.wearsShoes = wearsShoes

        self.head = ToonHead(self.species, self.headtype, self.eyelashes)
        self.torso = toonTorsoTypes[self.torso_type]
        self.legs = toonLegTypes[self.leg_size]

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
         'head': {self.animationType: self.returnHeadAnim(self.headtype, self.animationType)},
         'torso': {self.animationType: self.returnTorsoAnim(self.torso_type, self.animationType)},
         'legs':  {self.animationType: self.returnLegsAnim(self.leg_size, self.animationType)} 
        })

        self.toonActor.attach('head', 'torso', 'def_head')
        self.toonActor.attach('torso', 'legs', 'joint_hips')

        self.toonActor.reparentTo(render)
        self.toonActor.setPos(2,35,0)
        self.toonActor.setHpr(180,0,0)

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
        '''Updates the head type.'''
        self.headtype = head_type
        self.species = species
        self.eyelashes = has_eyelashes
        self.head = ToonHead(species, head_type, has_eyelashes)
    
    def updateHeadColor(self, color_to_set):
        '''Updates the Toon's head color'''
        self.head_color = color_to_set

        if self.species == 'd':
            self.toonActor.find('**/head').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front').setColor(colorsList[self.head_color])
        elif self.species == 'de': # Gotta account for Deers only having one head type.
            self.toonActor.find('**/*ears-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
        elif self.species == 'du': # Gotta account for ducks not having ears
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-long').setColor(colorsList[self.head_color])
        elif self.species == 'ri': # Riggy only has one head type.
            self.toonActor.find('**/*ears').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front').setColor(colorsList[self.head_color])
        else:
            self.toonActor.find('**/*ears-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-short').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*ears-long').setColor(colorsList[self.head_color])
            self.toonActor.find('**/*head-front-long').setColor(colorsList[self.head_color])
        self.toonActor.find('**/neck').setColor(colorsList[self.head_color])

    def updateTorso(self, torso_type):
        '''Updates the torso type'''
        self.torso = toonTorsoTypes[torso_type]
        self.torso_type = torso_type

    def updateArmsColor(self, color_to_set):
        self.arm_color = color_to_set
        self.toonActor.find('**/arms').setColor(colorsList[self.arm_color])

    def updateLegs(self, legs_type):
        '''Updates the leg type'''
        self.leg_size = legs_type
        self.legs = toonLegTypes[legs_type]

    def updateLegsColor(self, color_to_set):
        '''Update the Toon leg colors'''
        self.leg_color = color_to_set
        self.toonActor.find('**/legs').setColor(colorsList[self.leg_color])
        self.toonActor.find('**/feet').setColor(colorsList[self.leg_color])
        
    def updateGloveColor(self, color_to_set):
        '''Colors the Toon's gloves'''
        self.glove_color = color_to_set
        self.toonActor.find('**/hands').setColor(colorsList[self.glove_color])

    def returnHead(self):
        '''Just returns the head'''
        return self.head.head_model

    def returnHeadAnim(self, headType, animation_type):
        headSizeIndex = headType[0]

        if headSizeIndex == 'l':
            return 'phase_3/models/char/tt_a_chr_dgl_shorts_head_' + animation_type + '.bam'
        elif headSizeIndex == 'm':
            return 'phase_3/models/char/tt_a_chr_dgm_shorts_head_' + animation_type + '.bam'
        elif headSizeIndex == 's':
            return 'phase_3/models/char/tt_a_chr_dgs_shorts_head_' + animation_type + '.bam'
    
    def returnTorso(self):
        '''Returns the torso'''
        return self.torso
    
    def returnTorsoAnim(self, torsoType, animation_type):

        if torsoType == 'ss':
            return 'phase_3/models/char/tt_a_chr_dgs_shorts_torso_' + animation_type + '.bam'
        elif torsoType == 'ms':
            return 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_' + animation_type + '.bam'
        elif torsoType == 'ls':
            return 'phase_3/models/char/tt_a_chr_dgl_shorts_torso_' + animation_type + '.bam'
        elif torsoType == 'sd':
            return 'phase_3/models/char/tt_a_chr_dgs_skirt_torso_' + animation_type + '.bam'
        elif torsoType == 'md':
            return 'phase_3/models/char/tt_a_chr_dgm_skirt_torso_' + animation_type + '.bam'
        elif torsoType == 'ld':
            return 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_' + animation_type + '.bam'
        
    def returnLegs(self):
        '''Returns the legs'''
        return self.legs    
    
    def returnLegsAnim(self, legsType, animation_type):
        legSizeIndex = legsType

        if legSizeIndex == 'l':
            return 'phase_3/models/char/tt_a_chr_dgl_shorts_legs_' + animation_type + '.bam'
        elif legSizeIndex == 'm':
            return 'phase_3/models/char/tt_a_chr_dgm_shorts_legs_' + animation_type + '.bam'
        elif legSizeIndex == 's':
            return 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_' + animation_type + '.bam'

 # Accessory related functions       
    def attachBackpack(self, backpack_to_attach):
        '''Attaches a backpack based on the type of backpack.'''

        if self.backpack_model: # So if we already had a model before changing it, remove its node.
            self.backpack_model.removeNode()
        else:
            pass

        # Doing this because some backpacks require a model and texture while others just need the bam file.
     
        if len( backpack_dict[backpack_to_attach] ) == 5:
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale( backpack_dict[ backpack_to_attach ][4] )
            if 'Sword' in backpack_to_attach:
                self.backpack_model.setHpr(180,15,30)
            elif "Bag" in backpack_to_attach:
                self.backpack_model.setHpr(0,0,0)
            elif 'Tail' in backpack_to_attach or 'Fin' in backpack_to_attach:
                self.backpack_model.setHpr(180,20,0)
            else:    
                self.backpack_model.setHpr(180,0,0)

            if self.torso_type[0] == 's':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][1] )
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][2] )
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][3] )
            else:
                print("What kind of torso are you rockin?")

        elif len( backpack_dict[backpack_to_attach] ) == 6: # This is when we need to retexture something like the ToonFest backpacks, or scarves.
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture( backpack_dict[backpack_to_attach][1])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale( backpack_dict[ backpack_to_attach ][5] )

            if 'Bowtie' in backpack_to_attach:
                self.backpack_model.setHpr(180,-50,0)
            else:
                self.backpack_model.setHpr(180,0,0)

            if self.torso_type[0] == 's':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][2] )
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][3] )
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][4] )
            else:
                print("What kind of torso are you rockin?")

        elif len( backpack_dict[backpack_to_attach] ) == 7: # This is when we need to retexture something like the Jellybean Jar reskins, which have an RGB file.
            self.backpack_model = loader.loadModel(backpack_dict[backpack_to_attach][0])
            texture = loader.loadTexture( texturePath = backpack_dict[backpack_to_attach][1], alphaPath= backpack_dict[backpack_to_attach][2])
            self.backpack_model.setTexture(texture, 1)
            self.backpack_model.reparentTo(self.toonActor.find('**/*def_joint_attachFlower'))
            self.backpack_model.setScale( backpack_dict[ backpack_to_attach ][6] )

            if self.torso_type[0] == 's':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][3] )
            elif self.torso_type[0] == 'm':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][4] )
            elif self.torso_type[0] == 'l':
                self.backpack_model.setPos( backpack_dict[ backpack_to_attach ][5] )
            else:
                print("What kind of torso are you rockin?")


            if 'Oil Pale Pack' in backpack_to_attach: # Oil Pale Pack's rotation is correct, unlike the other models
                self.backpack_model.setHpr(180,0,0)

    def attachGlasses(self, glasses_to_attach):
        self.glasses_type = glasses_to_attach
        self.glasses_model = loader.loadModel(glasses_dict[glasses_to_attach])
        self.glasses_model.reparentTo(self.toonActor.find('**/*head'))
        self.glasses_model.setPos(0,0.1,0.2)
        self.glasses_model.setHpr(180,0,0)
        self.glasses_model.setScale(0.4)
