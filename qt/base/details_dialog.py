# Created By: Virgil Dupras
# Created On: 2010-02-05
# Copyright 2013 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog

from .details_table import DetailsModel

class DetailsDialog(QDialog):
    def __init__(self, parent, app):
        QDialog.__init__(self, parent, Qt.Tool)
        self.app = app
        self.model = app.model.details_panel
        self._setupUi()
        # To avoid saving uninitialized geometry on appWillSavePrefs, we track whether our dialog
        # has been shown. If it has, we know that our geometry should be saved.
        self._shown_once = False
        self.app.prefs.restoreGeometry('DetailsWindowRect', self)
        self.tableModel = DetailsModel(self.model)
        # tableView is defined in subclasses
        self.tableView.setModel(self.tableModel)
        self.model.view = self
        
        self.app.willSavePrefs.connect(self.appWillSavePrefs)
    
    def _setupUi(self): # Virtual
        pass
    
    def show(self):
        self._shown_once = True
        QDialog.show(self)

    #--- Events
    def appWillSavePrefs(self):
        if self._shown_once:
            self.app.prefs.saveGeometry('DetailsWindowRect', self)
    
    #--- model --> view
    def refresh(self):
        self.tableModel.reset()
    
