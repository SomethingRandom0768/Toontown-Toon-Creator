# THIS FILE CONTAINS ALL THE DICTIONARIES USED FOR THE CHOOSING MENUS IN OPTIONSMENU.PY
from panda3d.core import *

colorsList = {
    'Amber'         :VBase4(0.9647058823529412,0.7490196078431373,0.34901960784313724, 1.0),
    'Apricot'       :VBase4(0.9803921568627451,0.5372549019607843,0.396078431372549, 1.0),                  
    'Aqua'          :VBase4(0.347656, 0.820312, 0.953125, 1.0),
    'Beige'         :VBase4(0.8,0.7529411764705882,0.611764705882353, 1.0),   
    'Black'         :VBase4(0.3, 0.3, 0.35, 1.0),
    'Blue'          :VBase4(0.191406, 0.5625, 0.773438, 1.0), 
    'Bright Red'   : VBase4(0.933594, 0.265625, 0.28125, 1.0),
    'Brown'        : VBase4(0.640625, 0.355469, 0.269531, 1.0),
    'Bubblegum'    : VBase4(0.996078431372549,0.35294117647058826,0.44313725490196076, 1.0),
    'Cartoonival Blue': VBase4(0.22745098039, 0.55686274509, 0.96862745098, 1.0),
    'Cartoonival Pink': VBase4(0.93333333333, 0.36470588235,0.81568627451, 1.0 ),  
    'Citrine'       :VBase4(0.855469, 0.933594, 0.492188, 1.0),  
    'Coral'        : VBase4(0.832031, 0.5, 0.296875, 1.0), 
    'Cream'         :VBase4(0.996094, 0.957031, 0.597656, 1.0),
    'Crimson'       :VBase4(0.6549019607843137,0.17647058823529413,0.25882352941176473, 1.0),
    'Emerald'       :VBase4(0.0392156862745098,0.8627450980392157,0.6549019607843137, 1.0),
    'Forest Green'  :VBase4(0.4117647058823529,0.6431372549019608,0.2823529411764706, 1.0),
    'Gray'          :VBase4(0.7, 0.7, 0.8, 1.0),
    'Green'         :VBase4(0.304688, 0.96875, 0.402344, 1.0),
    'Ice Blue'      :VBase4(0.7333333333333333,0.8666666666666667,0.9490196078431372, 1.0), 
    'Lavender'      :VBase4(0.726562, 0.472656, 0.859375, 1.0),
    'Lime Green'    :VBase4(0.550781, 0.824219, 0.324219, 1.0), 
    'Light Blue'    :VBase4(0.433594, 0.90625, 0.835938, 1.0),      
    'Maroon'       : VBase4(0.710938, 0.234375, 0.4375, 1.0),
    'Mint Green'    :VBase4(0.6392156862745098,0.8549019607843137,0.6705882352941176, 1.0),
    'Orange'        :VBase4(0.992188, 0.480469, 0.167969, 1.0),         
    'Peach'        : VBase4(0.96875, 0.691406, 0.699219, 1.0),
    'Periwinkle'    :VBase4(0.558594, 0.589844, 0.875, 1.0),   
    'Pink'          :VBase4(0.898438, 0.617188, 0.90625, 1.0),
    'Purple'        :VBase4(0.546875, 0.28125, 0.75, 1.0),
    'Red'          : VBase4(0.863281, 0.40625, 0.417969, 1.0),
    'Rose Pink'     :VBase4(0.8823529411764706, 0.43529411764705883, 0.6901960784313725, 1.0),                          
    'Royal Blue'    :VBase4(0.285156, 0.328125, 0.726562, 1.0),
    'Sea Green'     :VBase4(0.242188, 0.742188, 0.515625, 1.0),
    'Sienna'       : VBase4(0.570312, 0.449219, 0.164062, 1.0),        
    'Slate Blue'    :VBase4(0.460938, 0.378906, 0.824219, 1.0),
    'Spooky Purple' :VBase4(0.35294117647, 0.23137254902, 0.51372549019, 1.0),
    'Steel Blue'    :VBase4(0.3254901960784314,0.403921568627451,0.6, 1.0), 
    'Tan'          : VBase4(0.996094, 0.695312, 0.511719, 1.0),
    'Teal'          :VBase4(0.19607843137254902,0.7215686274509804,0.7098039215686275, 1.0),
    'White'        : VBase4(1.0, 1.0, 1.0, 1.0),    
    'Yellow'        :VBase4(0.996094, 0.898438, 0.320312, 1.0),              
}

