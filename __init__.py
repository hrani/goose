import sys
import traceback
from .config import *

def excepthook(exception_class, exception, tb):
    CRITICAL('{0}: {1}'.format(exception_class.__name__, exception))
    CRITICAL("\n" + "".join(traceback.format_tb(tb)))
    sys.exit()

sys.excepthook = excepthook
