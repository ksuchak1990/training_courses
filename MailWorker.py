## Import
from Worker import Worker

class MailWorker(Worker):
    """worker to email out all of the processed info"""
    def __init__(self):
        super().__init__()
