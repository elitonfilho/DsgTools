# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2018-02-25
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : borba.philipe@eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os, json
from os.path import expanduser

from qgis.core import QgsMessageLog

# Qt imports
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSlot, Qt, QSettings
from qgis.PyQt.QtWidgets import QListWidgetItem, QMessageBox, QMenu, QApplication, QFileDialog
from qgis.PyQt.QtGui import QCursor
from qgis.PyQt.QtSql import QSqlDatabase, QSqlQuery

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'validationProcessWidget.ui'))

class ValidationProcessWidget(QtWidgets.QWidget, FORM_CLASS):
    def __init__(self, parameterDict = {}, parent = None):
        """Constructor."""
        super(ValidationProcessWidget, self).__init__(parent = parent)
        self.setupUi(self)
        self.parent = parent
        if self.parent:
            self.validationManager = parent.validationManager
        self.validKeys = ['parameters', 'validationProcess']
        self.parameters = None
        self.processChain = None
        self.setInitialState()
        if parameterDict != {}:
            self.populateInterface(parameterDict)
    
    def setInitialState(self):
        self.validationProcessComboBox.clear()
        self.validationProcessComboBox.addItem(self.tr('Select a validation process'))
        self.validationProcessComboBox.addItems(list(self.validationManager.processDict.keys()))
    
    @pyqtSlot(int)
    def on_validationProcessComboBox_currentIndexChanged(self):
        styleSheet = "background-color:rgb({0},{1},{2});".format(255, 0, 0)
        self.parametersPushButton.setStyleSheet(styleSheet)
        self.parametersPushButton.setToolTip(self.tr('Set parameters'))
    
    @pyqtSlot(bool)
    def on_parametersPushButton_clicked(self):
        if self.validationProcessComboBox.currentIndex() < 1:
            self.parameters = None
            self.processChain = None
            return
        processAlias = self.validationProcessComboBox.currentText()
        self.parameters, self.processChain = self.validationManager.getParams(processAlias, restoreOverride = False, withElements = False)
        if self.parameters:
            self.parametersPushButton.setStyleSheet('')
    
    def clearAll(self):
        """
        Clears all widget information
        """
        pass
    
    def getParameterDict(self):
        """
        Components:
        parameterDict = {'validationProcess':--name of the validation process--,
                         'parameters': --parameter dict--}
        """
        if not self.validate():
            raise Exception(self.invalidatedReason())
        parameterDict = dict()
        parameterDict['validationProcess'] = self.validationProcessComboBox.currentText()
        parameterDict['parameters'] = self.parameters
        return parameterDict

    def populateInterface(self, parameterDict):
        """
        Populates interface with parameters from parameterDict.
        """
        if parameterDict:
            if not self.validateJson(parameterDict):
                raise Exception(self.tr('Invalid Validation Process Widget json config!'))
            #set layer combo
            self.validationProcessComboBox.setText(parameterDict['validationProcess'])
    
    def validateJson(self, inputJson):
        """
        Validates input json
        """
        inputKeys = list(inputJson.keys())
        inputKeys.sort()
        if self.validKeys != inputKeys:
            return False
        else:
            return True

    def validate(self):
        """
        Validates fields. Returns True if all information are filled correctly.
        """
        if self.attributeRuleTypeLineEdit.text() == '':
            return False
        return True
    
    def invalidatedReason(self):
        """
        Error reason
        """
        msg = ''
        if self.attributeRuleTypeLineEdit.text() == '':
            msg += self.tr('Invalid rule name!\n')
        return msg