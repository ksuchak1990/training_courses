## Imports

## Classes
# Worker
class Worker():
    """class representing the generic worker, for which more specific workers inherit"""
    def __init__(self):
        pass

class WebWorker(Worker):
    """a worker augmented with handy functions for web stuff"""
    def __init__(self):
        super(WebWorker, self).__init__()

class CDRCWorker(WebWorker):
    """worker to grab the CDRC info, process it, and output it"""
    def __init__(self):
        super(CDRCWorker, self).__init__()

class ODPLWorker(WebWorker):
    """worker to grab the ODPL info, process it, and output it"""
    def __init__(self):
        super(ODPLWorker, self).__init__()

class MailWorker(Worker):
    """worker to email out all of the processed info"""
    def __init__(self):
        super(MailWorker, self).__init__()

class Manager():
    """class that handles the overall running of the workers"""
    def __init__(self):
        pass
        