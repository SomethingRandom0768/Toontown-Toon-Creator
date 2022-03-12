from direct.gui.DirectGuiGlobals import FLAT, HORIZONTAL, SUNKEN, VERTICAL, RAISED, GROOVE
from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, TextNode
from direct.interval.LerpInterval import *
from Toon import Toon
from ToonDNA import *
from direct.showbase.DirectObject import DirectObject
options_geom = 'phase_3/models/gui/ttr_m_gui_gen_buttons.bam'
gui_click_sound = 'phase_3/audio/sfx/GUI_create_toon_fwd.ogg'
gui_rollover_sound = 'phase_3/audio/sfx/GUI_rollover.ogg'
toon_font = 'phase_3/fonts/ImpressBT.ttf'


class OptionsMenu(DirectObject):
    '''The main OptionsMenu
       Houses the DirectFrame that is the entire frame.'''

    def __init__(self, toon):
        self.showOptions = True
        self.main_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        self.options_geom = loader.loadModel(options_geom)
        self.icon = loader.loadModel('phase_3/models/gui/toontown-logo.bam')
        self.toontaskicons = loader.loadModel(
            'phase_3.5/models/gui/ttr_m_gui_qst_toontask_icons.bam')

        self.selectedToon = toon

        self.accept('space', self.hideOrShowOptions)
        # Removing nodes that aren't needed

        stuffToDelete1 = self.main_geom.find('**/*tabInactive')
        stuffToDelete1.removeNode()
        stuffToDelete2 = self.main_geom.find('**/*tabActive3')
        stuffToDelete2.removeNode()
        stuffToDelete3 = self.main_geom.find('**/*tabActive4')
        stuffToDelete3.removeNode()

        # Geom to get DirectFrames for.

        self.outer_page_geom = self.main_geom.find('**/*panelMain')
        self.first_page_geom = self.main_geom.find('**/*tabActive1')
        self.second_page_geom = self.main_geom.find('**/*tabActive2')

        self.slider_geom = self.options_geom.find('**/*slider1')
        self.trough_geom = self.options_geom.find('**/*lineThick')

        # There'll be nothing here, it's just the outer frame

        self.outer_page = DirectGui.DirectFrame(
            frameSize=(0, 0, 0, 0),
            geom=self.outer_page_geom,
            geom_scale=0.15,
            parent=aspect2d,
            sortOrder=3,
            pos=(0.8, 0, 0)
        )

        # First page, this'll be where the Toon controller is

        self.first_page = DirectGui.DirectFrame(
            parent=self.outer_page,
            geom=self.first_page_geom,
            geom_scale=0.15,
            geom_pos=(0, 0, 0.1),
            frameColor=(0, 0, 0, 0)
        )

        label_outer_font = loader.loadFont(
            'phase_3/fonts/MickeyFontMaximum.bam')

        self.label_inner_text = OnscreenText(text='Toon Creator',
                                             parent=self.first_page,
                                             font=label_outer_font,
                                             fg=(0.28, 0.75111111111,
                                                 1.08888888889, 1),
                                             scale=0.175,
                                             pos=(0, 0.4)
                                             )

        # First Tab related stuff

        self.firstTabGeom = self.icon.find('**/*eyes')

        def funnyFunction():
            print("You clicked on a button that has no function yet..or does it? Only time will tell......just kidding, I'm tired.\nIf you found this, I'd like a cookie, preferably chocolate chip.")

        self.first_Tab = DirectGui.DirectButton(
            geom=self.firstTabGeom,
            geom_scale=0.045,
            geom_pos=(-0.6, 0, 0.680),
            parent=self.first_page,
            command=funnyFunction,
            frameColor=(0, 0, 0, 0))

        self.optionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.first_page,
            # GUI of the box
            frameSize=(-0.8, 0.85, -0.55, 0.35),
            canvasSize=(-1, 0, -5, 1),
            frameColor=(0, 0, 0, 0),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            verticalScroll_thumb_geom=self.slider_geom,
            verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=loader.loadSfx(gui_click_sound),
            verticalScroll_thumb_rolloverSound=loader.loadSfx(
                gui_rollover_sound),

            # The (invisible) bar you slide across.
            verticalScroll_relief=None,
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_pos=(0.80, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            scrollBarWidth=0.1,
        )

        def updateHead():
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

        def updateHeadColor(color_to_change_to):
            self.selectedToon.updateHeadColor(color_to_change_to)

        def updateTorso():
            '''Updates the Toon's torso based on the value'''
            sliderValue = self.torso_slider.slider['value']
            tested_value = int(sliderValue)

            if self.selectedToon.gender == 'm':
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
            elif self.selectedToon.gender == 'f':
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

        def updateArmsColor(color_to_change_to):
            self.selectedToon.updateArmsColor(color_to_change_to)

        def updateLegs():
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

        def updateLegsColor(color_to_change_to):
            self.selectedToon.updateLegsColor(color_to_change_to)

        def updateGloveColor(color_to_change_to):
            self.selectedToon.updateGloveColor(color_to_change_to)

        def rotateToon():
            '''Updates the Toon's rotation based on the value'''
            sliderValue = self.rotation_slider.slider['value']
            tested_value = int(sliderValue)

            self.selectedToon.toonActor.setH(tested_value)

        def changeGender():
            '''Changes the toon's gender based on the current gender'''
            if self.selectedToon.gender == 'm':
                self.selectedToon.gender = 'f'
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateTorso(
                    self.selectedToon.torso_type[0] + 'd')
                self.selectedToon.generateActor()
            elif self.selectedToon.gender == 'f':
                self.selectedToon.gender = 'm'
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateTorso(
                    self.selectedToon.torso_type[0] + 's')
                self.selectedToon.generateActor()

            self.selectedToon.toonActor.setH(
                self.rotation_slider.slider['value'])

        def eyelashToggle():
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

        def smoothanimationToggle():
            if self.selectedToon.smooth_enabled:
                self.selectedToon.toonActor.setBlend(frameBlend=False)
                self.selectedToon.smooth_enabled = False
            else:
                self.selectedToon.toonActor.setBlend(frameBlend=True)
                self.selectedToon.smooth_enabled = True

        def shoesToggle():
            if self.selectedToon.wearsShoes:
                self.selectedToon.toonActor.find('**/*boots_short').hide()
                self.selectedToon.toonActor.find('**/*boots_long').hide()
                self.selectedToon.toonActor.find('**/*shoes').hide()
                self.selectedToon.toonActor.find('**/*feet').show()
                self.selectedToon.wearsShoes = False
            else:
                self.selectedToon.attachShoes(self.selectedToon.shoe_type)
                self.selectedToon.wearsShoes = True

        def updateSpecies(species):
            '''Updates the Toon's species'''
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateSpecies(species)
            self.selectedToon.updateHead(
                self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
            self.selectedToon.toonActor.setH(
                self.rotation_slider.slider['value'])
            print(f"Animation has been changed to {species}")

        def updateAnim(anim):
            self.selectedToon.animationType = anim
            self.selectedToon.toonActor.stop()
            self.selectedToon.toonActor.loop(anim)
            print(f"Animation has been changed to {anim}")

        def updateBackpack(backpack_type):
            self.selectedToon.backpack_type = backpack_type
            self.selectedToon.attachBackpack(backpack_type)
            print(f"Backpack has been changed to {backpack_type}")

        def updateGlasses(glasses_type):
            self.selectedToon.glasses_type = glasses_type
            self.selectedToon.attachGlasses(glasses_type)
            print(f"Glasses has been changed to {glasses_type}")

        def updateShirtTexture(shirt_texture):
            self.selectedToon.shirt_texture = shirt_texture
            self.selectedToon.setShirtTexture(shirt_texture)
            print(f"Shirt Texture has been changed to {shirt_texture}")

        def updateShortTexture(short_texture):
            self.selectedToon.short_texture = short_texture
            self.selectedToon.setShortTexture(short_texture)
            print(f"Short Texture has been changed to {short_texture}")

        def updateSkirtTexture(skirt_texture):
            self.selectedToon.skirt_texture = skirt_texture
            self.selectedToon.setSkirtTexture(skirt_texture)
            print(f"Skirt Texture has been changed to {skirt_texture}")

        def updateShirtColor(shirt_color):
            self.selectedToon.shirt_color = shirt_color
            self.selectedToon.setShirtColor(shirt_color)
            print(f"Shirt color has been changed to {shirt_color}")

        def updateBottomColor(bottom_color):
            self.selectedToon.bottom_color = bottom_color
            self.selectedToon.setBottomColor(bottom_color)
            print(f"Bottom color has been changed to {bottom_color}")

        def updateShoeTexture(shoe_texture):
            try:
                self.selectedToon.shoe_texture = shoe_texture
                self.selectedToon.applyShoeTexture(shoe_texture)
                print(f"Shoe has been changed to {shoe_texture}")
            except:
                pass

        def updateShortBootTexture(shoe_texture):
            try:
                self.selectedToon.short_boot_texture = shoe_texture
                self.selectedToon.applyShortBootTexture(shoe_texture)
                print(f"Short Boots has been changed to {shoe_texture}")
            except:
                pass

        def updateLongBootTexture(shoe_texture):
            try:
                self.selectedToon.long_boot_texture = shoe_texture
                self.selectedToon.applyLongBootTexture(shoe_texture)
                print(f"Long Boots has been changed to {shoe_texture}")
            except:
                pass

        def updateShoes():
            """Updates the Toon's shoe type based on the thumb's position"""
            sliderValue = self.shoes_switching_slider.slider['value']
            tested_value = int(sliderValue)

            if tested_value >= 0 and tested_value <= 25:
                self.selectedToon.shoe_type = 1
                self.selectedToon.attachShoes(self.selectedToon.shoe_type)
            elif tested_value > 25 and tested_value <= 50:
                self.selectedToon.shoe_type = 2
                self.selectedToon.attachShoes(self.selectedToon.shoe_type)
            elif tested_value > 50 and tested_value <= 75:
                self.selectedToon.shoe_type = 3
                self.selectedToon.attachShoes(self.selectedToon.shoe_type)
            else:
                self.selectedToon.shoe_type = 4
                self.selectedToon.hideShoePieces()

        self.rotation_slider = OptionsSlider(
            aspect2d, '', -0.80, rotateToon, (0, 360))
        self.rotation_slider.containerFrame.setX(-1.75)
        self.rotation_slider.slider.setX(1.15)
        self.rotation_slider.slider['value'] = 180
        rotateToon()

        self.toonDNALabel = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Toon DNA',  0.8)
        self.head_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Head:', 0.65, updateHead)
        self.torso_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Torso:', 0.50, updateTorso)
        self.legs_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Legs:', 0.35, updateLegs)
        self.eyelash_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Eyelashes:', 0.20, eyelashToggle)
        self.gender_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Gender:', 0.05, changeGender)
        self.smoothanim_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Smooth Animation:', -0.1, smoothanimationToggle)
        self.shoes_toggle = OptionsToggle(
            self.optionsScroll.getCanvas(), 'Shoes:', -0.25, shoesToggle)

        self.accessory_label = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Accessories', -2.9)
        self.shoes_switching_slider = OptionsSlider(
            self.optionsScroll.getCanvas(), 'Shoe Type:', -4.1, updateShoes)
        self.shoes_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shoes:', 0, -3.9, 22, shoe_texture_dict, updateShoeTexture, 0)
        self.boot_short_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Short Boot:', 0, -3.7, 22, shoe_texture_dict, updateShortBootTexture, 0)
        self.boot_long_texture_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Long Boot:', 0, -3.5, 15, boot_long_texture_dict, updateLongBootTexture, 0)
        self.glasses_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Glasses:', -0.1, -3.3, 22, glasses_dict, updateGlasses, 0)
        self.backpack_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Backpack:', -0.1, -3.1, 23, backpack_dict, updateBackpack, 0)
        self.glove_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Gloves Color:', 0, -1.4, 10, colorsList, updateGloveColor, 0)
        self.leg_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Leg Color:', 0, -1.2, 10, colorsList, updateLegsColor, 0)
        self.arm_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Arms Color:', 0, -1, 10, colorsList, updateArmsColor, 0)
        self.head_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Head Color:', 0, -0.8, 10, colorsList, updateHeadColor, 0)
        self.anim_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Animation:', 0, -0.6, 20, anim_dict, updateAnim)
        self.species_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Species:', 0, -0.4, 10, species_dict, updateSpecies)

        self.clothing_label = OptionsLabel(
            self.optionsScroll.getCanvas(), 'Clothing', -1.7)
        self.bottom_coloring_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Bottom Color:', 0, -2.7, 10, colorsList, updateBottomColor, 0)
        self.skirts_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Skirt:', 0, -2.5, 20, skirt_dict, updateSkirtTexture, 0)
        self.shorts_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shorts:', 0, -2.3,  20, short_dict, updateShortTexture, 0)
        self.shirt_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shirt Color:', -0.1, -2.1, 10, colorsList, updateShirtColor, 0)
        self.shirt_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(
        ), 'Shirt:', -0.2, -1.9, 25, shirt_dict, updateShirtTexture, 0)

    def hideOrShowOptions(self):
        if self.showOptions:
            self.showOptions = False
            self.outer_page.hide()
            self.rotation_slider.slider.hide()
        else:
            self.showOptions = True
            self.outer_page.show()
            self.rotation_slider.slider.show()


