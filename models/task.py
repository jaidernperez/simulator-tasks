from models import machine as machine


class task:

    def __init__(self, timeTask, machine):
        self.timeTask = timeTask
        self.machine = machine
        

    def getTimeTask(self):
        return self.timeTask

    
    
