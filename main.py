
from panda3d.core import loadPrcFileData

loadPrcFileData('', 'interpolate-frames true')
loadPrcFileData('', 'fullscreen false')
loadPrcFileData('', 'window-title Toon Creator')
loadPrcFileData('', 'notify-level fatal')

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from OptionsMenu import *
from Toon import Toon

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Window settings
        windowSettings = WindowProperties()
        windowSettings.setSize(1280, 720)
        windowSettings.setIconFilename('phase_3/etc/icon.ico')
        self.win.requestProperties(windowSettings)

        # Music
        self.music = loader.loadSfx('phase_3/audio/bgm/create_a_toon.ogg')
        self.music.setLoop(True)
        self.music.play()

        # Environment
        self.environment = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
        self.environment.reparentTo(render)
        self.environment.setHpr(-90,0,0)

        # Moving camera
        base.cam.setPos(5.5,18,3)
        base.cam.setHpr(0,0,0)
        base.disableMouse()

        self.toon = Toon('ri', 'ls', False, 'ms', 'l', 'f', head_color='Periwinkle', arm_color='Periwinkle', leg_color='Periwinkle', animation_type='Neutral', shirt_texture='Beta Bug Hunter Shirt', short_texture='Beta Bug Hunter Shorts', skirt_texture='Bee Skirt', backpack="The Flunk-Trunk", glasses='ToonFest 2020 Blue Attendee Glasses', is60FPS=True)
        self.options = OptionsMenu(self.toon)
    
app = MyApp()
app.run()