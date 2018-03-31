# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPXandKMLExport_TheWayIWantItQGIS2
                                 A QGIS plugin
 this an almost fully customizable export shape to GPX or KML in QGIS 2
                             -------------------
        begin                : 2018-03-30
        copyright            : (C) 2018 by Stefan Müller
        email                : Stefan.Mueller.83@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GPXandKMLExport_TheWayIWantItQGIS2 class from file GPXandKMLExport_TheWayIWantItQGIS2.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .gpx_and_kml_export_the_way_iW_want_it_qgis2 import GPXandKMLExport_TheWayIWantItQGIS2
    return GPXandKMLExport_TheWayIWantItQGIS2(iface)