class OptionsLabel:
    '''Used as labels for the bigger letters
    Lower Z means lower on the DirectScrolledFrame'''

    def __init__(self, labelParent, labelText, z):
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')

        self.label = DirectGui.DirectLabel(
            parent=labelParent,
            pos=(-1, 0, z),
            frameColor=(0, 0, 0, 0),
            frameSize=(0, 0.9, 0, 0.1)
        )

        self.labelText = OnscreenText(
            text=labelText,
            font=label_outer_font,
            fg=(0, 0, 0, 1),
            scale=0.1,
            align=TextNode.ALeft
        )
        self.labelText.reparentTo(self.label)


class OptionsModal(DirectGui.DirectFrame):
    '''This is the left part of any Options Modal, everything else past this class inherits from this and adds to it'''

    def __init__(self, modalParent, modalText, z):
        modal_font = loader.loadFont('phase_3/fonts/ImpressBT.ttf')

        self.containerFrame = DirectGui.DirectLabel(
            parent=modalParent,
            pos=(-0.95, 0, z),
            frameColor=(0, 0, 0, 0),
            frameSize=(-0.01, 0.9, -0.01, 0.06),
            scale=0.9,
        )

        self.modalTextNode = OnscreenText(
            align=TextNode.ALeft,
            text=modalText,
            font=modal_font
        )
        self.modalTextNode.reparentTo(self.containerFrame)


