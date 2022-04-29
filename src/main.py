
from panda3d.core import loadPrcFileData, loadPrcFile

loadPrcFile('../config/general.prc')
loadPrcFileData('', 'model-path $RESOURCES_DIR')
loadPrcFileData('',  'notify-level fatal')

from direct.showbase.ShowBase import ShowBase
from gui.ToonEditorMenu import *
from gui.CogEditorMenu import *
from gui.NPCEditorMenu import *
from toon.Toon import Toon

class ToonCreator(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.setFrameRateMeter(True)

        # Environment
        self.environment = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall.bam')
        self.environment.reparentTo(render)
        self.environment.setHpr(-90,0,0)

        # Moving camera
        base.cam.setPos(5.5,18,3)
        base.cam.setHpr(0,0,0)
        base.disableMouse()

        # Music
        self.music = loader.loadSfx('phase_3/audio/bgm/create_a_toon.ogg')
        self.music.setLoop(True)
        self.music.play()

        self.toon = Toon('ca', 'ss', False, 'ls', 'l', 'Cartoonival Blue', 'Cartoonival Blue', 'White', 'Cartoonival Blue', None, None, None, 'White', 'White', None, None, 1, None, None, None, 'Neutral', True, False)
        self.options = ToonEditorMenu(self.toon)
    
app = ToonCreator()
app.run()
