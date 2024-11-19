import pygame

class Projectile:
    def __init__(self, pStart, pEnd):
        self.__pStart = pStart
        self.__pEnd = pEnd
        self.__pTickLeft = 10
        self.__pSprite = pygame.image.load("Images\projectile.png").convert()


    def getPStart(self):
        return self.__pStart
    
    def getPStartX(self):
        return self.__pStart[0]
    
    def getPStartY(self):
        return self.__pStart[1]
    
    def getPEnd(self):
        return self.__pEnd
    
    def getPEndX(self):
        return self.__pEnd[0]
    
    def getPEndY(self):
        return self.__pEnd[1]
    
    def getPTickLeft(self):
        return self.__pTickLeft
    
    def getPSprite(self):
        return self.__pSprite
    
    
    def setPStart(self, newPStart):
        self.__pStart = newPStart
    
    def setPEnd(self, newPEnd):
        self.__pEnd = newPEnd
    
    def setPCoord(self, newPCoord):
        self.__pCoord = newPCoord
    
    def setPTickLeft(self, newPTickLeft):
        self.__pTickLeft = newPTickLeft

    def decreasePTickLeft(self):
        self.__pTickLeft -= 1


    '''
    Y = i
    X = j

    Start = (coord Tour) - 10px pour X et Y
    End = (coord Monstre) - 10px pour X et Y

    Coord = End-Start
    '''