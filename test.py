
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'fullscreen false')
loadPrcFileData('', 'window-title Test File')

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
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
        self.music = loader.loadSfx('phase_5/audio/bgm/ttr_s_ara_cbe_cogdoStreet.ogg')
        self.music.setLoop(True)
        #self.music.play()

        # Moving camera
        base.cam.setPos(10,-20,3)
        base.cam.setHpr(0,0,0)


        # The following Toon's concept was created by Lovealot/Ghosheart, go check her work out at https://toyhou.se/Ghosheart
        self.toon = Toon('ca', 'ss', True, 'ld', 'l', 'f', 'Yellow', 'Bright Red', 'White', 'Bright Red', 'Scientist A', 'Scientist D Shorts', 'Trainee Skirt', 'White', 'White', None, None, 1, None, None, None, 'Neutral', True, False)
        self.toon.toonActor.setPos(10,0,0)
        self.toon.toonActor.pose('Victory Dance', 10)
        base.setBackgroundColor((57/255),255,(20/255))

        # Use the print-screen function on your keyboard to take a screenshot, and then post it in 
        # https://www.aatbio.com/tools/online-automatic-green-screen-remover, a tool you can use to get rid of green screen!


app = MyApp()
app.run()
