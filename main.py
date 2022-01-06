from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from OptionsMenu import*

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Window settings
        windowSettings = WindowProperties()
        windowSettings.setFullscreen(False)
        windowSettings.setSize(1920, 1080)
        self.win.requestProperties(windowSettings)

        # Music
        self.music = loader.loadSfx('phase_3/audio/bgm/create_a_toon.ogg')
        self.music.setLoop(True)
        #self.music.play()

        # Environment
        self.environment = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
        self.environment.reparentTo(render)
        self.environment.setHpr(-90,0,0)

        # Moving camera
        base.cam.setPos(-4,7,5)
        base.cam.setHpr(-20,0,0)
        base.disableMouse()

        #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam').find('**/*bottomRight')
        #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_sbk_settingsPanel.bam')
        #self.options = loader.loadModel('phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        self.options = OptionsMenu()
        # phase_3/models/gui/ttr_m_gui_gen_buttons.bam for sliders and what not
        # use settings panel for the entire thing.
        # dynamic frame is a piece of the options menu
        # dynamic frame yellow for the generate Toon button
        # dyanimc frame default for the buttons
        # Generic GUI for the sliders


    
app = MyApp()
app.run()