# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2016-06-22
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Luiz Andrade - Cartographic Engineer @ Brazilian Army
        email                : luiz.claudio@dsg.eb.mil.br
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
from qgis.core import QgsMessageLog
from DsgTools.ValidationTools.ValidationProcesses.validationProcess import ValidationProcess

class RecursiveSnapProcess(ValidationProcess):
    def __init__(self, postgisDb, iface):
        '''
        Constructor
        '''
        super(self.__class__,self).__init__(postgisDb, iface)
        self.processAlias = self.tr('Recursive Snap')
        
        classesWithElem = self.abstractDb.listClassesWithElementsFromDatabase(useComplex = False, primitiveFilter = ['a', 'l'])
        self.parameters = {'Snap': 5.0, 'Classes':classesWithElem.keys()}

    def execute(self):
        '''
        Reimplementation of the execute method from the parent class
        '''
        QgsMessageLog.logMessage(self.tr('Starting ')+self.getName()+self.tr(' Process.'), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
        try:
            self.setStatus(self.tr('Running'), 3) #now I'm running!
            classesWithElem = self.parameters['Classes']
            if len(classesWithElem) == 0:
                self.setStatus(self.tr('Empty database.'), 1) #Finished
                QgsMessageLog.logMessage(self.tr('Empty database.'), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
                return 1
            #getting parameters
            tol = self.parameters['Snap']
            for cl in classesWithElem:
                # preparation
                processTableName, lyr = self.prepareExecution(cl)
                self.abstractDb.recursiveSnap([processTableName], tol)
                # finalization
                self.postProcessSteps(processTableName, lyr)
                QgsMessageLog.logMessage(self.tr('All features from {} snapped successfully.').format(cl), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
            #setting status
            self.setStatus(self.tr('All features from snapped successfully.'), 1) #Finished
            return 1
        except Exception as e:
            QgsMessageLog.logMessage(':'.join(e.args), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
            self.finishedWithError()
            return 0