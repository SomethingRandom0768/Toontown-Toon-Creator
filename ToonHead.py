from direct.actor.Actor import Actor
from panda3d.core import NodePath

class ToonHead:
#TODO NEED TO REWRITE IT TO WHERE THE SPECIES WILL AFFECT THE MODEL OF THE HEAD SHOWN. 
#THE SLICE OF THE STRING THAT REPRESENTS THE MUZZLE AND THE HEAD SIZE WILL BE USED TO HIDE AND SHOW BITS AND PIECES.
    def __init__(self, species, headType, gender='m'):
        '''Species - what species the toon is
           Type - What type of head are we going for (what head type and muzzle type?)
        '''

        # generateHead creates the specific species head model, generateHeadDetails changes the head size and the muzzle size
        self.head_model = self.generateHead(species)
        self.generateHeadDetails(self.head_model, species, headType)

    def generateHead(self, species):
        '''Generates the head model based on the species. Passes headType and gender to the details function'''

        # All the bears
        if species == 'b': 
            headModel = loader.loadModel('phase_3/models/char/bear-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the cats
        elif species == 'ca':
            headModel = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the crocodiles
        elif species == 'cr':
            headModel = loader.loadModel('phase_3/models/char/crocodile-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the deers
        elif species == 'de':
            headModel = loader.loadModel('phase_3/models/char/deer-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the dogs (WIP)
        # All the ducks
        elif species == 'du':
            headModel = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the horses
        elif species == 'h':
            headModel = loader.loadModel('phase_3/models/char/horse-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the monkeys
        elif species == 'mo':
            headModel = loader.loadModel('phase_3/models/char/monkey-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the mice
        elif species == 'mi':
            headModel = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the pigs
        elif species == 'p':
            headModel = loader.loadModel('phase_3/models/char/pig-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        # All the rabbits
        elif species == 'r':
            headModel = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
            headModel.reparentTo(render)
            headModel.setPos(2,35,3.5)
            headModel.setHpr(180,0,0)
            return headModel
        else:
            print("Your head type doesn't exist in ToonHead.py")

    def generateHeadDetails(self, headModel, species, head_type, gender='m'):
        '''Based on the species and head type and gender, changes the head detail'''
        toonType = species + head_type # toonType is a string, basically returns something like "cls" or "cals"

        # Bears
        if toonType == 'bls': # Big Head, Small Muzzle
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'bll': # Big Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-long-neutral').show()
        elif toonType == 'bsl': # Small Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()  
        elif toonType == 'bss': # Small Head, Small Head
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()

        # Cats
        if toonType == 'cals': # Big Head, Small Muzzle

            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'call': # Big Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-long-neutral').show()           
        elif toonType == 'casl': # Small Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()            
        elif toonType == 'cass': # Small Head, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()

        # Crocodiles
        if toonType == 'crls': # Big Head, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'crll': # Big Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
            headModel.find('**/eyes-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-long').show()
            headModel.find('**/head-front-long').show()
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-long-neutral').show()           
        elif toonType == 'crsl': # Small Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()            
        elif toonType == 'crss': # Small Head, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
            headModel.find('**/eyes-long').hide()
            headModel.find('**/joint_pupilL_long').hide()
            headModel.find('**/joint_pupilR_long').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/head-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()
    
    def removeHead(self):
        self.head_model.getChildren().detach()


