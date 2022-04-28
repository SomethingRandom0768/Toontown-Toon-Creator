################################
#
#
#       This file contains all the methods
#       meant for Cogs
#
################################

from gui.EditorMenu import EditorMenu

class CogEditorMenu(EditorMenu):
    
    def __init__(self):
        super().__init__()
        self.menuLabel['text'] = 'Cog Creator'
        self.menuLabel['fg'] = (0, 0, 0, 1)
        self.menuLabel['font'] = loader.loadFont('phase_3/fonts/vtRemingtonPortable.ttf')