from krita import *
from .Settings import Settings
from .MenuArea import MenuArea

class PieMenuExtension(Extension):
  def __init__(self,parent):
    super(PieMenuExtension, self).__init__(parent)

    self.actionsList = [
        {"name": "your action name", "actionID": "qaction id here"},
        {"name": "your action name2", "actionID": "qaction id here2"},
        {"name": "your action name3", "actionID": "qaction id here3"},
        {"name": "your action name4", "actionID": "qaction id here4"},
        {"name": "your action name5", "actionID": "qaction id here5"}
    ]  

    self.settings = Settings(self.actionsList, Krita.instance().activeWindow().qwindow())
    self.settings.menusChanged.connect(self.updateMenus)

    self.menuArea = MenuArea(QCursor.pos(), Krita.instance().activeWindow().qwindow())

  def setup(self):
    pass

  def updateMenus(self):
    self.menus = self.settings.menus

  def openPieMenu(self):
    if (not self.qWin.underMouse()):
      return
    
    # self.menuArea.menu.showMenuAt()

  def openSettings(self):
    self.settings.show()

  def createActions(self, window):
    self.qWin = window
    
    self.pieMenuAction = window.createAction("pieMenu", "Pie Menu")
    self.pieMenuSettingsAction = window.createAction("pieMenuSettings", "Pie Menu Settings")

    self.pieMenuAction.triggered.connect(self.openPieMenu)
    self.pieMenuAction.setAutoRepeat(False)

    self.pieMenuSettingsAction.triggered.connect(self.openSettings)
    self.pieMenuSettingsAction.setAutoRepeat(False)