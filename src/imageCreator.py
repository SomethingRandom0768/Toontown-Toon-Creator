from datetime import datetime
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'fullscreen true')
loadPrcFileData('', 'window-title Image Creator')

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from toon.Toon import Toon

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


        self.toon = Toon('ri', 'ls', False, 'ls', 'l', 'm', 'Black', 'Black', 'White', 'Black', 'Sellbot Cog-Crusher Shirt', 'Sellbot Cog-Crusher Shorts', None, 'White', 'White', None, 'Sellbot Cog-Crusher Shades', 1, None, None, 'Sellbot Cog-Crusher Shoes', 'Riggy Neutral', True, True)
        self.toon.toonActor.setPos(10,0,0)
        self.toon.toonActor.pose('Neutral', 0)


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
