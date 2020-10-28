class vector:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.__x = xComp
        self.__y = yComp
        self.__z = zComp
    def __str__(self):
        return ("Xv: "  + str(self.__x) + " Yv: " + str(self.__y) + " Zv: " + str(self.__z))

    #add component where it takes points and turns in into a vector

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z
