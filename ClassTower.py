import pygame

class Tower():
    def __init__(self, towerCoord, towerType):
        self.__towerCoord = towerCoord
        self.__towerType = towerType
        if towerType == 0:
            self.__towerName = "Tour 1"
            self.__cost = 100
            self.__towerDamage = 1
            self.__attackRange = 2
            self.__attackRate = 60
            self.__towerSprite = pygame.image.load("Images/tower1.png").convert()
        elif towerType == 1:
            self.__towerName = "Tour 2"
            self.__cost = 100
            self.__towerDamage = 1
            self.__attackRange = 3
            self.__attackRate = 60
            self.__towerSprite = pygame.image.load("Images/tower2.png").convert()
        elif towerType == 2:
            self.__towerName = "Tour 3"
            self.__cost = 100
            self.__towerDamage = 2
            self.__attackRange = 2
            self.__attackRate = 60
            self.__towerSprite = pygame.image.load("Images/tower3.png").convert()
        elif towerType == 3:
            self.__towerName = "Tour 4"
            self.__cost = 100
            self.__towerDamage = 1
            self.__attackRange = 2
            self.__attackRate = 30
            self.__towerSprite = pygame.image.load("Images/tower4.png").convert()
        self.__attackCooldown = 0

    def getTowerCoord(self):
        return self.__towerCoord

    def getTowerX(self):
        return self.__towerCoord[0]

    def getTowerY(self):
        return self.__towerCoord[1]

    def getTowerType(self):
        return self.__towerType

    def getTowerName(self):
        return self.__towerName

    def getTowerSprite(self):
        return self.__towerSprite

    def getCost(self):
        return self.__cost

    def getTowerDamage(self):
        return self.__towerDamage

    def getAttackRange(self):
        return self.__attackRange

    def getAttackRate(self):
        return self.__attackRate

    def getAttackCooldown(self):
        return self.__attackCooldown


    def setX(self, toAdd):
        self.__towerCoord[0] += toAdd

    def setY(self, toAdd):
        self.__towerCoord[1] += toAdd

    def setTowerCoord(self, newCoord):
        self.__towerCoord += newCoord

    def setAttackCooldown(self, newCD):
        self.__attackCooldown = newCD

    def tickAttackCooldown(self):
        self.__attackCooldown += 1

    def upgradeTower(self, newTowerType):
        self.__towerType = newTowerType
        if self.__towerType == 1:
            self.__towerName = "Tour 2"
            self.__cost = 100
            self.__towerDamage = 1
            self.__attackRange = 3
            self.__attackRate = 60
            self.__towerSprite = pygame.image.load("Images/tower2.png").convert()
        elif self.__towerType == 2:
            self.__towerName = "Tour 3"
            self.__cost = 100
            self.__towerDamage = 2
            self.__attackRange = 2
            self.__attackRate = 60
            self.__towerSprite = pygame.image.load("Images/tower3.png").convert()
        elif self.__towerType == 3:
            self.__towerName = "Tour 4"
            self.__cost = 100
            self.__towerDamage = 1
            self.__attackRange = 2
            self.__attackRate = 30
            self.__towerSprite = pygame.image.load("Images/tower4.png").convert()

