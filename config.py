from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(filename)s:%(funcName)s:%(lineno)s]- %(message)s")
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.DEBUG)
logger.addHandler(console)

DEBUG                       = logger.debug

INFO                        = logger.info

WARN                        = logger.warn

ERROR                       = logger.error

CRITICAL                    = logger.critical

EXCEPTION                   = logger.exception

GOOSE_DIRECTORY             = os.path.dirname(os.path.realpath(__file__))

DATASTORE_DIRECTORY         = os.path.join( GOOSE_DIRECTORY
                                          , "datastore"
                                          )

ICONS_DIRECTORY             = os.path.join( DATASTORE_DIRECTORY
                                          , "icons"
                                          )

COLORMAPS_DIRECTORY         = os.path.join( DATASTORE_DIRECTORY
                                          , "colormaps"
                                          )

IMAGES_DIRECTORY            = os.path.join( DATASTORE_DIRECTORY
                                          , "images"
                                          )

APPLICATION_ICON_PATH       = os.path.join( ICONS_DIRECTORY
                                          , "moose-icon.png"
                                          )

APPLICATION_BACKGROUND_PATH = os.path.join( IMAGES_DIRECTORY
                                          , "moose.png"
                                          )
