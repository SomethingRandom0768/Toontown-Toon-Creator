################################
#
#
#       This file contains all the methods
#       meant for Toons
#
################################

from gui.EditorMenu import *
from toon.ToonDNA import *
from direct.directnotify import DirectNotifyGlobal

class ToonEditorMenu(EditorMenu):
    '''Houses the menu for Toons'''

    def __init__(self, toon):

        self.notify = DirectNotifyGlobal.directNotify.newCategory('ToonEditorMenu')
        self.notify.setDebug(1)

        super().__init__()
        self.menuLabel['text'] = 'Toon Creator'
        self.icon = loader.loadModel('phase_3/models/gui/toontown-logo.bam')
        self.toontaskicons = loader.loadModel(
            'phase_3.5/models/gui/ttr_m_gui_qst_toontask_icons.bam')


        self.selectedToon = toon

        self.hidingButton = DirectGui.DirectButton(self.menuFrame,
        frameSize=(-0.15, 1.85, -0.75, 0.75),
        command=self.hideSelectables,
        pos=(0,2.5,0),
        frameColor=(0,0,0,0.1)
        )


# Contains all the modals

        self.rotation_slider = OptionsSlider(
            aspect2d, '', -0.80, self.rotateToon, (0, 360))
        self.rotation_slider.containerFrame.setX(-1.75)
        self.rotation_slider.slider.setX(1.15)
        self.rotation_slider.slider['value'] = 180
        self.rotateToon()

# FIRST PAGE

        self.toonDNALabel = OptionsLabel(
            self.firstPageOptionsScroll.getCanvas(), 'Toon DNA',  0.8)
        self.head_slider = OptionsSlider(
            self.firstPageOptionsScroll.getCanvas(), 'Head:', 0.65, self.updateHead)
        self.torso_slider = OptionsSlider(
            self.firstPageOptionsScroll.getCanvas(), 'Torso:', 0.50, self.updateTorso)
        self.legs_slider = OptionsSlider(
            self.firstPageOptionsScroll.getCanvas(), 'Legs:', 0.35, self.updateLegs)
        self.eyelash_toggle = OptionsToggle(
            self.firstPageOptionsScroll.getCanvas(), 'Eyelashes:', 0.20, self.eyelashToggle)
        self.bottomType = OptionsToggle(
            self.firstPageOptionsScroll.getCanvas(), 'Short/Skirt:', 0.05, self.changeBottomType)
        self.smoothanim_toggle = OptionsToggle(
            self.firstPageOptionsScroll.getCanvas(), 'Smooth Animation:', -0.1, self.smoothanimationToggle)
        self.shoes_toggle = OptionsToggle(
            self.firstPageOptionsScroll.getCanvas(), 'Shoes:', -0.25, self.shoesToggle)

        self.glove_color_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Gloves Color:', 0, -1.4, 10, colorsList, self.updateGloveColor, 0)
        self.leg_color_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Leg Color:', 0, -1.2, 10, colorsList, self.updateLegsColor, 0)
        self.arm_color_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Arms Color:', 0, -1, 10, colorsList, self.updateArmsColor, 0)
        self.head_color_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Head Color:', 0, -0.8, 10, colorsList, self.updateHeadColor, 0)
        self.anim_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Animation:', 0, -0.6, 20, anim_dict, self.updateAnim)
        self.species_menu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Species:', 0, -0.4, 10, species_dict, self.updateSpecies)



# SECOND PAGE

        self.clothingLabel = OptionsLabel(
            self.secondPageOptionsScroll.getCanvas(), 'Clothing',  0.8)
        self.bottom_coloring_menu = OptionsChoosingMenu(self.secondPageOptionsScroll.getCanvas(
        ), 'Bottom Color:', 0, -0.2, 10, colorsList, self.updateBottomColor, 0)
        self.skirts_menu = OptionsChoosingMenu(self.secondPageOptionsScroll.getCanvas(
        ), 'Skirt:', 0, 0, 20, skirt_dict, self.updateSkirtTexture, 0)
        self.shorts_menu = OptionsChoosingMenu(self.secondPageOptionsScroll.getCanvas(
        ), 'Shorts:', 0, 0.2,  20, short_dict, self.updateShortTexture, 0)
        self.shirt_color_menu = OptionsChoosingMenu(self.secondPageOptionsScroll.getCanvas(
        ), 'Shirt Color:', -0.1, 0.4, 10, colorsList, self.updateShirtColor, 0)
        self.shirt_menu = OptionsChoosingMenu(self.secondPageOptionsScroll.getCanvas(
        ), 'Shirt:', -0.2, 0.6, 25, shirt_dict, self.updateShirtTexture, 0)