class OptionsSlider(OptionsModal):
    '''Creates a Slider which is useful for functions with arguments that include a range'''

    def __init__(self, modalParent, modalText, z, slider_command=None, given_range=(0, 100)):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left
        self.options_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.slider_thumb_geom = self.options_geom.find('**/*slider2')
        self.slider_scroll_geom = self.options_geom.find('**/*lineSkinny')

        self.slider = DirectGui.DirectSlider(
            thumb_geom=self.slider_thumb_geom,
            thumb_geom_scale=(0.4, 0.1, 0.25),
            thumb_relief=None,
            thumb_clickSound=loader.loadSfx(gui_click_sound),
            thumb_rolloverSound=loader.loadSfx(gui_rollover_sound),
            geom=self.slider_scroll_geom,
            geom_scale=0.5,
            scale=(0.3, 0.1, 0.4),
            relief=None,
            command=slider_command,
            range=given_range
        )
        self.slider.reparentTo(self.containerFrame)
        self.slider.setPos(1.3, 0, 0)


class OptionsToggle(OptionsModal):
    '''Creates a toggle that creates an off/on switch'''

    def __init__(self, modalParent, modalText, z, toggle_command=None):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left
        self.options_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.toggle_thumb_geom = self.options_geom.find('**/*toggleButton')
        self.warm_geom = self.options_geom.find('**/*toggleWarm')
        self.cold_geom = self.options_geom.find('**/*toggleCool')

        def executeFunction(self, toggle_command=None):
            if toggle_command:
                toggle_command()

            animateToggle()

        self.button = DirectGui.DirectCheckButton(
            scale=0.15,
            relief=None,
            boxImageScale=1,
            boxPlacement=('right'),
            boxImage=(self.warm_geom, self.cold_geom),
            boxRelief=None,
            pressEffect=1,
            clickSound=loader.loadSfx(gui_click_sound),
            rolloverSound=loader.loadSfx(gui_rollover_sound),
            command=executeFunction,
            extraArgs=[toggle_command]
        )

        self.button.reparentTo(self.containerFrame)
        self.button.setPos(1.25, 0, 0.025)

        # The button on the thing.
        self.toggle_thumb_geom.setScale(1)
        self.toggle_thumb_geom.setPos(0.6, 0, -0.15)
        self.toggle_thumb_geom.reparentTo(self.button)

        def animateToggle():
            if self.button['indicatorValue']:
                toggle_forward_interval = LerpPosInterval(
                    self.toggle_thumb_geom, 0.15, (1.2, 0, -0.15), (0.6, 0, -0.15))
                toggle_forward_interval.start()
            else:
                toggle_back_interval = LerpPosInterval(
                    self.toggle_thumb_geom, 0.15, (0.6, 0, -0.15), (1.2, 0, -0.15))
                toggle_back_interval.start()


