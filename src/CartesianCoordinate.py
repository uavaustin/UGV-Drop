class point:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.__x = xComp
        self.__y = yComp
        self.__z = zComp
    def __str__(self):
        return ("X: "  + str(self.__x) + " Y: " + str(self.__y) + " Z: " + str(self.__z))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def setX(self, newX: float):
        self.__x = newX

    def setY(self, newY: float):
        self.__y = newY

    def setZ(self, newZ: float):
        self.__z = newZ