# THIRD PAGE

        self.accessoryLabel = OptionsLabel(
            self.thirdPageOptionsScroll.getCanvas(), 'Accessories',  0.8)

        self.shoes_switching_slider = OptionsSlider(
            self.thirdPageOptionsScroll.getCanvas(), 'Shoe Type:', -0.4, self.updateShoes)

        self.shoes_texture_menu = OptionsChoosingMenu(self.thirdPageOptionsScroll.getCanvas(
        ), 'Shoes:', 0, -0.2, 22, shoe_texture_dict, self.updateShoeTexture, 0)

        self.boot_short_texture_menu = OptionsChoosingMenu(self.thirdPageOptionsScroll.getCanvas(
        ), 'Short Boot:', 0, 0, 22, shoe_texture_dict, self.updateShortBootTexture, 0)

        self.boot_long_texture_menu = OptionsChoosingMenu(self.thirdPageOptionsScroll.getCanvas(
        ), 'Long Boot:', 0, 0.2, 15, boot_long_texture_dict, self.updateLongBootTexture, 0)

        self.glasses_menu = OptionsChoosingMenu(self.thirdPageOptionsScroll.getCanvas(
        ), 'Glasses:', -0.1, 0.4, 22, glasses_dict, self.updateGlasses, 0)

        self.backpack_menu = OptionsChoosingMenu(self.thirdPageOptionsScroll.getCanvas(
        ), 'Backpack:', -0.1, 0.6, 23, backpack_dict, self.updateBackpack, 0)

# FOURTH PAGE

        self.accessoryLabel = OptionsLabel(
            self.fourthPageOptionsScroll.getCanvas(), 'Miscellaneous',  0.8)

        generateButtonGeom = self.optionsGeom.find('**/*ttr_t_gui_gen_buttons_squareButton')

        self.generateToonButton = DirectButton(
            parent = self.fourthPageOptionsScroll.getCanvas(),
            geom = generateButtonGeom,
            pos = (-0.25,0,0.6),
            scale=0.2,
            text='Generate Toon',
            text_scale=0.35,
            text_font = self.modalFont,
            relief=None,
            command=self.generateToon,
            clickSound=self.guiClickSound,
            rolloverSound=self.guiRolloverSound,            

        )


# All the functions related to the ToonEditorMenu

