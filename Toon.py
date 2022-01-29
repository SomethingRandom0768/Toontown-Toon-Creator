from direct.actor.Actor import Actor
from panda3d.core import *
from ToonHead import *


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
    def __init__(self, species, head_type=None, has_eyelashes=False, torso_type=None, leg_size=None, gender=None, head_color=None, glove_color=None, torso_color=None, leg_color=None, shirt_texture=None, shirt_color=None,bottom_color=None, animation_type=None, is60FPS=None, wearsShoes=None):
        self.species = species
        self.headtype = head_type # This basically helps set the species.
        self.torso_type = torso_type
        self.leg_size = leg_size
        self.gender= gender
        self.head_color = head_color
        self.glove_color = glove_color
        self.torso_color = torso_color
        self.leg_color = leg_color
        self.shirt_texture = shirt_texture
        self.shirt_color = shirt_color
        self.bottom_color = bottom_color
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
            self.toonActor.find('**/*shoes').removeNode()
            self.toonActor.find('**/*boots_short').removeNode()
            self.toonActor.find('**/*boots_long').removeNode()

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
    
    def updateTorso(self, torso_type):
        '''Updates the torso type'''
        self.torso = toonTorsoTypes[torso_type]
        self.torso_type = torso_type

    def updateLegs(self, legs_type):
        '''Updates the leg type'''
        self.leg_size = legs_type
        self.legs = toonLegTypes[legs_type]

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
        