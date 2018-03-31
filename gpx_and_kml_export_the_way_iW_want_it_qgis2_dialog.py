# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPXandKMLExport_TheWayIWantItQGIS2Dialog
                                 A QGIS plugin
 this an almost fully customizable export shape to GPX or KML in QGIS 2
                             -------------------
        begin                : 2018-03-30
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Stefan Müller
        email                : Stefan.Mueller.83@gmail.com
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

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'gpx_and_kml_export_the_way_iW_want_it_qgis2_dialog_base.ui'))


class GPXandKMLExport_TheWayIWantItQGIS2Dialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GPXandKMLExport_TheWayIWantItQGIS2Dialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
