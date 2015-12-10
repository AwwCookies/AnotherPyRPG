import sys

from logbook import Logger, StreamHandler

settings = {
    "debug": True
}

class PyRPGObject:
    def __init__(self):
        StreamHandler(sys.stdout).push_application()
        self.log = Logger("AnotherPyRPG")
