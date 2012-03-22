#/*##########################################################################
# Copyright (C) 2004-2012 European Synchrotron Radiation Facility
#
# This file is part of the PyMCA X-ray Fluorescence Toolkit developed at
# the ESRF by the Beamline Instrumentation Software Support (BLISS) group.
#
# This toolkit is free software; you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option) 
# any later version.
#
# PyMCA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PyMCA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# PyMCA follows the dual licensing model of Trolltech's Qt and Riverbank's PyQt
# and cannot be used as a free plugin for a non-free program. 
#
# Please contact the ESRF industrial unit (industry@esrf.fr) if this license 
# is a problem for you.
#############################################################################*/
import sys
import os
from PyMca import ConfigDict
from PyMca import PyMcaDataDir

dict = ConfigDict.ConfigDict()
dirmod = PyMcaDataDir.PYMCA_DATA_DIR 
dictfile = os.path.join(dirmod, "Scofield1973.dict")
if not os.path.exists(dictfile):
    dirmod = os.path.dirname(dirmod)
    dictfile = os.path.join(dirmod,"Scofield1973.dict")
    if not os.path.exists(dictfile):
        if dirmod.lower().endswith(".zip"):
            dirmod = os.path.dirname(dirmod)
    dictfile = os.path.join(dirmod,"Scofield1973.dict")
if not os.path.exists(dictfile):
    print("Cannot find file ", dictfile)
    raise IOError("Cannot find file %s " % dictfile)
dict.read(dictfile)


