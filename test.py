from datetime import datetime
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'fullscreen true')
loadPrcFileData('', 'window-title Test File')

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from src.toon.Toon import Toon

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Window settings
        windowSettings = WindowProperties()
        windowSettings.setSize(1920, 1080)
        windowSettings.setIconFilename('phase_3/etc/icon.ico')
        self.win.requestProperties(windowSettings)

        # Music
        self.music = loader.loadSfx('phase_5/audio/bgm/ttr_s_ara_cbe_cogdoStreet.ogg')
        self.music.setLoop(True)
        #self.music.play()

        # Moving camera
        base.cam.setPos(10,-10,3)
        base.cam.setHpr(0,0,0)


        # The following Toon's concept was created by Lovealot/Ghosheart, go check her work out at https://toyhou.se/Ghosheart
        self.toon = Toon('du', 'ss', False, 'ls', 's', 'f', 'Yellow', 'Yellow', 'White', 'Yellow', 'Oiled Sellbot Cog-Crusher Shirt', 'Oiled Sellbot Cog-Crusher Shorts', 'Oiled Sellbot Cog-Crusher Skirt', 'White', 'White', None, 'Four Eyes', 1, None, None, 'Sleuthing Sneakers', 'fewaf', True, True)
        self.toon.toonActor.setPos(10,0,0)
        self.toon.toonActor.pose('Call Pet', 50)

        # Use the print-screen function on your keyboard to take a screenshot, and then post it in 
        # https://www.aatbio.com/tools/online-automatic-green-screen-remover, a tool you can use to get rid of green screen!

        self.isShadowHidden = False

        def showOrHideShadow():
            if self.isShadowHidden:
                self.isShadowHidden = False
                self.toon.shadow.reparentTo(self.toon.toonActor.find('**/joint_shadow'))
            else:
                self.isShadowHidden = True
                self.toon.shadow.reparentTo(hidden)

        def takeScreenshot():
            base.screenshot(f'Toon{datetime.now()}.png', False)

        self.accept('space', takeScreenshot)
        self.accept('s', showOrHideShadow)

app = MyApp()
app.run()
