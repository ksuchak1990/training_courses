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

    ## Web functions
    def requestURL(self, inputString):
        if not isinstance(inputString, str):
            raise TypeError('inputString must be a string') 
        r = requests.get(url=inputString)
        if r.status_code != 200:
            ## Don't think that this should be a StandardError, I'll need to find something more appropriate
            raise StandardError('Page request unsuccessful: status code {0}'.format(r.status_code))
        return(r.text)

    ## Text functions
    def restrict(self, inputString, start=None, end=None):
        ## Error cases:
        ## Ensure that inputString is string
        if not isinstance(inputString, str):
            raise TypeError('inputString must be a string')

        ## If start given then find start, else default to beginning
        c0 = inputString.index(start) + len(start) if start else 0
        
        ## If end given then find end, else default to end
        c1 = inputString.index(end) if end else len(inputString)
        
        ## Return text between start and end
        return(inputString[c0:c1])

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
        