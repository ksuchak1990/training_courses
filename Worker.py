class Worker():
    """class representing the generic worker, for which more specific workers inherit"""
    def __init__(self):
        self.stages = dict()

    def work(self):
        print(self.stages)
        for k, v in self.stages.items():
            ## run the relevant function
            pass

    def initialChecks(self):
        ## for each stage, make sure that there is the relevant folder in which to output
        pass
