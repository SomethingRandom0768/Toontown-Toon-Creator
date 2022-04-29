################################
#
#
#       This file contains all the methods
#       meant for NPCS
#
################################

from gui.EditorMenu import EditorMenu

class NPCEditorMenu(EditorMenu):
    
    def __init__(self):
        super().__init__()
        self.menuLabel['text'] = 'NPC Creator'
        self.menuLabel['fg'] = (0.952, 0.631, 0.007, 1)