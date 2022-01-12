from typing import Text
from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import FLAT, HORIZONTAL, SUNKEN, VERTICAL
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, TextNode
from direct.interval.LerpInterval import *

    #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam').find('**/*bottomRight')
    #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
    #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
    # phase_3/models/gui/ttr_m_gui_gen_buttons.bam for sliders and what not
    # use settings panel for the entire thing.
    # dynamic frame is a piece of the options menu
    # dynamic frame yellow for the generate Toon button
    # dynamic frame default for the buttons
    # Generic GUI for the sliders

options_geom = 'phase_3/models/gui/ttr_m_gui_gen_buttons.bam'

class OptionsMenu:
    '''The main OptionsMenu
       Houses the DirectFrame that is the entire frame.'''
    def __init__(self):
        self.main_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        self.options_geom = loader.loadModel(options_geom)
        self.icon = loader.loadModel('phase_3/models/gui/toontown-logo.bam')
        self.toontaskicons = loader.loadModel('phase_3.5/models/gui/ttr_m_gui_qst_toontask_icons.bam')

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
        
        self.Outer_Page = DirectGui.DirectFrame(
            frameSize=(0,0,0,0),
            geom = self.outer_page_geom, 
            geom_scale=0.15, 
            parent=aspect2d,
            sortOrder=3,
            pos=(0.8,0,0)
            )

        # First page, this'll be where the Toon controller is

        self.First_Page = DirectGui.DirectFrame(
            parent=self.Outer_Page,
            geom = self.first_page_geom,
            geom_scale=0.15,
            geom_pos=(0,0,0.1),
            frameColor=(0,0,0,0)
        )
        
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')

        self.label_inner_text = OnscreenText(text='Test Project',
        parent=self.First_Page,
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
            parent = self.First_Page,
            frameColor=(0,0,0,0))
        
        self.optionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.First_Page,
            # GUI of the box
            frameSize=(-0.8,0.85,-0.55,0.35),
            canvasSize=(-1,0,-2,1),
            frameColor=(0,0,0,0),

            # GUI DirectScrollBar attributes
            horizontalScroll_frameSize=(0,0,0,0), # Getting rid of the horizontal scroll

            # The button you click and hold.
            verticalScroll_thumb_geom = self.slider_geom, 
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_frameSize=(-2.5,5,-2.5,5),

            # The (invisible) bar you slide across.
            verticalScroll_relief=None, 
            verticalScroll_range=(0,5),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_thumb_relief=None,
            verticalScroll_geom=self.trough_geom,
            verticalScroll_geom_pos=(0.80,0,-0.10),
            verticalScroll_geom_hpr=(0,0,90),
            verticalScroll_geom_scale=(0.2,0.1,0.1),
            scrollBarWidth=0.1,
        )

        def updateHead():
            '''Updates the Toon's head based on the value'''
            sliderValue = self.first_slider.slider['value']
            print(sliderValue)
        
        def changeGender():
            print('test2')
        
        self.musicLabel = OptionsLabel(self.optionsScroll.getCanvas(),'Music',  0.8)
        self.first_slider= OptionsSlider(self.optionsScroll.getCanvas(), 'True Friends:', 0.65)
        self.second_slider= OptionsSlider(self.optionsScroll.getCanvas(), 'Big Brains:', 0.50)
        self.toonDNALabel = OptionsLabel(self.optionsScroll.getCanvas(),'Toon DNA',  0.35)
        self.first_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Test:', 0.20)
        self.clothingLabel = OptionsLabel(self.optionsScroll.getCanvas(),'Clothing',  0)
        self.second_toggle= OptionsToggle(self.optionsScroll.getCanvas(), 'Clothing Tes:', -0.20)
        self.accessoryLabel = OptionsLabel(self.optionsScroll.getCanvas(),'Accessories',  -0.4)


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
    def __init__(self, modalParent, modalText, z, slider_command=None):
        super().__init__(modalParent, modalText, z) # Creates the text on the left
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.slider_thumb_geom = self.options_geom.find('**/*slider2')
        self.slider_scroll_geom = self.options_geom.find('**/*lineSkinny')

        self.slider = DirectGui.DirectSlider(
            thumb_geom=self.slider_thumb_geom,
            thumb_geom_scale=(0.4,0.1,0.25),
            thumb_relief=None,
            geom=self.slider_scroll_geom, 
            geom_scale=0.5,
            scale=(0.3,0.1,0.4),
            relief=None,
            command=slider_command,
            range=(0,100)
        )
        self.slider.reparentTo(self.containerFrame)
        self.slider.setPos(1.3,0,0)

class OptionsToggle(OptionsModal):
    def __init__(self, modalParent, modalText, z, toggle_command=None, fake_command=None):
        super().__init__(modalParent, modalText, z) # Creates the text on the left
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
        self.toggle_thumb_geom = self.options_geom.find('**/*toggleButton')
        self.warm_geom = self.options_geom.find('**/*toggleWarm')
        self.cold_geom = self.options_geom.find('**/*toggleCool')

        def executeFunction(self, toggle_command=None):
            if toggle_command:
                print("Function Executed")

            animateToggle()

        self.button= DirectGui.DirectCheckButton(
            scale=0.25,
            relief=None,
            boxImageScale=0.5,
            boxPlacement=('right'),
            boxImage=(self.warm_geom, self.cold_geom),
            boxRelief=None,
            pressEffect=1,
            command=executeFunction,
            extraArgs=[toggle_command]
        )

        self.button.reparentTo(self.containerFrame)
        self.button.setPos(1.25,0,0.1)

        # The button on the thing.
        self.toggle_thumb_geom.setScale(0.5)
        self.toggle_thumb_geom.setPos(0.35,0,-0.25)
        self.toggle_thumb_geom.reparentTo(self.button)

        def animateToggle():
            if self.button['indicatorValue']:
                toggle_forward_interval = LerpPosInterval(self.toggle_thumb_geom, 0.25, (0.65,0,-0.25), (0.35,0,-0.25) )
                toggle_forward_interval.start()
            else:
                toggle_back_interval = LerpPosInterval(self.toggle_thumb_geom, 0.25, (0.35,0,-0.25), (0.65,0,-0.25) )
                toggle_back_interval.start()




