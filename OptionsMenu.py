from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import FLAT, HORIZONTAL, SUNKEN, VERTICAL
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, TextNode
from direct.interval.LerpInterval import *
from Toon import Toon
from ToonDNA import *
from direct.showbase.DirectObject import DirectObject

options_geom = 'phase_3/models/gui/ttr_m_gui_gen_buttons.bam'
gui_click_sound = 'phase_3/sfx/GUI_create_toon_fwd.ogg'
gui_rollover_sound = 'phase_3/sfx/GUI_rollover.ogg'
toon_font = 'phase_3/fonts/ImpressBT.ttf'

class OptionsMenu(DirectObject):
    '''The main OptionsMenu
       Houses the DirectFrame that is the entire frame.'''

    def __init__(self, toon):
        self.showOptions = False
        self.main_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        self.options_geom = loader.loadModel(options_geom)
        self.icon = loader.loadModel('phase_3/models/gui/toontown-logo.bam')
        self.toontaskicons = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_qst_toontask_icons.bam')

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
            frameSize=(0,0,0,0),
            geom = self.outer_page_geom, 
            geom_scale=0.15, 
            parent=aspect2d,
            sortOrder=3,
            pos=(0.8,0,0)
            )

        # First page, this'll be where the Toon controller is

        self.first_page = DirectGui.DirectFrame(
            parent=self.outer_page,
            geom = self.first_page_geom,
            geom_scale=0.15,
            geom_pos=(0,0,0.1),
            frameColor=(0,0,0,0)
        )
        
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')

        self.label_inner_text = OnscreenText(text='Toon Creator',
        parent=self.first_page,
        font=label_outer_font,
        fg=(0.2,0.6,0.9,1),
        scale=0.15,
        shadow=(0.11,0.27,0.34,1),
        pos=(0,0.4)
        )
        
        # First Tab related stuff

        self.firstTabGeom = self.icon.find('**/*eyes')

        self.first_Tab = DirectGui.DirectButton(
            geom=self.firstTabGeom,
            geom_scale=0.045,
            geom_pos=(-0.6,0,0.680),
            parent = self.first_page,
            frameColor=(0,0,0,0))
        
        self.optionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.first_page,
            # GUI of the box
            frameSize=(-0.8,0.85,-0.55,0.35),
            canvasSize=(-1,0,-5,1),
            frameColor=(0,0,0,0),

            # GUI DirectScrollBar attributes
            horizontalScroll_frameSize=(0,0,0,0), # Getting rid of the horizontal scroll

            # The button you click and hold.
            verticalScroll_thumb_geom = self.slider_geom, 
            verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=loader.loadSfx(gui_click_sound),
            verticalScroll_thumb_rolloverSound=loader.loadSfx(gui_rollover_sound),

            # The (invisible) bar you slide across.
            verticalScroll_relief=None, 
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_pos=(0.80,0,-0.10),
            verticalScroll_geom_hpr=(0,0,90),
            verticalScroll_geom_scale=(0.2,0.1,0.1),
            scrollBarWidth=0.1,
        )

        def updateHead():
            '''Updates the Toon's head based on the value'''
            sliderValue = self.head_slider.slider['value']
            tested_value = int(sliderValue)

            if self.selectedToon.species == 'mi':
                if tested_value == 50:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('mi', 'ls', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value == 100:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('mi', 'ss', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
            elif self.selectedToon.species == 'd':
                if tested_value < 20 and tested_value > 15:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('d', 'ss', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 40 and tested_value > 35:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('d', 'sl', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 60 and tested_value > 55:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('d', 'ls', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 80 and tested_value > 75:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead('d', 'll', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
            else:
                if tested_value < 20 and tested_value > 15:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead(self.selectedToon.species, 'ls', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 40 and tested_value > 35:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead(self.selectedToon.species, 'll', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 60 and tested_value > 55:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead(self.selectedToon.species, 'sl', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                elif tested_value < 80 and tested_value > 75:
                    self.selectedToon.toonActor.delete()
                    self.selectedToon.updateHead(self.selectedToon.species, 'ss', self.selectedToon.eyelashes)
                    self.selectedToon.generateActor()
                
            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

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
            
            
            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

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
            
            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

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
                self.selectedToon.updateTorso(self.selectedToon.torso_type[0] + 'd')
                self.selectedToon.generateActor()
            elif self.selectedToon.gender == 'f':
                self.selectedToon.gender = 'm'
                self.selectedToon.toonActor.delete()
                self.selectedToon.updateTorso(self.selectedToon.torso_type[0] + 's')
                self.selectedToon.generateActor()

            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

        def eyelashToggle():
            '''Toggles the eyelashes on the Toon's head'''
            if self.selectedToon.eyelashes:
                self.selectedToon.toonActor.delete()
                self.selectedToon.eyelashes = False
                self.selectedToon.updateHead(self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            elif self.selectedToon.eyelashes == False:
                self.selectedToon.toonActor.delete()
                self.selectedToon.eyelashes = True
                self.selectedToon.updateHead(self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
                self.selectedToon.generateActor()
            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

        def smoothanimationToggle():
            if self.selectedToon.smooth_enabled:
                self.selectedToon.toonActor.setBlend(frameBlend=False)
                self.selectedToon.smooth_enabled = False
            else:
                self.selectedToon.toonActor.setBlend(frameBlend=True)
                self.selectedToon.smooth_enabled = True

        def shoesToggle():
            if self.selectedToon.wearsShoes:
                self.selectedToon.toonActor.find('**/*shoes').hide()
                self.selectedToon.toonActor.find('**/*boots_short').hide()
                self.selectedToon.toonActor.find('**/boots_long*').hide() 
                self.selectedToon.wearsShoes = False
            else:
                self.selectedToon.toonActor.find('**/*shoes').show()
                self.selectedToon.toonActor.find('**/*boots_short').show()
                self.selectedToon.toonActor.find('**/boots_long*').show()                  
                self.selectedToon.wearsShoes = True
                
        def updateSpecies(species):
            '''Updates the Toon's species'''
            self.selectedToon.toonActor.delete()
            self.selectedToon.updateSpecies(species)
            self.selectedToon.updateHead(self.selectedToon.species, self.selectedToon.headtype, self.selectedToon.eyelashes)
            self.selectedToon.generateActor()
            self.selectedToon.toonActor.setH(self.rotation_slider.slider['value'])

        def updateAnim(anim):
            self.selectedToon.toonActor.delete()
            self.selectedToon.animationType = anim
            self.selectedToon.generateActor()

        def updateBackpack(backpack_type):
            self.selectedToon.backpack_type = backpack_type
            self.selectedToon.attachBackpack(backpack_type)

        def updateGlasses(glasses_type):
            self.selectedToon.glasses_type = glasses_type
            self.selectedToon.attachGlasses(glasses_type)

        self.rotation_slider = OptionsSlider(aspect2d, '', -0.80, rotateToon, (0, 360))
        self.rotation_slider.containerFrame.setX(-1.75)
        self.rotation_slider.slider.setX(1.15)
        self.rotation_slider.slider['value'] = 180
        rotateToon()

        self.toonDNALabel = OptionsLabel(self.optionsScroll.getCanvas(),'Toon DNA',  0.8)
        self.head_slider = OptionsSlider(self.optionsScroll.getCanvas(), 'Head:', 0.65, updateHead)
        self.torso_slider = OptionsSlider(self.optionsScroll.getCanvas(), 'Torso:', 0.50, updateTorso)
        self.legs_slider = OptionsSlider(self.optionsScroll.getCanvas(), 'Legs:', 0.35, updateLegs)
        self.eyelash_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Eyelashes:', 0.20, eyelashToggle)
        self.gender_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Gender:', 0.05, changeGender)
        self.smoothanim_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Smooth Animation:', -0.1, smoothanimationToggle)
        self.shoes_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Shoes:', -0.25, shoesToggle)

        self.glasses_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Glasses:', -0.1, -2.9, -3.5, 22, glasses_dict, updateGlasses, 0)
        self.backpack_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Backpack:', -0.1, -2.7, -3.9, 23, backpack_dict, updateBackpack, 0)
        self.accessory_label = OptionsLabel(self.optionsScroll.getCanvas(), 'Accessories', -2.5)
        self.glove_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Gloves Color:', 0, -1.4, 1.25, 10, colorsList, updateGloveColor, 0)
        self.leg_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Leg Color:', 0, -1.2, 1.25, 10, colorsList, updateLegsColor, 0)
        self.arm_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Arms Color:', 0, -1, 1.25, 10, colorsList, updateArmsColor, 0)
        self.head_color_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Head Color:', 0, -0.8, 1.25, 10, colorsList, updateHeadColor, 0)
        self.anim_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Animation:', 0, -0.6, -4.2, 10, anim_dict, updateAnim)
        self.species_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'Species:', 0, -0.4, 7.5, 10, species_dict, updateSpecies)
        

    def hideOrShowOptions(self):
        if self.showOptions:
            self.showOptions = False
            self.outer_page.hide()
            self.rotation_slider.slider.hide()
        else:
            self.showOptions = True
            self.outer_page.show()
            self.rotation_slider.slider.show()
#        self.clothingLabel = OptionsLabel(self.optionsScroll.getCanvas(),'Clothing',  -0.10)
     #   self.test_menu = OptionsChoosingMenu(self.optionsScroll.getCanvas(), 'test:', -0.9)

class OptionsLabel:
    '''Used as labels for the bigger letters
    Lower Z means lower on the DirectScrolledFrame'''
    def __init__(self, labelParent, labelText, z):
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')
        
        self.label = DirectGui.DirectLabel(
            parent=labelParent,        
            pos=(-1, 0, z),
            frameColor=(0,0,0,0),
            frameSize=(0,0.9,0,0.1)    
        )

        self.labelText = OnscreenText(
            text=labelText,
            font=label_outer_font,
            fg=(0,0,0,1),
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
            frameColor=(0,0,0,0),
            frameSize=(-0.01,0.9,-0.01,0.06),
            scale=0.9
        )

        self.modalTextNode = OnscreenText(
            align=TextNode.ALeft,
            text=modalText,
            font=modal_font
        )
        self.modalTextNode.reparentTo(self.containerFrame)

class OptionsSlider(OptionsModal):
    '''Creates a Slider which is useful for functions with arguments that include a range'''
    def __init__(self, modalParent, modalText, z, slider_command=None, given_range=(0,100)):
        super().__init__(modalParent, modalText, z) # Creates the text on the left
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.slider_thumb_geom = self.options_geom.find('**/*slider2')
        self.slider_scroll_geom = self.options_geom.find('**/*lineSkinny')

        self.slider = DirectGui.DirectSlider(
            thumb_geom=self.slider_thumb_geom,
            thumb_geom_scale=(0.4,0.1,0.25),
            thumb_relief=None,
            thumb_clickSound=loader.loadSfx(gui_click_sound),
            thumb_rolloverSound=loader.loadSfx(gui_rollover_sound),
            geom=self.slider_scroll_geom, 
            geom_scale=0.5,
            scale=(0.3,0.1,0.4),
            relief=None,
            command=slider_command,
            range=given_range
        )
        self.slider.reparentTo(self.containerFrame)
        self.slider.setPos(1.3,0,0)

class OptionsToggle(OptionsModal):
    '''Creates a toggle that creates an off/on switch'''
    def __init__(self, modalParent, modalText, z, toggle_command=None):
        super().__init__(modalParent, modalText, z) # Creates the text on the left
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.toggle_thumb_geom = self.options_geom.find('**/*toggleButton')
        self.warm_geom = self.options_geom.find('**/*toggleWarm')
        self.cold_geom = self.options_geom.find('**/*toggleCool')

        def executeFunction(self, toggle_command=None):
            if toggle_command:
                toggle_command()

            animateToggle()

        self.button= DirectGui.DirectCheckButton(
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
        self.button.setPos(1.25,0,0.025)

        # The button on the thing.
        self.toggle_thumb_geom.setScale(1)
        self.toggle_thumb_geom.setPos(0.6,0,-0.15)
        self.toggle_thumb_geom.reparentTo(self.button)

        def animateToggle():
            if self.button['indicatorValue']:
                toggle_forward_interval = LerpPosInterval(self.toggle_thumb_geom, 0.15, (1.2,0,-0.15), (0.6,0,-0.15) )
                toggle_forward_interval.start()
            else:
                toggle_back_interval = LerpPosInterval(self.toggle_thumb_geom, 0.15, (0.6,0,-0.15), (1.2,0,-0.15) )
                toggle_back_interval.start()

class OptionsChoosingMenu(OptionsModal):
    '''Creates a menu with a bunch of options that execute a certain function the height of selectables controls
    the bottom of the frame. keyOrValue simply returns the value if set to 1, key if 0.'''
    def __init__(self, modalParent, modalText, x, z, height_of_selectables, width_of_clickable, used_dictionary=None, chosen_command=None, keyOrValue=1):
        super().__init__(modalParent, modalText, z)
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.clickable = self.generateClickableFrame(chosen_command, x, height_of_selectables, width_of_clickable, keyOrValue, used_dictionary)

    def generateClickableFrame(self, command, x, frame_height, width_of_clickable, key_or_value, used_dictionary=None):
        '''Creates the small frame that the player will click on'''
        dynamicFrameFile = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        self.dynamic_frame = NodePath('test')
        # The Top Left piece
        self.top_leftdf = dynamicFrameFile.find('**/*topLeft')
        self.top_leftdf.setScale(0.05)
        self.top_leftdf.reparentTo(self.dynamic_frame)
        self.top_leftdf.setPos(x,0,0.5)
        # The top middle piece
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_middle_model.reparentTo(self.top_leftdf)
        top_middle_model.setPos(1,0,0)
        # The Top Middle repetitions
        for i in range(1, width_of_clickable):
            self.top_center_copy = top_middle_model.copyTo(self.top_leftdf)
            self.top_center_copy.setPos(top_middle_model.getX()+i,0,0)
        # The Top Right piece
        top_right_model = dynamicFrameFile.find('**/topRight')
        top_right_model.reparentTo(self.top_center_copy)
        top_right_model.setPos(1,0,0)
        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_left_model.reparentTo(self.top_leftdf)
        center_left_model.setPos(0,0,-1)
        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_middle_model.reparentTo(center_left_model)
        center_middle_model.setPos(1,0,0)
        # The Center Middle repetitions
        for i in range(1, width_of_clickable+1):
            self.center_middle_copy = center_middle_model.copyTo(self.top_leftdf)
            self.center_middle_copy.setPos(i,0,-1)
        center_right_model = dynamicFrameFile.find('**/*centerRight')
        center_right_model.setScale(1)
        center_right_model.reparentTo(self.center_middle_copy)
        center_right_model.setPos(1,0,0)
        bottom_left_model= dynamicFrameFile.find('**/*bottomLeft')
        bottom_left_model.setScale(1)
        bottom_left_model.reparentTo(self.top_leftdf)
        bottom_left_model.setPos(0,0,-2)
        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_middle_model.setScale(1)
        bottom_middle_model.reparentTo(bottom_left_model)
        bottom_middle_model.setPos(1,0,0)
        # The Bottom Middle repetitions
        for i in range(1, width_of_clickable+1):
            self.bottom_middle_copy = bottom_middle_model.copyTo(self.top_leftdf)
            self.bottom_middle_copy.setPos(i,0,-2)

        self.bottom_rightdf = dynamicFrameFile.find('**/*bottomRight')
        self.bottom_rightdf.setScale(1)
        self.bottom_rightdf.reparentTo(self.bottom_middle_copy)
        self.bottom_rightdf.setPos(1,0,0)

        self.dynamic_frame.setPos(0.5,0,-0.45)

        # The actual button
        self.clickable_button = DirectButton(
            sortOrder=5,
            geom=self.dynamic_frame,
            parent=self.containerFrame,
            relief=None,
            command=self.generateSelectablesFrame,
            extraArgs=[command, frame_height, key_or_value, used_dictionary],
            clickSound=loader.loadSfx(gui_click_sound),
            rolloverSound=loader.loadSfx(gui_rollover_sound),
            text='None', 
            text_font=loader.loadFont(toon_font), 
            text_pos =(x+0.5,-0.025), 
            text_align=TextNode.ALeft,
            text_scale=0.07
        )
        return self.clickable_button

    def showAndHide(self, function, args_to_insert):
        '''This basically reparents clickable so you can see it again and hides the selectables_frame'''
        self.clickable.reparentTo(self.containerFrame)
        self.clickable['text'] = args_to_insert
        self.selectables_geom.removeNode()
        self.selectables_frame.removeNode()
        function(args_to_insert)

    def generateSelectablesFrame(self, command_to_execute, selectable_frame_height, keyOrValue, selectables_dictionary=None, height=6):
        dynamicFrameFile = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        self.selectable_dynamic_frame = NodePath('selectable_frame')

        self.clickable.reparentTo(hidden)    
        
        # The Top Left piece
        self.top_leftdf = dynamicFrameFile.find('**/*topLeft')
        self.top_leftdf.setScale(0.05)
        self.top_leftdf.reparentTo(self.selectable_dynamic_frame)
        self.top_leftdf.setPos(0.5,0,0.5)

        # The top middle piece
        top_middle_model = dynamicFrameFile.find('**/*topMiddle')
        top_middle_model.reparentTo(self.top_leftdf)
        top_middle_model.setPos(self.top_leftdf.getX()+0.5,0,0)

        # The Top Middle repetitions
        for i in range(1, 20):
            self.top_center_copy = top_middle_model.copyTo(self.top_leftdf)
            self.top_center_copy.setPos(top_middle_model.getX()+i,0,0)

        # The Top Right piece
        top_right_model = dynamicFrameFile.find('**/topRight')
        top_right_model.reparentTo(self.top_center_copy)
        top_right_model.setPos(1,0,0)

        # Let's make a node that we can duplicate.

        self.middlepiece = NodePath('middle_piece')
        self.middlepiece.reparentTo(self.top_leftdf)
        self.middlepiece.setPos(0,0,0)

        center_left_model = dynamicFrameFile.find('**/*centerLeft')
        center_left_model.reparentTo(self.middlepiece)
        center_left_model.setPos(0,0,-1)

        center_middle_model = dynamicFrameFile.find('**/*centerMiddle')
        center_middle_model.reparentTo(self.middlepiece)
        center_middle_model.setPos(1,0,-1)

         # The Center Middle repetitions
        for i in range(1, 21):
            self.center_middle_copy = center_middle_model.copyTo(self.middlepiece)
            self.center_middle_copy.setPos(i,0,-1)
            

        center_right_model = dynamicFrameFile.find('**/*centerRight')
        center_right_model.setScale(1)
        center_right_model.reparentTo(self.center_middle_copy)
        center_right_model.setPos(1,0,0)

        # Now let's duplicate the amount of times the thing is made.

        for i in range(1, height):
            self.middle_piece_copy = self.middlepiece.copyTo(self.selectable_dynamic_frame)
            self.middle_piece_copy.setPos(0.5, 0, 0.5 - (0.05 * i))
            self.middle_piece_copy.setScale(0.05)

        bottom_left_model= dynamicFrameFile.find('**/*bottomLeft')
        bottom_left_model.setScale(1)
        bottom_left_model.reparentTo(self.middle_piece_copy)
        bottom_left_model.setPos(0,0,-2)

        bottom_middle_model = dynamicFrameFile.find('**/*bottomMiddle')
        bottom_middle_model.setScale(1)
        bottom_middle_model.reparentTo(bottom_left_model)
        bottom_middle_model.setPos(1,0,0)

        # The Bottom Middle repetitions
        for i in range(1, 21):
            self.bottom_middle_copy = bottom_middle_model.copyTo(bottom_left_model)
            self.bottom_middle_copy.setPos(i, 0, 0)


        self.bottom_right = dynamicFrameFile.find('**/*bottomRight')
        self.bottom_right.setScale(1)
        self.bottom_right.reparentTo(self.bottom_middle_copy)
        self.bottom_right.setPos(1,0,0)

        self.slider_geom = self.options_geom.find('**/*slider1')
        self.trough_geom = self.options_geom.find('**/*lineSkinny')

        self.selectables_geom = DirectGui.DirectFrame(
            geom=self.selectable_dynamic_frame,
            parent=self.containerFrame,
            pos=(0.05,0,-0.45),
            relief=None
        )

        self.selectables_frame = DirectGui.DirectScrolledFrame(
            parent=self.selectables_geom,
            frameSize=(-0.5,1.6,-0.6,0.1),
            canvasSize=(-1.25,0,selectable_frame_height,10),
            pos=(0.75,0,0.45),
            scale=0.5,
            sortOrder=10,
            relief=None,

        # Horizontal bar stuff
            horizontalScroll_relief=None,
            horizontalScroll_incButton_relief=None,
            horizontalScroll_decButton_relief=None,
            horizontalScroll_frameSize=(0,0,0,0), # Getting rid of the horizontal scroll

        # Vertical bar
            verticalScroll_thumb_geom=self.slider_geom,
            verticalScroll_thumb_geom_scale=0.1,
            verticalScroll_relief=None,
            verticalScroll_thumb_relief=None,
            verticalScroll_range=(0, 0.5),
            verticalScroll_thumb_clickSound=loader.loadSfx(gui_click_sound),
            verticalScroll_thumb_rolloverSound=loader.loadSfx(gui_rollover_sound),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom_hpr=(0,0,90),
            verticalScroll_geom_pos=(self.bottom_right.getX()+0.55,0,-0.25),
            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_scale=0.175,
            scrollBarWidth=0.1
        )

        selectable_gui_font = loader.loadFont(toon_font)

        if keyOrValue == 1: # If we want to return the values
            i = 0
            for item in selectables_dictionary.keys():
                i+=1
                button = DirectButton(
                    parent = self.selectables_frame.getCanvas(),
                    text=item,
                    text_font=selectable_gui_font,
                    text_align=TextNode.ALeft,
                    text_scale=0.57, 
                    scale=0.2, 
                    pos=(-1.2,0,10 - (i*0.2) ), 
                    relief=None,
                    command=self.showAndHide,
                    clickSound=loader.loadSfx(gui_click_sound),
                    rolloverSound=loader.loadSfx(gui_rollover_sound),
                    extraArgs=[command_to_execute,selectables_dictionary[item]]
            )
        else: # If we want to return the key
            i = 0
            for item in selectables_dictionary.keys():
                i+=1
                button = DirectButton(
                    parent = self.selectables_frame.getCanvas(),
                    text=item,
                    text_font=selectable_gui_font,
                    text_align=TextNode.ALeft,
                    text_scale=0.57, 
                    scale=0.2, 
                    pos=(-1.2,0,10 - (i*0.2) ), 
                    relief=None,
                    command=self.showAndHide,
                    clickSound=loader.loadSfx(gui_click_sound),
                    rolloverSound=loader.loadSfx(gui_rollover_sound),
                    extraArgs=[command_to_execute,item]
            )





