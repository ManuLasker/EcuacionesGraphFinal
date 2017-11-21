# Creating an exception (error)

class Error(Exception):
    __input = ""
    def __init__(self,input):
        self.__input = input
        Exception.__init__(self,input)

    def getMessage(self):
        return self.__input