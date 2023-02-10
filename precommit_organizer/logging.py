import logging

mylogger = logging.getLogger("precommit_organizer")
mylogger.setLevel(logging.INFO)

_formatter = logging.Formatter("%(name)s : [%(levelname)s ] %(asctime)s:  %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(_formatter)
mylogger.addHandler(stream_handler)
