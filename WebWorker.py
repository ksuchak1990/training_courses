## Import
from Worker import Worker
import requests

class WebWorker(Worker):
    """a worker augmented with handy functions for web stuff"""
    def __init__(self):
        super().__init__()

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
