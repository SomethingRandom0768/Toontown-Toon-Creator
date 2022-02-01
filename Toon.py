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
    '''This is the Actor that is a toon. Reads from ToonDNA's data for clothing'''
    def __init__(self, species, head_type=None, has_eyelashes=False, torso_type=None, leg_size=None, gender=None, head_color='White', arm_color='White', glove_color='White', leg_color='White', shirt_texture=None, shirt_color=None,bottom_color=None, animation_type=None, is60FPS=None, wearsShoes=None):
        self.species = species
        self.headtype = head_type # This basically helps set the species.
        self.torso_type = torso_type
        self.leg_size = leg_size
        self.gender= gender
        self.head_color = head_color
        self.arm_color = arm_color
        self.glove_color = glove_color
        self.leg_color = leg_color
        self.shirt_texture = shirt_texture
        self.toonActor = None
        self.eyelashes = has_eyelashes
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

        # Add shadow
        shadow = loader.loadModel("phase_3/models/props/drop_shadow.bam")
        shadow.reparentTo(self.toonActor.find('**/joint_shadow'))

        shadow.setSx(0.5)
        shadow.setSy(0.5)

    def updateSpecies(self, species_to_change_to):
        self.species = species_to_change_to

    def updateHead(self, species, head_type, has_eyelashes):
        '''Updates the head type.'''
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
        