# Toon DNA related functions

    def updateHead(self):
        '''Updates the Toon's head based on the value'''
        sliderValue = self.head_slider.slider['value']
        tested_value = int(sliderValue)

        if self.selectedToon.species == 'mi':
            if tested_value == 50:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'mi', 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value == 100:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'mi', 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
        elif self.selectedToon.species == 'd':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'sl', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 80 and tested_value > 75:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    'd', 'll', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
        else:
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'ls', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'll', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'sl', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif tested_value < 80 and tested_value > 75:
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateHead(
                    self.selectedToon.species, 'ss', self.selectedToon.eyelashes)
                self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateHeadColor(self, color_to_change_to):
        self.selectedToon.updateHeadColor(color_to_change_to)

    def updateTorso(self):
        '''Updates the Toon's torso based on the value'''
        sliderValue = self.torso_slider.slider['value']
        tested_value = int(sliderValue)

        if self.selectedToon.torso_type[1] == 's':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.updateTorso('ss')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.updateTorso('ms')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.updateTorso('ls')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
        elif self.selectedToon.torso_type[1] == 'd':
            if tested_value < 20 and tested_value > 15:
                self.selectedToon.updateTorso('sd')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 40 and tested_value > 35:
                self.selectedToon.updateTorso('md')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()
            elif tested_value < 60 and tested_value > 55:
                self.selectedToon.updateTorso('ld')
                self.selectedToon.toonActor.delete()
                self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateArmsColor(self, color_to_change_to):
        self.selectedToon.updateArmsColor(color_to_change_to)

    def updateLegs(self):
        '''Updates the Toon's legs based on the value'''
        sliderValue = self.legs_slider.slider['value']
        tested_value = int(sliderValue)

        if tested_value < 20 and tested_value > 15:
            self.selectedToon.updateLegs('s')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()
        elif tested_value < 40 and tested_value > 35:
            self.selectedToon.updateLegs('m')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()
        elif tested_value < 60 and tested_value > 55:
            self.selectedToon.updateLegs('l')
            self.selectedToon.toonActor.delete()
            self.selectedToon.generateActor()

        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def updateLegsColor(self, color_to_change_to):
        self.selectedToon.updateLegsColor(color_to_change_to)

    def updateGloveColor(self, color_to_change_to):
        self.selectedToon.updateGloveColor(color_to_change_to)

    def rotateToon(self):
        '''Updates the Toon's rotation based on the value'''
        sliderValue = self.rotation_slider.slider['value']
        tested_value = int(sliderValue)

        self.selectedToon.toonActor.setH(tested_value)

    def changeBottomType(self):
        '''Changes the toon's bottom (shorts/skirts) based on the current bottom type'''

        if self.selectedToon.torso_type[1] == 's':
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateTorso(
                self.selectedToon.torso_type[0] + 'd')
            self.selectedToon.generateActor()

        elif self.selectedToon.torso_type[1] == 'd':
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateTorso(
                self.selectedToon.torso_type[0] + 's')
            self.selectedToon.generateActor()


        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def eyelashToggle(self):
        '''Toggles the eyelashes on the Toon's head'''
        if self.selectedToon.eyelashes:
            self.selectedToon.toonActor.delete()
            self.selectedToon.eyelashes = False
            self.selectedToon.updateHead(
                self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
        elif self.selectedToon.eyelashes == False:
            self.selectedToon.toonActor.delete()
            self.selectedToon.eyelashes = True
            self.selectedToon.updateHead(
                self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])

    def smoothanimationToggle(self):
        if self.selectedToon.smooth_enabled:
            self.selectedToon.toonActor.setBlend(frameBlend=False)
            self.selectedToon.smooth_enabled = False
        else:
            self.selectedToon.toonActor.setBlend(frameBlend=True)
            self.selectedToon.smooth_enabled = True

    def shoesToggle(self):
        if self.selectedToon.wearsShoes:
            self.selectedToon.toonActor.find('**/*boots_short').hide()
            self.selectedToon.toonActor.find('**/*boots_long').hide()
            self.selectedToon.toonActor.find('**/*shoes').hide()
            self.selectedToon.toonActor.find('**/*feet').show()
            self.selectedToon.wearsShoes = False
        else:
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
            self.selectedToon.wearsShoes = True

    def updateSpecies(self, species):
        '''Updates the Toon's species'''
        self.selectedToon.toonActor.delete()
        self.selectedToon.updateSpecies(species)
        self.selectedToon.updateHead(
            self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
        self.selectedToon.generateActor()
        self.selectedToon.toonActor.setH(
            self.rotation_slider.slider['value'])
        self.notify.debug(f"Species has been changed to {species}")

    def updateAnim(self, anim):
        self.selectedToon.animationType = anim
        self.selectedToon.toonActor.stop()
        self.selectedToon.toonActor.loop(anim)
        self.notify.debug(f"Animation has been changed to {anim}")

# Accessory related functions

    def updateBackpack(self, backpack_type):
        self.selectedToon.backpack_type = backpack_type
        self.selectedToon.attachBackpack(backpack_type)

        self.backpackXEntry.set( str( round( self.selectedToon.returnBackpackPosition().getX(), 2 ) ) )
        self.backpackYEntry.set( str( round( self.selectedToon.returnBackpackPosition().getY(), 2 ) ) )
        self.backpackZEntry.set( str( round( self.selectedToon.returnBackpackPosition().getZ(), 2 ) ) )
        self.backpackScaleEntry.set(f"{ round(self.selectedToon.backpack_model.getScale().getX(), 2) } ")

        self.notify.debug(f"Backpack has been changed to {backpack_type}")

    def updateBackpackXPos(self, xPosition):
        self.selectedToon.backpack_model.setX(float(xPosition))

    def updateBackpackYPos(self, yPosition):
        self.selectedToon.backpack_model.setY(float(yPosition))

    def updateBackpackZPos(self, zPosition):
        self.selectedToon.backpack_model.setZ(float(zPosition))

    def updateBackpackScale(self, newScale):
        self.selectedToon.backpack_model.setScale(float(newScale))

    def updateGlasses(self, glasses_type):
        self.selectedToon.glasses_type = glasses_type
        self.selectedToon.attachGlasses(glasses_type)
        
        self.glassesXEntry.set( str( round( self.selectedToon.returnGlassesPosition().getX(), 2 ) ) )
        self.glassesYEntry.set( str( round( self.selectedToon.returnGlassesPosition().getY(), 2 ) ) )
        self.glassesZEntry.set( str( round( self.selectedToon.returnGlassesPosition().getZ(), 2 ) ) )
        self.glassesScaleEntry.set(f"{ round(self.selectedToon.glasses_model.getScale().getX(), 2) } ")
        self.notify.debug(f"Glasses has been changed to {glasses_type}")

    def updateGlassesXPos(self, xPosition):
        self.selectedToon.glasses_model.setX(float(xPosition))

    def updateGlassesYPos(self, yPosition):
        self.selectedToon.glasses_model.setY(float(yPosition))

    def updateGlassesZPos(self, zPosition):
        self.selectedToon.glasses_model.setZ(float(zPosition))

    def updateGlassesScale(self, newScale):
        self.selectedToon.glasses_model.setScale(float(newScale))

# Clothing related functions

    def updateShirtTexture(self, shirt_texture):
        self.selectedToon.shirt_texture = shirt_texture
        self.selectedToon.setShirtTexture(shirt_texture)
        self.notify.debug(f"Shirt Texture has been changed to {shirt_texture}")

    def updateShortTexture(self, short_texture):
        self.selectedToon.short_texture = short_texture
        self.selectedToon.setShortTexture(short_texture)
        self.notify.debug(f"Short Texture has been changed to {short_texture}")

    def updateSkirtTexture(self, skirt_texture):
        self.selectedToon.skirt_texture = skirt_texture
        self.selectedToon.setSkirtTexture(skirt_texture)
        self.notify.debug(f"Skirt Texture has been changed to {skirt_texture}")

    def updateShirtColor(self, shirt_color):
        self.selectedToon.shirt_color = shirt_color
        self.selectedToon.setShirtColor(shirt_color)
        self.notify.debug(f"Shirt color has been changed to {shirt_color}")

    def updateBottomColor(self, bottom_color):
        self.selectedToon.bottom_color = bottom_color
        self.selectedToon.setBottomColor(bottom_color)
        self.notify.debug(f"Bottom color has been changed to {bottom_color}")

    def updateShoeTexture(self, shoe_texture):
        try:
            self.selectedToon.shoe_texture = shoe_texture
            self.selectedToon.applyShoeTexture(shoe_texture)
            self.notify.debug(f"Shoe has been changed to {shoe_texture}")
        except:
            pass

    def updateShortBootTexture(self, shoe_texture):
        try:
            self.selectedToon.short_boot_texture = shoe_texture
            self.selectedToon.applyShortBootTexture(shoe_texture)
            self.notify.debug(f"Short Boots has been changed to {shoe_texture}")
        except:
            pass

    def updateLongBootTexture(self, shoe_texture):
        try:
            self.selectedToon.long_boot_texture = shoe_texture
            self.selectedToon.applyLongBootTexture(shoe_texture)
            self.notify.debug(f"Long Boots has been changed to {shoe_texture}")
        except:
            pass

    def updateShoes(self):
        """Updates the Toon's shoe type based on the thumb's position"""
        sliderValue = self.shoes_switching_slider.slider['value']
        tested_value = int(sliderValue)

        if tested_value >= 0 and tested_value <= 25:
            self.selectedToon.shoe_type = 4
            self.selectedToon.hideShoePieces()
        elif tested_value > 25 and tested_value <= 50:
            self.selectedToon.shoe_type = 1
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
        elif tested_value > 50 and tested_value <= 75:
            self.selectedToon.shoe_type = 2
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)
        else:
            self.selectedToon.shoe_type = 3
            self.selectedToon.attachShoes(self.selectedToon.shoe_type)

    def generateToon(self):
        '''Just prints out the Toon's toString'''
        self.notify.debug(self.selectedToon)

    def hideSelectables(self):
        self.shoes_texture_menu.selectablesFrame.hide()
        self.shoes_texture_menu.clickable.show()

        self.boot_short_texture_menu.selectablesFrame.hide()
        self.boot_short_texture_menu.clickable.show()

        self.boot_long_texture_menu.selectablesFrame.hide()
        self.boot_long_texture_menu.clickable.show()

        self.glasses_menu.selectablesFrame.hide()
        self.glasses_menu.clickable.show()

        self.backpack_menu.selectablesFrame.hide()
        self.backpack_menu.clickable.show()

        self.glove_color_menu.selectablesFrame.hide()
        self.glove_color_menu.clickable.show()

        self.leg_color_menu.selectablesFrame.hide()
        self.leg_color_menu.clickable.show()

        self.arm_color_menu.selectablesFrame.hide()
        self.arm_color_menu.clickable.show()

        self.head_color_menu.selectablesFrame.hide()
        self.head_color_menu.clickable.show()

        self.anim_menu.selectablesFrame.hide()
        self.anim_menu.clickable.show()

        self.species_menu.selectablesFrame.hide()
        self.species_menu.clickable.show()
        
        self.bottom_coloring_menu.selectablesFrame.hide()
        self.bottom_coloring_menu.clickable.show()

        self.skirts_menu.selectablesFrame.hide()
        self.skirts_menu.clickable.show()

        self.shorts_menu.selectablesFrame.hide()
        self.shorts_menu.clickable.show()

        self.shirt_color_menu.selectablesFrame.hide()
        self.shirt_color_menu.clickable.show()

        self.shirt_menu.selectablesFrame.hide()
        self.shirt_menu.clickable.show()

