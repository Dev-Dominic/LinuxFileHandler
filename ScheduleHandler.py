
class ScheduleHandler():
    """ Used to schedule a given task on a linux system """

    def __init__(self, interval=0, command):
        self.intervalTime = interval
        self.command = command

    def runCommand(self):
        """
            Checks if less than a minute
            Uses crontab to set a schedule if interval is greater than or equal to a minute,
            otherwise uses starts process on boot cycles in a given amount of seconds 
        """
        if self.interval < 60: 
            os.system(command)
        else:
            pass


    def updateCommand(self, newCommand):
        pass

    def updateIntervalTime(self, newInterval):
        pass

    def getCommand(self):
        return self.command

    def getInterval(self):
        return self.interval


