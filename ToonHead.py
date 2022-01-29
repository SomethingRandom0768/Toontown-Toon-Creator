from direct.actor.Actor import Actor
from panda3d.core import NodePath

class ToonHead:
#TODO NEED TO REWRITE IT TO WHERE THE SPECIES WILL AFFECT THE MODEL OF THE HEAD SHOWN. 
#THE SLICE OF THE STRING THAT REPRESENTS THE MUZZLE AND THE HEAD SIZE WILL BE USED TO HIDE AND SHOW BITS AND PIECES.
    def __init__(self, species, headType, hasEyelashes, gender='m'):
        '''Species - what species the toon is
           Type - What type of head are we going for (what head type and muzzle type?)
        '''

        # generateHead creates the specific species head model, generateHeadDetails changes the head size and the muzzle size
        self.head_model = self.generateHead(species)
        self.generateHeadDetails(self.head_model, species, headType, hasEyelashes)

    def generateHead(self, species, headType=None):
        '''Generates the head model based on the species. Passes headType and gender to the details function.
        Use headType only for dogs.'''

        # All the bears
        if species == 'b': 
            headModel = loader.loadModel('phase_3/models/char/bear-heads-1000.bam')
        # All the cats
        elif species == 'ca':
            headModel = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
        # All the crocodiles
        elif species == 'cr':
            headModel = loader.loadModel('phase_3/models/char/crocodile-heads-1000.bam')
        # All the deers
        elif species == 'de':
            headModel = loader.loadModel('phase_3/models/char/deer-heads-1000.bam')
        # All the dogs (WIP)
        #elif species == 'do'
        # All the ducks
        elif species == 'du':
            headModel = loader.loadModel('phase_3/models/char/duck-heads-1000.bam')
        # All the horses
        elif species == 'h':
            headModel = loader.loadModel('phase_3/models/char/horse-heads-1000.bam')
        # All the monkeys
        elif species == 'mo':
            headModel = loader.loadModel('phase_3/models/char/monkey-heads-1000.bam')
        # All the mice
        elif species == 'mi':
            headModel = loader.loadModel('phase_3/models/char/mouse-heads-1000.bam')
        # All the pigs
        elif species == 'p':
            headModel = loader.loadModel('phase_3/models/char/pig-heads-1000.bam')
        # All the rabbits
        elif species == 'r':
            headModel = loader.loadModel('phase_3/models/char/rabbit-heads-1000.bam')
        # If someone wants riggy.
        elif species == 'ri':
            headModel = loader.loadModel('phase_3/models/char/tt_a_chr_rgy_shorts_head_1000.bam')
        else:
            print("Your head type doesn't exist in ToonHead.py")
    
        return headModel

    def generateHeadDetails(self, headModel, species, head_type, has_eyelashes):
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
        elif toonType == 'cals': # Big Head, Small Muzzle

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
        elif toonType == 'crls': # Big Head, Small Muzzle
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
            headModel.find('**/muzzle-long-neutral').show()            
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
    
        # Deers
        elif toonType == 'dels': # Big Antlers, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/antlers-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/antlers-long').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'dell': # Big Antlers, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/antlers-short').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/antlers-long').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-long-neutral').show()     
        elif toonType == 'desl': # Small Antlers, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/antlers-long').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-long-surprise').hide()
            headModel.find('**/muzzle-long-sad').hide()
            headModel.find('**/muzzle-long-smile').hide()
            headModel.find('**/muzzle-long-angry').hide()
            headModel.find('**/muzzle-long-laugh').hide()

            # All the stuff we show

            headModel.find('**/antlers-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-long-neutral').show()              
        elif toonType == 'dess': # Small Antlers, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/antlers-long').hide()
            headModel.find('**/joint_pupilL_short').hide()
            headModel.find('**/joint_pupilR_short').hide()
            headModel.find('**/muzzle-short-surprise').hide()
            headModel.find('**/muzzle-short-sad').hide()
            headModel.find('**/muzzle-short-smile').hide()
            headModel.find('**/muzzle-short-angry').hide()
            headModel.find('**/muzzle-short-laugh').hide()

            # All the stuff we show

            headModel.find('**/antlers-short').show()
            headModel.find('**/head-front-short').show()
            headModel.find('**/ears-short').show()
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()     
        
        # Dogs (Need to hold off considering they have different models.)

        # Ducks 
        elif toonType == 'duls': # Big Head, Small Muzzle

            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
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
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'dull': # Big Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
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
            headModel.find('**/eyes-long').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-long-neutral').show()           
        elif toonType == 'dusl': # Small Head, Big Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
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
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()            
        elif toonType == 'duss': # Small Head, Small Muzzle
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
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
            headModel.find('**/eyes-short').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()

        # Horses
        elif toonType == 'hls': # Big Head, Small Muzzle
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
        elif toonType == 'hll': # Big Head, Big Muzzle
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
        elif toonType == 'hsl': # Small Head, Big Muzzle
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
            headModel.find('**/muzzle-long-neutral').show()   
        elif toonType == 'hss': # Small Head, Small Muzzle 
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

        # Monkeys
        elif toonType == 'mols': # Big Head, Small Muzzle
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
        elif toonType == 'moll': # Big Head, Big Muzzle
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
        elif toonType == 'mosl': # Small Head, Big Muzzle
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
            headModel.find('**/muzzle-long-neutral').show() 
        elif toonType == 'moss': # Small Head, Small Muzzle
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

        # Mice (thank goodness they only have 2 types)
        elif toonType == 'mils': # Big Head, Small Muzzle
            # All the stuff we hide
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
        elif toonType == 'miss': # Small head, Small Muzzle
            # All the stuff we hide
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

        # Pigs
        elif toonType == 'pls': # Big Head, Small Muzzle
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
        elif toonType == 'pll': # Big Head, Big Muzzle
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
        elif toonType == 'psl': # Small Head, Big Muzzle
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
            headModel.find('**/muzzle-long-neutral').show() 
        elif toonType == 'pss': # Small Head, Small Muzzle
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

        # Rabbits
        elif toonType == 'rls':
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
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
            headModel.find('**/eyes').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-short-neutral').show()
        elif toonType == 'rll':
        # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-short').hide()
            headModel.find('**/head-front-short').hide()
            headModel.find('**/ears-short').hide()
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
            headModel.find('**/eyes').show()
            headModel.find('**/joint_pupilL_long').show()
            headModel.find('**/joint_pupilR_long').show()
            headModel.find('**/muzzle-long-neutral').show() 
        elif toonType == 'rsl':
            # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-short*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-short').hide()
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
            headModel.find('**/ears-long').show()
            headModel.find('**/eyes').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show() 
        elif toonType == 'rss':
          # All the stuff we hide
            muzzleToRemove = headModel.findAllMatches('**/muzzle-long*')
            for piece in muzzleToRemove:
                piece.hide()
            headModel.find('**/head-long').hide()
            headModel.find('**/head-front-long').hide()
            headModel.find('**/ears-long').hide()
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
            headModel.find('**/eyes').show()
            headModel.find('**/joint_pupilL_short').show()
            headModel.find('**/joint_pupilR_short').show()
            headModel.find('**/muzzle-short-neutral').show()    

        # Generate the eyelashes if wanted
        if has_eyelashes:
            self.createEyelashes(species, head_type)
        else:
            pass
    
    def createEyelashes(self, species, head_type):
        '''Creates eyelash model based on species and head type'''

        if species == 'b' and head_type[0] == 'l':  # Bear and long head
            eyelashes = loader.loadModel('phase_3/models/char/bear-lashes.bam').find('**/open-long')
        elif species == 'b' and head_type[0] == 's': # Bear and small head
            eyelashes = loader.loadModel('phase_3/models/char/bear-lashes.bam').find('**/open-short')

        elif species == 'ca' and head_type[0] == 'l': # Cat and long head
            eyelashes = loader.loadModel('phase_3/models/char/cat-lashes.bam').find('**/open-long')
        elif species == 'ca' and head_type[0] == 's': # Cat and short head
            eyelashes = loader.loadModel('phase_3/models/char/cat-lashes.bam').find('**/open-short')

        elif species == 'cr' and head_type[0] == 'l': # Crocodile and long head
            eyelashes = loader.loadModel('phase_3/models/char/crocodile-lashes.bam').find('**/open-long')
        elif species == 'cr' and head_type[0] == 's': # Crocodile and short head
            eyelashes = loader.loadModel('phase_3/models/char/crocodile-lashes.bam').find('**/open-short')
        
        elif species == 'de': # Deers only have one type of head, though they have eyelashes even for long heads, whichever those were. Interesting.
            eyelashes = loader.loadModel('phase_3/models/char/deer-lashes.bam').find('**/open-short')
        
        elif species == 'du' and head_type[0] == 'l': # Ducks and long head
            eyelashes = loader.loadModel('phase_3/models/char/duck-lashes.bam').find('**/open-long')
        elif species == 'du' and head_type[0] == 's': # Ducks and short head
            eyelashes = loader.loadModel('phase_3/models/char/duck-lashes.bam').find('**/open-short')
        
        elif species == 'h' and head_type[0] == 'l': # Horse and long head
            eyelashes = loader.loadModel('phase_3/models/char/horse-lashes.bam').find('**/open-long')
        elif species == 'h' and head_type[0] == 's': # Horse and short head
            eyelashes = loader.loadModel('phase_3/models/char/horse-lashes.bam').find('**/open-short')

        elif species == 'mo' and head_type[0] == 'l': # Monkey and long head
            eyelashes = loader.loadModel('phase_3/models/char/monkey-lashes.bam').find('**/open-long')
        elif species == 'mo' and head_type[0] == 's': # Monkey and short head
            eyelashes = loader.loadModel('phase_3/models/char/monkey-lashes.bam').find('**/open-short')
        
        elif species == 'mi' and head_type[0] == 'l': # Mouse and long head
            eyelashes = loader.loadModel('phase_3/models/char/mouse-lashes.bam').find('**/open-long')
        elif species == 'mi' and head_type[0] == 's': # Mouse and short head
            eyelashes = loader.loadModel('phase_3/models/char/mouse-lashes.bam').find('**/open-short')

        elif species == 'p' and head_type[0] == 'l': # Pig and long head
            eyelashes = loader.loadModel('phase_3/models/char/mouse-lashes.bam').find('**/open-long')
        elif species == 'p' and head_type[0] == 's': # Pig and short head
            eyelashes = loader.loadModel('phase_3/models/char/mouse-lashes.bam').find('**/open-short')
        elif species == 'r': # Since rabbits only have one type of eyes
            eyelashes = loader.loadModel('phase_3/models/char/rabbit-lashes.bam').find('**/open-short')

        # I have to make some changes here to make sure deers can work since they don't have different head types, only antler types.

        if head_type[0] == 'l' and species != 'de' and species != 'ri' and species != 'r':
            eyelashes.reparentTo(self.head_model.find('**/eyes-long'))
        elif head_type[0] == 's' and species != 'de' and species != 'ri' and species != 'r':
            eyelashes.reparentTo(self.head_model.find('**/eyes-short'))
        elif species == 'de':
            eyelashes.reparentTo(self.head_model.find('**/eyes-short'))
        elif species == 'r':
            eyelashes.reparentTo(self.head_model.find('**/eyes'))
        elif species == 'ri':
            print("There are no eyelashes for Riggy!!!!!")

    def removeHead(self):
        self.head_model.getChildren().detach()


