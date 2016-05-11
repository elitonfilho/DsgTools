# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadAuxStruct
                                 A QGIS plugin
 Load line centroid aux structure.
                             -------------------
        begin                : 2016-04-28
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : borba@dsg.eb.mil.br
        mod history          : 
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

#Qgis imports
from qgis.gui import QgsMessageBar

#PyQt imports
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import QApplication, QCursor
import qgis as qgis

#DsgTools imports
from DsgTools.Factories.LayerFactory.layerFactory import LayerFactory

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'loadAuxStruct.ui'))

class LoadAuxStruct(QtGui.QDialog, FORM_CLASS):
    def __init__(self, codeList, parent=None):
        """Constructor."""
        super(self.__class__, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.selectedClasses = []

        self.bar = QgsMessageBar()
        self.setLayout(QtGui.QGridLayout(self))
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.bar.setSizePolicy(sizePolicy)
        self.layout().addWidget(self.bar, 0,0,1,1)

        QtCore.QObject.connect(self.widget, QtCore.SIGNAL(("problemOccurred()")), self.pushMessage)

        
        self.codeList = codeList
        self.layerFactory = LayerFactory()

    @pyqtSlot(bool)
    def on_pushButtonCancel_clicked(self):
        self.close()
        
    def pushMessage(self, msg):
        self.bar.pushMessage("", msg, level=QgsMessageBar.CRITICAL)

    @pyqtSlot(bool)
    def on_pushButtonOk_clicked(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        auxCreated = self.widget.abstractDb.checkCentroidAuxStruct()
        if not auxCreated:
            if QtGui.QMessageBox.question(self, self.tr('Question'), self.tr('Auxiliar structure not created. Do you want to create it?'), QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel) == QtGui.QMessageBox.Cancel:
                self.widget.abstractDb.createCentroidAuxStruct(self.widget.abstractDb.getEarthCoverageClasses())
                self.loadLayers()
        else:
            self.loadLayers()
        QApplication.restoreOverrideCursor()

    def loadLayers(self):
        try:
            auxClasses = self.widget.abstractDb.getEarthCoverageClasses()
            for lyr in auxClasses:
                layer = lyr[:-1]+lyr[-1].replace('a','c')
                dbName = self.widget.abstractDb.getDatabaseName()
                groupList =  qgis.utils.iface.legendInterface().groups()
                edgvLayer = self.layerFactory.makeLayer(self.widget.abstractDb, self.codeList, layer)
                if dbName in groupList:
                    edgvLayer.load(self.widget.crs,groupList.index(dbName))
                else:
                    self.parentTreeNode = qgis.utils.iface.legendInterface().addGroup(self.widget.abstractDb.getDatabaseName(), -1)
                    edgvLayer.load(self.widget.crs,self.parentTreeNode)
            
        except Exception as e:
                QgsMessageLog.logMessage(str(e.args[0]), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
                self.bar.pushMessage(self.tr("Error!"), self.tr("Could not load auxiliary classes! Check log for details!"), level=QgsMessageBar.CRITICAL)