species_dict = {
             'Bear'         :'b',
             'Cat'          :'ca',
             'Crocodile'    :'cr',
             'Deer'         :'de',
             'Dog '         :'d',
             'Duck'         :'du',
             'Horse'        :'h',
             'Monkey'       :'mo',
             'Mouse'        :'mi',
             'Pig'          :'p',
             'Rabbit'       :'r',
             'Riggy'        :'ri'
              }
# How does this work?
# "Animation Name" - "file_of_animation"

anim_dict = {
    'Angry'    : 'angry',
    'Applause' : 'applause',
    'begCycle' : 'begCycle',
    'begOut'   : 'begOut',
    'Book'     : 'book',
    'Bored'    : 'bored',
    'Bow'      : 'bow',
    'Cast'     : 'cast',
    'Cast(Long)': 'castlong',
    'Climb'    : 'climb',
    'Confused' : 'confused',
    'Cringe'   : 'cringe',
    'Curtsy'   : 'curtsy',
    'Down'     : 'down',
    'Duck'     : 'duck',
    'Eat(Neutral)': 'eat_neutral',
    'Eat N\' Run' : 'eatnrun',
    'Firehose' : 'firehose',
    'Fish again': 'fishAGAIN',
    'Fish'     : 'fish',
    'Fish End' : 'fishEND',
    'Fish (neutral)': 'fishneutral',
    'Flashlight' : 'flashlight',
    'Game Neutral': 'gameneutral',
    'Game Run'  : 'gamerun',
    'Game Throw': 'gameThrow',
    'Give'      : 'give',
    'Happy Dance' : 'happy-dance',
    'Hold Bottle' : 'hold-bottle',
    'Hold Magnet' : 'hold-magnet',
    'Hypnotize' : 'hypnotize',
    'into Beg'  : 'intoBeg',
    'into Sit'  : 'intoSit',
    'Juggle'    : 'juggle',
    'Left'      : 'left',
    'Left Point': 'left-point',
    'Lose'      : 'lose',
    'Lose Walk' : 'losewalk',
    'Melt'      : 'melt',
    'Neutral'   : 'neutral',
    'Pie Throw' : 'pie-throw',
    'Pole'      : 'pole',
    'Pole (Neutral)' : 'poleneutral',
    'Press Button' : 'press-button',
    'Remote Attack' : 'remoteAttack',
    'Riggy Neutral': 'riggyNeutral',
    'Riggy Walk': 'riggyWalk',
    'Run'       : 'run',
    'Sad(Neutral)' : 'sad-neutral',
    'Scientist (Emcee)' : 'scientistEmcee',
    'Scientist (Jealous)' : 'scientistJealous',
    'Scientist (Work)' : ' scientistWork',
    'Shrug'         : 'shrug',
    'Sit'           : 'sit',
    'Skate (Boost)' : 'skateBoost',
    'Skate (Brake)' : 'skateBrake',
    'Skate (Run)'  : 'skateRun',
    'Side Step (Left)' : 'sidestep-left', 
    'Spit'      : 'spit',
    'Sprinkle'  : 'sprinkle-dust',
    'Struggle'  : 'struggle',
    'Surprise'  : 'surprise',
    'Swim'      : 'swim',
    'Swing'     : 'swing',
    'Teleport'  : 'teleport',
    'Think'     : 'think',
    'Victory Dance' : 'victory-dance',
    'Walk'      : 'walk',
    'Water Gun' : 'water-gun',
    'Wave'      : 'wave',

}

# Backpack model, (potentially texture if reskin), (potentially what to retexture), small scale, medium scale, large scale, accessory scale

