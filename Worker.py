import os

class Worker():
    """class representing the generic worker, for which more specific workers inherit"""
    def __init__(self):
        self.product = 'generic'
        self.stageList = list()
        self.stageDict = dict()
        self.baseDir = 'output'

    def work(self):
        print(self.stageList)
        print(self.stageDict)
        # for stage in self.stageList:
        #     self.stageDict[stage]()
        #     pass

    # ensure that relevant output directories exist
    def initialChecks(self):
        outputPath = '{0}/{1}'.format(self.baseDir, self.product) if self.product != 'generic' else self.baseDir
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

    # get data from previous stage
    def pickUp():
        pass

    # output data at end of stage
    def putDown():
        pass
