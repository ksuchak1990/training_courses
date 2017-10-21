##Import
from WebWorker import WebWorker

class CDRCWorker(WebWorker):
    """worker to grab the CDRC info, process it, and output it"""
    def __init__(self):
        super().__init__()
        self.stageList = ['catalogueDownload', 'catalogueParse', 'eventsDownload', 'eventsParse']
        self.stageDict = {'catalogueDownload': self.downloadCatalogue, 'catalogueParse': self.parseCatalogue, 
                            'eventsDownload': self.downloadEvents, 'eventsParse': self.parseEvents}
        self.product = 'CDRC'
        self.baseUrl = 'https://www.cdrc.ac.uk/events/'
        self.eventSplitter = '<!-- Event  -->'
        self.metadataSplitter = ''
        self.headerDict = {'a': 'Title', 'b': 'Date & Time', 'c': 'Venue', 'd': 'Description'}

    def downloadCatalogue(self):
        return self.requestURL(self.baseUrl)

    def parseCatalogue(self, code):
        restrictedCode = self.restrict(inputString=code, start='<!-- Events Loop -->', end='<!-- List Footer -->')

        eventList = restrictedCode.split(self.eventSplitter)[1:]
        urlList = [self.restrict(inputString=event, start='tribe-event-url" href="', end='" title=') for event in eventList]
        return urlList

    def downloadEvents(self, urlList):
        return [self.requestURL(url) for url in urlList]

    def parseEvents(self, code):
        ## Parse the event page to get the event metadata
        ## Isolate required text
        # restrictedCode = self.restrict(inputString=code, start='', end='')
        
        ## Split into sections
        # metadataList = restrictedCode.split(self.metadataSplitter)[1:]

        ## Clean up sections
        ## Make dictionary of metadata
        pass

