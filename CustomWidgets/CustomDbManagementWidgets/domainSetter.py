# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2016-12-20
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Philipe Borba - Cartographic Engineer @ Brazilian Army
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
import os

from qgis.core import QgsMessageLog

# Qt imports
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtCore import pyqtSlot, pyqtSignal, QSettings, Qt
from PyQt4.QtSql import QSqlQuery
from PyQt4.QtGui import QListWidgetItem

# DSGTools imports
from DsgTools.ServerTools.viewServers import ViewServers
from DsgTools.Factories.SqlFactory.sqlGeneratorFactory import SqlGeneratorFactory
from DsgTools.Factories.DbFactory.dbFactory import DbFactory
from DsgTools.PostgisCustomization.CustomJSONTools.customJSONBuilder import CustomJSONBuilder

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'domainSetter.ui'))

class DomainSetter(QtGui.QDialog, FORM_CLASS):
    domainChanged = pyqtSignal(str, dict, dict)
    def __init__(self, abstractDb, references = None, filter = None, parent = None):
        """Constructor."""
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.abstractDb = abstractDb
        self.populateDomainList()
        self.domainName = None
        self.domainDict = None
        self.filterClause = dict()
        self.jsonBuilder = CustomJSONBuilder()
        self.populateFromJsonTag(references, filter)
    
    def populateFromJsonTag(self, references, filter):
        if references:
            item = self.domainListWidget.findItems(references, Qt.MatchExactly)
            if isinstance(item,list):
                item = item[0]
            self.domainListWiget.setCurrentItem(item)
        if filter <> []:
            codeNameList = [i for i in self.domainDict.keys() if self.domainDict[i] in filter]
            for codeName in codeNameList:
                item = self.filterListWidget.findItems(references, Qt.MatchExactly)
                if isinstance(item,list):
                    item = item[0]
                item.setCheckState(QtCore.Qt.Checked)


    def populateDomainList(self):
        self.domainTableList = self.abstractDb.getDomainTables()
        self.domainListWidget.clear()
        for domain in self.domainTableList:
            self.domainListWidget.addItem(domain)
    
    def clearAll(self):
        self.filterLineEdit.clear()
        self.filterListWidget.clear()
        self.filterCheckBox.setCheckState(QtCore.Qt.Unchecked)
        self.domainName = None
        self.domainDict = None
        self.filterClause = dict()
        self.populateDomainList()

    def enableItems(self, enabled):
        self.filterListWidget.setEnabled(enabled)
    
    def clearCheckableItems(self):
        for idx in range(self.filterListWidget.__len__()):
            item = self.filterListWidget.item(idx)
            item.setCheckState(QtCore.Qt.Unchecked)
    
    @pyqtSlot(int)
    def on_filterCheckBox_stateChanged(self, idx):
        if idx == 2:
            state = True
        else:
            state = False
            self.clearCheckableItems()
        self.enableItems(state)
    
    def getSelectedDomain(self):
        return self.domainListWidget.selectedItems()[0].data()
    
    @pyqtSlot(int)
    def on_domainListWidget_currentRowChanged(self, idx):
        curItem = self.domainListWidget.item(idx)
        self.filterListWidget.clear()
        if curItem:
            self.domainName = curItem.data(0)
            self.domainDict = self.abstractDb.getDomainDictV2('dominios.'+self.domainName)
            for codeName in self.domainDict.keys():
                newItem = QListWidgetItem(codeName)
                newItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
                newItem.setCheckState(QtCore.Qt.Unchecked)
                self.filterListWidget.addItem(newItem)
    
    def on_filterLineEdit_textChanged(self, text):
        '''
        Filters the items to make it easier to spot and select them
        '''
        classes = [edgvDomain for edgvDomain in self.domainTableList if text in edgvDomain]
        self.domainListWidget.clear()
        self.domainListWidget.addItems(classes)
        self.domainListWidget.sortItems()
    
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.clearAll()

    @pyqtSlot()
    def on_buttonBox_accepted(self):
        for idx in range(self.filterListWidget.__len__()):
            item = self.filterListWidget.item(idx)
            if item.checkState() == 2:
                codeName = item.data(0) 
                if codeName not in self.filterClause.keys():
                    self.filterClause[codeName] = self.domainDict[codeName]
        self.domainChanged.emit(self.domainName, self.domainDict, self.filterClause)
    
    def getChildWidgets(self):
        return None
    