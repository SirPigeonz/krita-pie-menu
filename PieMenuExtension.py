from krita import *
from .Settings import Settings
from .MenuArea import MenuArea

class PieMenuExtension(Extension):
  def __init__(self,parent):
    super(PieMenuExtension, self).__init__(parent)
    self.settings = None
    self.menuArea = None

  def setup(self):
    pass

  def openPieMenu( self ):
    self.menuArea = MenuArea(QCursor.pos(), Krita.instance().activeWindow().qwindow())

  def openSettings( self ):
    self.settings = Settings(Krita.instance().activeWindow().qwindow())

  def createActions(self, window):
    self.pieMenuAction = window.createAction("pieMenu", "Pie Menu")
    self.pieMenuSettingsAction = window.createAction("pieMenuSettings", "Pie Menu Settings")

    self.pieMenuAction.triggered.connect(self.openPieMenu)
    self.pieMenuAction.setAutoRepeat(False)

    self.pieMenuSettingsAction.triggered.connect(self.openSettings)
    self.pieMenuSettingsAction.setAutoRepeat(False)