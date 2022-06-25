################################
#
#
#       This file contains all the methods
#       meant for NPCS
#
################################

from gui.EditorMenu import *
from toon.ToonDNA import *
from toon.npctoon.NPCDictionaryForChoosingMenu import *

class NPCEditorMenu(EditorMenu):
    
    def __init__(self, toon):
        super().__init__()
        self.menuLabel['text'] = 'NPC Creator'
        self.menuLabel['fg'] = (0.952, 0.631, 0.007, 1)

        self.selectedToon = toon

        self.notify = DirectNotifyGlobal.directNotify.newCategory('NPCEditorMenu')
        self.notify.setDebug(1)

        self.gsnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), "Goofy's Speedway:", 0.15, -0.45, 15, goofySpeedwayNPCDict, self.updateToon, 1)

        self.mmlnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Donalds Dreamland:', 0.15, -0.25, 15, donaldsDreamlandNPCDict, self.updateToon, 1)

        self.tbnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'The Brrrgh:', -0.07, -0.05, 20, theBrrrghNPCDict, self.updateToon, 1)

        self.mmlnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Minnies Melodyland:', 0.15, 0.15, 15, minniesMelodyLandNPCDict, self.updateToon, 1)

        self.dgnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Daisy Gardens:', 0.1, 0.35, 20, daisyGardensNPCDict, self.updateToon, 1)

        self.ddnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Donalds Dock:', 0.1, 0.55, 20, donaldDockNPCDict, self.updateToon, 1)

        self.ttcnpcDNAMenu = OptionsChoosingMenu(self.firstPageOptionsScroll.getCanvas(
        ), 'Toontown Central:', 0.1, 0.75, 20, toontownCentralNPCDict, self.updateToon, 1)

    def updateToon(self, npcID):
            updatedString = self.selectedToon.convertNPCToToon(npcID)
            self.selectedToon.updateNPCToonInfo(updatedString[0],  # species
            updatedString[1], # headtype
            updatedString[2], # eyelashes
            updatedString[3], # torsoType
            updatedString[4], # legSize
            updatedString[5], # headColor
            updatedString[6], # armColor
            updatedString[7], # legColor
            updatedString[8], # shirtTexture
            updatedString[9],  # shirtTextureColor
            updatedString[10], # shortTexture
            updatedString[11],  # skirtTexture
            updatedString[12]   # bottomColor
            )
            self.selectedToon.updateToonBody()

    def hideSelectables(self):
        self.ttcnpcDNAMenu.selectablesFrame.hide()
        self.ttcnpcDNAMenu.clickable.show()

        self.ddnpcDNAMenu.selectablesFrame.hide()
        self.ddnpcDNAMenu.clickable.show()

        self.dgnpcDNAMenu.selectablesFrame.hide()
        self.dgnpcDNAMenu.clickable.show()

        self.mmlnpcDNAMenu.selectablesFrame.hide()
        self.mmlnpcDNAMenu.clickable.show()

        self.tbnpcDNAMenu.selectablesFrame.hide()
        self.tbnpcDNAMenu.clickable.show()

        self.ddnpcDNAMenu.selectablesFrame.hide()
        self.ddnpcDNAMenu.clickable.show()

        self.gsnpcDNAMenu.selectablesFrame.hide()
        self.gsnpcDNAMenu.clickable.show()