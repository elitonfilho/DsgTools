# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2018-07-26
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
from qgis.core import QgsProcessingProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.deaggregateGeometriesAlgorithm import DeaggregatorAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifySmallPolygonsAlgorithm import IdentifySmallPolygonsAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifySmallLinesAlgorithm import IdentifySmallLinesAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyDuplicatedGeometriesAlgorithm import IdentifyDuplicatedGeometriesAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyOutOfBoundsAnglesAlgorithm import IdentifyOutOfBoundsAnglesAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyOutOfBoundsAnglesInCoverageAlgorithm import IdentifyOutOfBoundsAnglesInCoverageAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyOverlapsAlgorithm import IdentifyOverlapsAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyGapsAndOverlapsInCoverageAlgorithm import IdentifyGapsAndOverlapsInCoverageAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyDanglesAlgorithm import IdentifyDanglesAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.identifyGapsAlgorithm import IdentifyGapsAlgorithm

from DsgTools.core.DSGToolsProcessingAlgs.Algs.GeometricAlgs.donutHoleExtractorAlgorithm import DonutHoleExtractorAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.OtherAlgs.updateOriginalLayerAlgorithm import UpdateOriginalLayerAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.topologicalCleanAlgorithm import TopologicalCleanAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.topologicalDouglasSimplificationAlgorithm import TopologicalDouglasSimplificationAlgorithm
from DsgTools.core.DSGToolsProcessingAlgs.Algs.ValidationAlgs.removeDuplicatedGeometriesAlgorithm import RemoveDuplicatedGeometriesAlgorithm

from qgis.PyQt.QtGui import QIcon

class DSGToolsProcessingAlgorithmProvider(QgsProcessingProvider):
    """
    Constructor
    """
    def __init__(self):
        super(DSGToolsProcessingAlgorithmProvider, self).__init__()
        self.algList = [DeaggregatorAlgorithm(), 
                        IdentifySmallPolygonsAlgorithm(), 
                        IdentifySmallLinesAlgorithm(), 
                        IdentifyDuplicatedGeometriesAlgorithm(),
                        IdentifyOutOfBoundsAnglesAlgorithm(),
                        IdentifyOutOfBoundsAnglesInCoverageAlgorithm(),
                        IdentifyOverlapsAlgorithm(),
                        IdentifyGapsAndOverlapsInCoverageAlgorithm(),
                        IdentifyDanglesAlgorithm(),
                        IdentifyGapsAlgorithm(),
                        DonutHoleExtractorAlgorithm(),
                        UpdateOriginalLayerAlgorithm(),
                        TopologicalCleanAlgorithm(),
                        TopologicalDouglasSimplificationAlgorithm(),
                        RemoveDuplicatedGeometriesAlgorithm()]

    def load(self):
        ProcessingConfig.settingIcons[self.name()] = self.icon()
        # Activate provider by default
        ProcessingConfig.addSetting(Setting(self.name(), 'ACTIVATE_DSGTools',
                                            'Activate', True))
        ProcessingConfig.readSettings()
        self.refreshAlgorithms()
        return True

    def unload(self):
        """
        Removes setting when the plugin is unloaded.
        """
        ProcessingConfig.removeSetting('ACTIVATE_DSGTools')

    def isActive(self):
        """
        Returns True if the provider is activated.
        """
        return ProcessingConfig.getSetting('ACTIVATE_DSGTools')

    def setActive(self, active):
        ProcessingConfig.setSettingValue('ACTIVATE_DSGTools', active)

    def id(self):
        """
        This is the name that will appear on the toolbox group.
        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'dsgtools'

    def name(self):
        """
        This is the localised full name.
        """
        return 'DSGTools'

    def icon(self):
        """
        We return the default icon.
        """
        return QIcon(':/plugins/DsgTools/icons/dsg.png')

    def loadAlgorithms(self):
        """
        Here we fill the list of algorithms in self.algs.
        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.
        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        for alg in self.algList:
            self.addAlgorithm(alg)