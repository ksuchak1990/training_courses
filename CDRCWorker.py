##Import
from WebWorker import WebWorker

class CDRCWorker(WebWorker):
    """worker to grab the CDRC info, process it, and output it"""
    def __init__(self):
        super().__init__()
        self.stages = {'catalogueDownload': self.downloadCatalogue, 'catalogueParse': self.parseCatalogue,
                        'eventsDownload': self.downloadEvents, 'eventsParse': self.parseEvents}

    def downloadCatalogue(self):
        pass

    def parseCatalogue(self):
        pass

    def downloadEvents(self):
        pass

    def parseEvents(self):
        pass

    def work(self):
        super().work()
