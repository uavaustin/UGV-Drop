class vector:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.__x = xComp
        self.__y = yComp
        self.__z = zComp

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z