backpack_dict = {
    'A Broken Jetpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_jetPack.bam', (0,-0.5,1), (0,-0.2,1), (0,-0.32,1.5), 0.32],
    'Angel Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_angelWings.bam', (0,-0.5,0.7), (0,-0.2,0.7), (0,-0.32,1.5), 0.3],
    'The Attack Pack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_gags.bam', (0,-0.5,0.7), (0,-0.5,0.7), (0,-0.5,1.5), 0.32],
    #'Banana Bowtie':
    'Basic Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', (0,-0.7,0.7), (0,-0.5,0.7), (0,-0.5,1.5), 0.32],
    'Bat Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_batWings.bam',(0,-0.5,0.7), (0,-0.2,0.7), (0,-0.32,1.5), 0.3],
#    'Bear Backpack': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam',
#    'Bee Wings': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_beeWings.bam',
#    'Bird Wings': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_birdWings.bam',
#    'Blue Backpack': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackDog.bam',
   # 'Blue Winter Scarf':
#    'Butterfly Wings': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_butterflyWings.bam',
  #  'Carrot Bowtie':
  #  'Chocolate Bowtie'
  #  'Crazy Bowtie'
#    'Dragon Fly Wings': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonFlyWings.bam',
#    'Dragon Wings': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonWing.bam',
    #'Dreamland Bowtie'
#    'Emergency Cream Pack': 'phase_4/models/accessories/ttr_m_chr_avt_acc_pac_creamPack.bam',
#    'Emergency Seltzer': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_scubaTank.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_seltzerTank.jpg' ],
    #'Extraordinaire Bowtie'
#    'Fairy Wings': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_butterflyWings.bam', 'phase_4/maps/tt_t_chr_avt_acc_pac_butterflyWingsStyle1.jpg'],
#    'The Flunk-Trunk': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_flunky.bam',
    #'Green Fancy Bowtie'
    #'Green Fancy Scarf'
    #'Holiday Scarf'
#    'Infinity and Beyond Backpack': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_airplane.bam',
#    'Jellybean Bag': 'phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam',
#    'Kitty Kit': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackCat.bam',
#    'Lipstick Jetpack': 'phase_4/models/accessories/ttr_m_chr_avt_acc_pac_lipstickPack.bam',
   # 'Melodyland Bowtie'
#    'Oil Pale Pack': 'phase_4/models/accessories/ttr_m_chr_avt_acc_pac_oilJar.bam',
#    'One-Toon Band': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_band.bam',
    #'Orange Knapsack'
    #'Pink Water Scarf'
#    'Pirate Sword': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_woodenSword.bam',
    #'Polka Bowtie'
    #'Portable Blanket'
    #'Purple Fancy Bowtie'
    #'Purple Pouch'
    #'Rainbow Scarf'
    #'Rainbow Wings'
    #'Red Bowtie'
    #'Red Fancy Bowtie'
    #'Red Polka-pack'
    #'Resistance Cape'
#    "Santa's Bag": 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_santa.bam',
#    'Scuba Tank': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_scubaTank.bam',
#    'Shark Fin': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_sharkFin.bam',
    #'Sly Scarf'
    #'Soft Scarf'
#    'Spider Legs': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_spiderLegs.bam',
    #'Starry Bowtie'
    #'Strawberry Bowtie'
    #'Strawberry Cape'
#    "SuperToon's Cape": 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape.bam',
    #'Teal Bowtie'
#    'Token Tote': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam','phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTokens.jpg'],
#    'ToonFest 2016 Blue Attendee Backpack':['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_stuffedAnimalBackpackTFBlue.jpg'],
#    'ToonFest 2016 Blue Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_backpackTFBlue.jpg'],
#    'ToonFest 2016 Pink Attendee Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_stuffedAnimalBackpackTFPink.jpg'],
#    'ToonFest 2016 Pink Backpack': ['phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack.bam', 'phase_4/maps/ttr_t_chr_avt_acc_pac_backpackTFPink.jpg'],
#    'Toonosaur Tail': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dinosaurTail.bam',
    #'Trainee Travel Pack'
#    'Treasure Trove': ['phase_4/models/accessories/ttr_m_chr_avt_acc_pac_jellybeanJar.bam', 'phase_4/maps/ttr_t_avt_acc_pac_jellybeanJarTreasures.jpg'],
#    'Vampire Cloak': 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_vampireCape.bam'
    #'Vanilla Bowtie'
    #'Yellow Polka-pack'
}