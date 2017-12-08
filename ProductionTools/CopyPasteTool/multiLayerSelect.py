# -*- coding: utf-8 -*-
"""
/***************************************************************************
multiLayerSelect
                                 A QGIS plugin
Builds a temp rubberband with a given size and shape.
                             -------------------
        begin                : 2016-08-02
        git sha              : $Format:%H$
        copyright            : (C) 2017 by  Jossan Costa - Surveying Technician @ Brazilian Army
                               (C) 2016 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : jossan.costa@eb.mil.br
                               borba.philipe@eb.mil.br
 ***************************************************************************/
Some parts were inspired by QGIS plugin MultipleLayerSelection
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.gui import QgsMapTool, QgsRubberBand
from qgis.core import QGis, QgsPoint, QgsRectangle, QgsMapLayer, QgsFeatureRequest, QgsDataSourceURI
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QColor, QMenu

import numpy as np
from PyQt4.QtCore import Qt

class MultiLayerSelection(QgsMapTool):
    finished = QtCore.pyqtSignal(list)
    def __init__(self, canvas, iface):
        """
        Tool Behaviours: (all behaviours start edition, except for rectangle one)
        1- Left Click: Clears previous selection, selects feature, sets feature layer as active layer. 
        The selection is done with the following priority: Point, Line then Polygon. 
        Selection is only done in visible layer.
        2- Control + Left Click: Adds to selection selected feature. This selection follows the priority in item 1.
        3- Right Click: Opens feature form
        4- Control + Right Click: clears selection and set feature's layer as activeLayer. activeLayer's definition
        follows priority of item 1;
        5- Shift + drag and drop: draws a rectangle, then features that intersect this rectangle are added to selection
        """
        self.iface = iface        
        self.canvas = canvas
        self.toolAction = None
        QgsMapTool.__init__(self, self.canvas)
        self.rubberBand = QgsRubberBand(self.canvas, QGis.Polygon)
        mFillColor = QColor( 254, 178, 76, 63 )
        self.rubberBand.setColor(mFillColor)
        self.rubberBand.setWidth(1)
        self.reset()
        self.blackList = ['moldura']
        self.iface.mapCanvas().setContextMenuPolicy(Qt.CustomContextMenu)
        self.iface.mapCanvas().customContextMenuRequested.connect(self.createContextMenu)
    
    def reset(self):
        """
        Resets rubber band.
        """
        self.startPoint = self.endPoint = None
        self.isEmittingPoint = False
        self.rubberBand.reset(QGis.Polygon)

    def canvasMoveEvent(self, e):
        """
        Used only on rectangle select.
        """
        if not self.isEmittingPoint:
            return
        self.endPoint = self.toMapCoordinates( e.pos() )
        self.showRect(self.startPoint, self.endPoint)

    def showRect(self, startPoint, endPoint):
        """
        Builds rubberband rect.
        """
        self.rubberBand.reset(QGis.Polygon)
        if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
            return
        point1 = QgsPoint(startPoint.x(), startPoint.y())
        point2 = QgsPoint(startPoint.x(), endPoint.y())
        point3 = QgsPoint(endPoint.x(), endPoint.y())
        point4 = QgsPoint(endPoint.x(), startPoint.y())
    
        self.rubberBand.addPoint(point1, False)
        self.rubberBand.addPoint(point2, False)
        self.rubberBand.addPoint(point3, False)
        self.rubberBand.addPoint(point4, True)    # true to update canvas
        self.rubberBand.show()

    def rectangle(self):
        """
        Builds rectangle from self.startPoint and self.endPoint
        """
        if self.startPoint is None or self.endPoint is None:
            return None
        elif self.startPoint.x() == self.endPoint.x() or self.startPoint.y() == self.endPoint.y():
            return None
        return QgsRectangle(self.startPoint, self.endPoint)

    def setAction(self, action):
        self.toolAction = action
        self.toolAction.setCheckable(True)
    
    def canvasReleaseEvent(self, e):
        """
        After the rectangle is built, here features are selected.
        """
        if QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.isEmittingPoint = False
            r = self.rectangle()
            layers = self.canvas.layers()
            for layer in layers:
                #ignore layers on black list and features that are not vector layers
                if layer.type() != QgsMapLayer.VectorLayer or (self.layerHasPartInBlackList(layer.name())):
                    continue
                if r is not None:
                    #builds bbRect and select from layer, adding selection
                    bbRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, r)
                    layer.select(bbRect, True)
            self.rubberBand.hide()

    def canvasPressEvent(self, e, filteredDict=False):
        """
        Method used to build rectangle if shift is held, otherwise, feature select/deselect and identify is done.
        """
        if QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.isEmittingPoint = True
            self.startPoint = self.toMapCoordinates(e.pos())
            self.endPoint = self.startPoint
            self.isEmittingPoint = True
            self.showRect(self.startPoint, self.endPoint)
        else:
            self.isEmittingPoint = False
            # selected =  (QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier)
            self.createContextMenu(e)
            # self.selectFeatures(e, hasControlModifyer = selected, filteredDict=filteredDict)
    
    def getCursorRect(self, e):
        """
        Calculates small cursor rectangle around mouse position. Used to facilitate operations
        """
        p = self.toMapCoordinates(e.pos())
        w = self.canvas.mapUnitsPerPixel() * 10
        return QgsRectangle(p.x()-w, p.y()-w, p.x()+w, p.y()+w)
    
    def layerHasPartInBlackList(self, lyrName):
        """
        Verifies if terms in black list appear on lyrName
        """
        for item in self.blackList:
            if item.lower() in lyrName.lower():
                return True
        return False
    
    def getPrimitiveDict(self, e, hasControlModifyer=False, filteredDict=False):
        """
        Builds a dict with keys as geometryTypes of layer, which are QGis.Point (value 0), QGis.Line (value 1) or QGis.Polygon (value 2),
        and values as layers from self.iface.legendInterface().layers(). When self.iface.legendInterface().layers() is called, a list of
        layers ordered according to lyr order in TOC is returned.

        Method altered:
        Added boolean parameter filteredDict to indicate whether a filtered 
        dictionary with ONLY the strongest type of geometry accordingly to 
        the hierarquy P (=0) > L (=1) > Pol (=2).
        Adapation meant for the createContextMenu method implemented.
        """
        #these layers are ordered by view order
        primitiveDict = dict()
        for lyr in self.iface.legendInterface().layers(): #ordered layers
            #layer types other than VectorLayer are ignored, as well as layers in black list and layers that are not visible
            if (lyr.type() != QgsMapLayer.VectorLayer) or (self.layerHasPartInBlackList(lyr.name())) or not self.iface.legendInterface().isLayerVisible(lyr):
                continue
            geomType = lyr.geometryType()
            if geomType not in primitiveDict.keys():
                primitiveDict[geomType] = []
            #removes selection
            if (not hasControlModifyer and e.button() == QtCore.Qt.LeftButton) or (hasControlModifyer and e.button() == QtCore.Qt.RightButton):
                lyr.removeSelection()
            primitiveDict[geomType].append(lyr)
        # finding strongest geometry
        if len(np.array(np.array(primitiveDict.keys()), 'int')) == 3:
            # if all 3 are present, then the strongests are point geometries
            strongest_geometry = 0
        else:
            strongest_geometry = np.array(np.array(primitiveDict.keys())[:,2], 'int').min()
        if filteredDict:
            # returning a dict containing only filtered layers
            primitiveDictFiltered = dict([])
            primitiveDictFiltered[strongest_geometry] = primitiveDict[strongest_geometry]
            return primitiveDictFiltered
        else:
            return primitiveDict

    def selectFeatures(self, e, bbRect=None, hasControlModifyer=False, filteredDict=False):
        """
        Method to select features acoording to mouse event e.
        Optional parameters:
        bbRect: if supplied, other rectangle is used
        hasControlModifyer: used to add to selection or not.
        """
        rect = self.getCursorRect(e)
        primitiveDict = self.getPrimitiveDict(e, hasControlModifyer = hasControlModifyer, filteredDict=filteredDict)
        primitives = primitiveDict.keys()
        primitives.sort() #this sort enables search to be done in the order of Point (value 0), Line (value 1) and Polygon (value 2)
        for primitive in primitives:
            for lyr in primitiveDict[primitive]:
                bbRect = self.canvas.mapSettings().mapToLayerCoordinates(lyr, rect)
                for feat in lyr.getFeatures(QgsFeatureRequest(bbRect)):
                    selectedIds = lyr.selectedFeaturesIds() #list of selected ids
                    featGeom = feat.geometry()
                    if not featGeom:
                        continue
                    if featGeom.intersects(bbRect): #tests if feature intersects tool bounding box, otherwise skip it
                        lyr.startEditing() #starts layer editting
                        if e.button() == QtCore.Qt.RightButton:
                            #set target, start edit and stop
                            if hasControlModifyer:
                                #sets active layer. Since hasControlModifyer indicates to this method to clear selection, this part of
                                #the code completes the  control + right click behaviour.
                                self.iface.setActiveLayer(lyr)
                                return
                            else:
                                #opens feature form. The tag showModal is to lock qgis window or not. 
                                #Current procedure is to imitate qgis way of doing things, so showModal = False
                                self.iface.openFeatureForm(lyr,feat, showModal=False)
                                return
                        #if code reaches here, it means that it is an incremental selection.
                        if feat.id() in selectedIds:
                            lyr.modifySelection([],[feat.id()])
                        else:
                            lyr.modifySelection([feat.id()],[])
                        if not hasControlModifyer:
                            self.iface.setActiveLayer(lyr)
                            return
                       
    def deactivate(self):
        """
        Deactivate tool.
        """
        try:
            if self.toolAction:
                self.toolAction.setChecked(False)
            if self is not None:
                QgsMapTool.deactivate(self)
        except:
            pass

    def activate(self):
        """
        Activate tool.
        """
        if self.toolAction:
            self.toolAction.setChecked(True)
        QgsMapTool.activate(self)

    def checkGeometryHierarquy(self, featureList=None):
        """
        TALVEZ NÃO USE

        Filtrate a list of features to only features of the
        strongest type of geometry (P (=0) > L (=1) > Pol (=2)).
        Returns the filtered list of ONLY the strongest features
        present
        arg featureList = [[feat_class_STR, feat_id_INT, feat_geom_type_INT]]     
        """
        filteredFeatureList = None
        if featureList:
            filteredFeatureList = []
            # choosing the strongest geometry type present in the list of features given 
            strongest_geometry = np.array(np.array(featureList)[:,2], 'int').min()
            for feature in featureList:
                if feature[2] == strongest_geometry:
                    filteredFeatureList.append(feature)
        return filteredFeatureList

    def setSelectionFeature(self, layer, feature):
        """
        Selects a given feature on canvas.
        """
        layer.setSelectedFeatures([feature.id()])
        return 

    def createContextMenu(self, e):
        """
        Creates the context menu for overlapping layers
        """
        menu = QMenu()
        selected =  (QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier)
        # setting a list of features to iterate over
        layerList = self.getPrimitiveDict(e, hasControlModifyer = selected, filteredDict=True)
        layers = layerList[layerList.keys()[0]]
        if layers:
            rect = self.getCursorRect(e)
            t = []
            for layer in layers:
                # iterate over features inside the mouse bounding box 
                bbRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)
                for feature in layer.getFeatures(QgsFeatureRequest(bbRect)):
                    if feature.geometry().intersects(rect):
                        """
                        # define the menu action name
                        s = '{0} (feat_id = {1})'.format(layer.name(), feature.id())
                        # create a menu action for each feature inside the mouse bounding box
                        menu.addAction(s, lambda: self.setSelectionFeature(layer, feature))
            # create an action that selects all features inside the bounding area (still filtered)
            menu.addAction(self.tr('Select All'), self.selectFeatures)
            menu.exec_(self.canvas.viewport().mapToGlobal(e.pos()))
            """
                        t.append([layer, feature])
            if len(t) > 1:
                for i in range(0, len(t)):
                    [layer, feature] = t[i]
                    uri = self.iface.activeLayer().dataProvider().dataSourceUri().split("'")[1]
                    s = '{0}.{1} (feat_id = {2})'.format(uri, layer.name(), feature.id())
                    menu.addAction(s, lambda: self.setSelectionFeature(layer, feature))
                menu.addAction(self.tr('Select All'), self.selectFeatures)
                menu.exec_(self.canvas.viewport().mapToGlobal(e.pos()))              
            elif t:                
                self.selectFeatures(e, hasControlModifyer = selected)
