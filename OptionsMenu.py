from typing import Text
from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import HORIZONTAL, VERTICAL
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, TextNode


class OptionsMenu(DirectGui.DirectFrame):
    '''The main OptionsMenu
    Houses the DirectGUI'''
    def __init__(self):
        self.main_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        self.options_geom = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_buttons.bam')
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
        self.label_inner_text = OnscreenText(text='Toon Creator',
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
            frameColor=(0,0,0,0.1),

            # GUI DirectScrollBar attributes
            horizontalScroll_frameSize=(0,0,0,0),
            verticalScroll_thumb_geom = self.slider_geom,
            verticalScroll_thumb_geom_scale=(0.06),
            verticalScroll_range=(0,10),
            scrollBarWidth=0.02,
        )
        
        self.firstTabGeom.reparentTo(self.optionsScroll.getCanvas())
        self.firstTabGeom.setScale(0.1)
        self.firstTabGeom.setPos(-0.8,0,0.7)
        