class OptionsChoosingMenu(OptionsModal):
    '''modalParent - sets parent as the parent of the menu
       modalText(string) - what text does the model show?
       x(float) - What position in the x-position (left or right) do you want the menu?
       z(float) - What position in the z direction (up or down) do you want the menu?
       height_of_selectables(float) - How much space do you want in the selection menu? Lower numbers means a bigger height
       width_of_clickable(float) - How big do you want the button you click to open a selectable menu
       used_dictionary - What dictionary should this menu read from?
       chosen_command - What function does this menu run once an object in the selection menu is chosen?
       keyOrValue - 0 returns the key, 1 returns the value in the used_dictionary 
    '''

    def __init__(self, modalParent, modalText, x, z, width_of_clickable, used_dictionary=None, chosen_command=None, keyOrValue=1):
        super().__init__(modalParent, modalText, z)
        self.options_geom = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.clickable = self.generateClickableFrame(
            x, width_of_clickable, chosen_command, keyOrValue, used_dictionary)
        self.selectables = self.generateSelectablesFrame(
            x, used_dictionary, width_of_clickable)
        self.populateBoolean = False
        self.selectable_gui_font = loader.loadFont(toon_font)

    def generateClickableFrame(self,
                               x,
                               width_of_clickable,
                               function_to_execute,
                               keyOrValueNum,
                               selectables_dictionary
                               ):
        '''Creates the small frame that the player will click on'''
        dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        top_left_model = dynamicFrameFile.find('**/*topLeft')
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_right_model = dynamicFrameFile.find('**/topRight')
        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_right_model = dynamicFrameFile.find('**/*centerRight')
        bottom_left_model = dynamicFrameFile.find('**/*bottomLeft')
        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_right_model = dynamicFrameFile.find('**/*bottomRight')

        self.clickable_node = NodePath('clickable_frame_node')

        # The Top Left piece
        top_left_model.setScale(0.05)
        top_left_model.reparentTo(self.clickable_node)
        top_left_model.setPos(0, 0, 0.5)

        # The top middle piece
        top_middle_model.reparentTo(self.clickable_node)
        top_middle_model.setScale(0.05)
        top_middle_model.setPos(top_left_model.getX() +
                                0.05, 0, top_left_model.getZ())

        # The Top Middle repetitions
        for i in range(1, width_of_clickable):
            self.top_center_copy = top_middle_model.copyTo(self.clickable_node)
            self.top_center_copy.setPos(
                top_middle_model.getX()+(i*0.05), 0, top_middle_model.getZ())

        # The Top Right piece
        top_right_model.reparentTo(self.clickable_node)
        top_right_model.setScale(0.05)
        top_right_model.setPos(self.top_center_copy.getX()+0.05, 0, 0.5)

        # The Middle Left piece

        center_left_model.reparentTo(self.clickable_node)
        center_left_model.setScale(0.05)
        center_left_model.setPos(
            top_left_model.getX(), 0, top_left_model.getZ()-0.05)

        center_middle_model.reparentTo(self.clickable_node)
        center_middle_model.setScale(0.05)
        center_middle_model.setPos(
            center_left_model.getX()+0.05, 0, center_left_model.getZ())

        # The Center Middle repetitions
        for i in range(1, width_of_clickable):
            self.center_middle_copy = center_middle_model.copyTo(
                self.clickable_node)
            self.center_middle_copy.setPos(
                center_middle_model.getX()+(i*0.05), 0, center_middle_model.getZ())

        # The Center Right piece
        center_right_model.setScale(0.05)
        center_right_model.reparentTo(self.clickable_node)
        center_right_model.setPos(
            self.center_middle_copy.getX()+0.05, 0, center_middle_model.getZ())

        bottom_left_model.setScale(0.05)
        bottom_left_model.reparentTo(self.clickable_node)
        bottom_left_model.setPos(
            center_left_model.getX(), 0, center_left_model.getZ()-0.05)

        bottom_middle_model.setScale(0.05)
        bottom_middle_model.reparentTo(self.clickable_node)
        bottom_middle_model.setPos(
            bottom_left_model.getX()+0.05, 0, center_left_model.getZ()-0.05)

        # The Bottom Middle repetitions
        for i in range(1, width_of_clickable):
            self.bottom_middle_copy = bottom_middle_model.copyTo(
                self.clickable_node)
            self.bottom_middle_copy.setPos(
                bottom_middle_model.getX()+(i*0.05), 0, bottom_middle_model.getZ())

        bottom_right_model.setScale(0.05)
        bottom_right_model.reparentTo(self.clickable_node)
        bottom_right_model.setPos(
            self.bottom_middle_copy.getX()+0.05, 0, bottom_middle_model.getZ())

        self.clickable_node.setPos(0.5, 0, -0.45)
        self.clickable_node.flattenStrong()

        # The actual button
        self.clickable_button = DirectFrame(
            geom=self.clickable_node,
            parent=self.containerFrame,
            pos=(x, 0, 0),
            relief=None
        )

        self.clickable_text = DirectButton(
            parent=self.clickable_button,
            text='None',
            text_scale=0.075,
            text_font=loader.loadFont(toon_font),
            text_align=TextNode.ALeft,
            pos=(0.5, 0, -0.025),
            relief=None,
            frameSize=(0, width_of_clickable*0.055, -0.05, 0.1),
            command=self.showSelectables,
            extraArgs=[function_to_execute,
                       keyOrValueNum, selectables_dictionary],
            clickSound=loader.loadSfx(gui_click_sound),
            rolloverSound=loader.loadSfx(gui_rollover_sound),
        )

        return self.clickable_button

    def showAndHide(self, function, args_to_insert):
        '''This basically reparents clickable so you can see it again and hides the selectables_frame'''
        self.clickable.show()
        self.clickable_text['text'] = args_to_insert
        self.selectablesFrame.hide()
        function(args_to_insert)

    def generateSelectablesFrame(self,
                                 x_position,
                                 selectables_dictionary=None,
                                 width=6,
                                 height=6):
        '''Creates the selectable menu based on the provided args'''
        dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        top_left_model = dynamicFrameFile.find('**/*topLeft')
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_right_model = dynamicFrameFile.find('**/topRight')
        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_right_model = dynamicFrameFile.find('**/*centerRight')
        bottom_left_model = dynamicFrameFile.find('**/*bottomLeft')
        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_right_model = dynamicFrameFile.find('**/*bottomRight')

        self.selectable_dynamic_frame = NodePath('selectable_frame')

        top_piece = NodePath('top_half')

        # The Top Left piece
        top_left_model.setScale(0.05)
        top_left_model.reparentTo(top_piece)
        top_left_model.setPos(0, 0, 0)

        # The top middle piece
        top_middle_model.setScale(0.05)
        top_middle_model.reparentTo(top_piece)
        top_middle_model.setPos(top_left_model.getX() +
                                0.05, 0, top_left_model.getZ())

        # The Top Middle repetitions
        for i in range(1, width):
            self.top_center_copy = top_middle_model.copyTo(top_piece)
            self.top_center_copy.setPos(top_middle_model.getX()+(0.05*i), 0, 0)

        # The Top Right piece
        top_right_model.setScale(0.05)
        top_right_model.reparentTo(top_piece)
        top_right_model.setPos(top_middle_model.getX()+(0.05*width), 0, 0)

        top_piece.flattenStrong()
        top_piece.reparentTo(self.selectable_dynamic_frame)
        top_piece.setPos(0, 0, 0)
        # Let's make a node that we can duplicate.

        middle_piece = NodePath('middle_half')
        middle_piece.reparentTo(self.selectable_dynamic_frame)
        middle_piece.setPos(0, 0, -0.05)

        center_left_model.setScale(0.05)
        center_left_model.reparentTo(middle_piece)
        center_left_model.setPos(0, 0, 0)

        center_middle_model.setScale(0.05)
        center_middle_model.reparentTo(middle_piece)
        center_middle_model.setPos(0.05, 0, 0)

        # The Center Middle repetitions
        for i in range(1, width+1):
            self.center_middle_copy = center_middle_model.copyTo(middle_piece)
            self.center_middle_copy.setPos(0.05*i, 0, 0)

        center_right_model.setScale(0.05)
        center_right_model.reparentTo(middle_piece)
        center_right_model.setPos((width+1)*0.05, 0, 0)

        # Now let's duplicate the amount of times the thing is made.

        middle_piece.flattenStrong()

        for i in range(1, height):
            self.middle_piece_copy = middle_piece.copyTo(
                self.selectable_dynamic_frame)
            self.middle_piece_copy.setPos(0, 0, (i * -0.05))

        bottom_piece = NodePath('bottom_half')
        bottom_piece.reparentTo(self.selectable_dynamic_frame)
        bottom_piece.setPos(0, 0, height * -0.05)

        bottom_left_model.setScale(0.05)
        bottom_left_model.reparentTo(bottom_piece)
        bottom_left_model.setPos(0, 0, -0.05)

        bottom_middle_model.setScale(0.05)
        bottom_middle_model.reparentTo(bottom_piece)
        bottom_middle_model.setPos(0.05, 0, -0.05)

        # The Bottom Middle repetitions
        for i in range(1, width+1):
            self.bottom_middle_copy = bottom_middle_model.copyTo(bottom_piece)
            self.bottom_middle_copy.setPos((0.05*i), 0, -0.05)

        # self.selectable_dynamic_frame.ls()
        bottom_right_model.setScale(0.05)
        bottom_right_model.reparentTo(bottom_piece)
        bottom_right_model.setPos((width+1)*0.05, 0, -0.05)

        bottom_piece.flattenStrong()

        self.slider_geom = self.options_geom.find('**/*slider1')
        self.trough_geom = self.options_geom.find('**/*lineSkinny')

        self.selectablesFrame = DirectGui.DirectFrame(
            geom=self.selectable_dynamic_frame,
            parent=self.containerFrame,
            pos=((x_position+0.5), 0, 0.05),
            relief=None,
        )

        # If you want to debug the amount of items ya got, uncomment the line under.

        #print(f"{self.modalTextNode['text']} : {len(selectables_dictionary)} items")

        selectable_height = (len(selectables_dictionary)) * -0.1005

        self.selectableScrollFrame = DirectGui.DirectScrolledFrame(
            parent=self.selectablesFrame,
            frameSize=(0, width*0.052, -0.4, 0),
            canvasSize=(0, 1.5, selectable_height, 0),

            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_range=(0, 0.5),
            verticalScroll_value=0,
            verticalScroll_manageButtons=True,
            verticalScroll_resizeThumb=True,
            verticalScroll_relief=None,
            verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom=self.slider_geom,
            verticalScroll_thumb_geom_scale=0.05,
            verticalScroll_thumb_geom_pos=(0, 0, 0),

            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_scale=0.085,
            verticalScroll_geom_pos=(width*0.049, 0, -0.175),
            verticalScroll_geom_hpr=(0, 0, 90),

            horizontalScroll_relief=None,
            horizontalScroll_thumb_relief=None,
            horizontalScroll_incButton_relief=None,
            horizontalScroll_decButton_relief=None,
            scrollBarWidth=0.05,
            relief=None,
        )

        self.selectablesFrame.hide()

    def showSelectables(self,
                        command_to_execute,
                        keyOrValue,
                        selectables_dictionary):
        self.selectablesFrame.show()
        self.clickable.hide()

        if self.populateBoolean:
            pass  # We've already populated it.
            print('This Selection Frame has already been generated')
        else:
            print('Generating Selectable Frame for the first time')
            if keyOrValue == 1:  # If we want to return the values
                i = 0
                for item in selectables_dictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableScrollFrame.getCanvas(),
                        text=item,
                        text_font=self.selectable_gui_font,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=loader.loadSfx(gui_click_sound),
                        rolloverSound=loader.loadSfx(gui_rollover_sound),
                        extraArgs=[command_to_execute,
                                   selectables_dictionary[item]]
                    )
            else:  # If we want to return the key
                i = 0
                for item in selectables_dictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableScrollFrame.getCanvas(),
                        text=item,
                        text_font=self.selectable_gui_font,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=loader.loadSfx(gui_click_sound),
                        rolloverSound=loader.loadSfx(gui_rollover_sound),
                        extraArgs=[command_to_execute, item]
                    )
            self.populateBoolean = True
