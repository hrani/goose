import logging

LOGGER = logging.getLogger("goose")
LOGGER.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(filename)s:%(funcName)s:%(lineno)s]- %(message)s")
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.DEBUG)
LOGGER.addHandler(console)

DEBUG                       = logger.debug

INFO                        = logger.info

WARN                        = logger.warn

ERROR                       = logger.error

CRITICAL                    = logger.critical

EXCEPTION                   = logger.exception
