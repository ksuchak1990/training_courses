## Import
from WebWorker import WebWorker

class ODPLWorker(WebWorker):
    """worker to grab the ODPL info, process it, and output it"""
    def __init__(self):
        super().__init__()
