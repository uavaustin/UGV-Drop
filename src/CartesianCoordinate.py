import unittest

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

"""
Unit testing section
"""

class TestMethods(unittest.TestCase):

#test point class and its methods
    def testPointMethods(self):
        x = 10
        y = -6.5
        z = 21.4
        testPoint = point(x, y, z)

        self.assertEqual(testPoint.getX(), x)
        self.assertEqual(testPoint.getY(), y)
        self.assertEqual(testPoint.getZ(), z)

        testPoint.setX(-13)
        testPoint.setY(-2.0)
        testPoint.setZ(29.8888)

        self.assertEqual(testPoint.getX(), -13)
        self.assertEqual(testPoint.getY(), -2)
        self.assertEqual(testPoint.getZ(), 29.8888)

if __name__ == '__main__':
    unittest.main()
