from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals

import pkg_resources
import os
from time import strftime, localtime


APPLICATION_BACKGROUND_IMAGE_PATH =
    pkg_resources.resource_filename(goose.__name__ , "data/images/moose.png")

RUN_SIMULATION_ICON_PATH    =
    pkg_resources.resource_filename(goose.__name__ , "data/icons/play.svg")

STOP_SIMULATION_ICON_PATH   =
    pkg_resources.resource_filename(goose.__name__ , "data/icons/pause.svg")

RESET_SIMULATION_ICON_PATH  =
    pkg_resources.resource_filename(goose.__name__ , "data/icons/stop.svg")


EXTENSIONS          = { "SBML"      :   ["xml"]
                      , "Python"    :   ["py"]
                      , "CSPACE"    :   ["cspace"]
                      , "Genesis"   :   ["g"]
                      , "NeuroML"   :   ["nml", "xml"]
                      }
MOOSE_ROOT_DIRECTORY    = os.path.expanduser("~/.moose/")
MOOSE_LOG               = "logs"
MOOSE_VERSION           = "3.1.0"
MOOSE_RUN_TIME          = strftime("%Y%m%d%H%M%S%Z", localtime())

MOOSE_LOG_DIRECTORY = os.path.join( MOOSE_ROOT_DIRECTORY
                                  , MOOSE_VERSION
                                  , MOOSE_LOG
                                  , MOOSE_RUN_TIME
                                  )
