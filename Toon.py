from direct.actor.Actor import Actor
from panda3d.core import *
from ToonHead import *


toonTorsoTypes = [ "ss", "ms", "ls", # short shorts, medium shorts, long shorts,
                   "sd", "md", "ld", # short dress,  medium dress,  long dress.
                   "s", "m", "l"     # short naked,  medium naked, long naked
                 ] 

toonLegTypes = { "s":'phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam',
                 "m":'phase_3/models/char/tt_a_chr_dgm_shorts_legs_1000.bam', 
                 "l":'phase_3/models/char/tt_a_chr_dgl_shorts_legs_1000.bam' 
                } 
# Short, Medium, Long.

colorsList = {
    'White'        : VBase4(1.0, 1.0, 1.0, 1.0),                 
    'Peach'        : VBase4(0.96875, 0.691406, 0.699219, 1.0),   
    'Bright Red'   : VBase4(0.933594, 0.265625, 0.28125, 1.0),   
    'Red'          : VBase4(0.863281, 0.40625, 0.417969, 1.0),   
    'Maroon'       : VBase4(0.710938, 0.234375, 0.4375, 1.0),    
    'Sienna'       : VBase4(0.570312, 0.449219, 0.164062, 1.0),  
    'Brown'        : VBase4(0.640625, 0.355469, 0.269531, 1.0),  
    'Tan'          : VBase4(0.996094, 0.695312, 0.511719, 1.0),  
    'Coral'        : VBase4(0.832031, 0.5, 0.296875, 1.0),       
    'Orange'        :VBase4(0.992188, 0.480469, 0.167969, 1.0),  
    'Yellow'        :VBase4(0.996094, 0.898438, 0.320312, 1.0),  
    'Cream'         :VBase4(0.996094, 0.957031, 0.597656, 1.0),  
    'Citrine'       :VBase4(0.855469, 0.933594, 0.492188, 1.0),  
    'Lime Green'    :VBase4(0.550781, 0.824219, 0.324219, 1.0),  
    'Sea Green'     :VBase4(0.242188, 0.742188, 0.515625, 1.0),  
    'Green'         :VBase4(0.304688, 0.96875, 0.402344, 1.0),   
    'Light Blue'    :VBase4(0.433594, 0.90625, 0.835938, 1.0),   
    'Aqua'          :VBase4(0.347656, 0.820312, 0.953125, 1.0),  
    'Blue'          :VBase4(0.191406, 0.5625, 0.773438, 1.0),    
    'Periwinkle'    :VBase4(0.558594, 0.589844, 0.875, 1.0),     
    'Royal Blue'    :VBase4(0.285156, 0.328125, 0.726562, 1.0),  
    'Slate Blue'    :VBase4(0.460938, 0.378906, 0.824219, 1.0),  
    'Purple'        :VBase4(0.546875, 0.28125, 0.75, 1.0),       
    'Lavender'      :VBase4(0.726562, 0.472656, 0.859375, 1.0),  
    'Pink'          :VBase4(0.898438, 0.617188, 0.90625, 1.0),   
    'Gray'          :VBase4(0.7, 0.7, 0.8, 1.0),                 
    'Black'         :VBase4(0.3, 0.3, 0.35, 1.0), 
}

class Toon:
    '''This is the Actor that is a toon. Reads from ToonDNA's data for clothing'''
    def __init__(self, species, head_type=None, torso_type=None, leg_size=None, gender=None, head_color=None, glove_color=None, torso_color=None, leg_color=None, shirt_texture=None, shirt_color=None,bottom_color=None):
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

        self.head = ToonHead(self.species, self.headtype)
        #self.torso = returnTorso(self.torso_type)
        self.legs = toonLegTypes[leg_size]

        self.generateActor()
        
        # phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral.bam
        # phase_3/models/char/tt_a_chr_dgm_shorts_head_neutral.bam
        # phase_3/models/char/tt_a_chr_dgs_shorts_head_neutral.bam

    def generateActor(self):
        '''Updates Toon's pieces, and then creates an actor.'''

        if self.toonActor:
            self.toonActor = None

        self.toonActor = Actor(
        
        {
            'head': self.returnHead(),
            'torso': 'phase_3/models/char/tt_a_chr_dgm_shorts_torso_1000.bam',
            'legs': self.returnLegs()
        },

        {
         'head': {'neutral': 'phase_3/models/char/tt_a_chr_dgl_shorts_head_neutral.bam' },
         'torso': {'neutral':'phase_3/models/char/tt_a_chr_dgm_shorts_torso_neutral.bam'},
         'legs':  {'neutral':'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam'} 
        })

        self.toonActor.attach('head', 'torso', 'def_head')
        self.toonActor.attach('torso', 'legs', 'joint_hips')

        self.toonActor.reparentTo(render)
        self.toonActor.setPos(2,35,0)
        self.toonActor.setHpr(180,0,0)
        self.toonActor.loop('neutral')

        shadow = loader.loadModel("phase_3/models/props/drop_shadow.bam")
        shadow.reparentTo(self.toonActor.find('**/joint_shadow'))

        shadow.setSx(0.5)
        shadow.setSy(0.5)
        
    def updateHead(self, species, head_type):
        self.head = ToonHead(species, head_type)
        self.headtype = head_type

    #def updateTorso(self, torso_type):

    def updateLegs(self, legs_type):
        self.legs = toonLegTypes[legs_type]

    def returnHead(self):
        '''Just returns the head node'''
        return self.head.head_model

    def returnLegs(self):
        '''Returns legs'''
        return self.legs    
        
        