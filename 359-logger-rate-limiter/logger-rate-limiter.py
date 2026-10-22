class Logger:

    def __init__(self):
        self.messageDict = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageDict:
            self.messageDict[message] = timestamp
            return True
        else:
            lastTimestamp = self.messageDict[message]
            if timestamp - lastTimestamp >= 10:
                self.messageDict[message] = timestamp
                return True
        return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)