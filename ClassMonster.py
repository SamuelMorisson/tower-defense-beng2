import pygame

class Monster:
    def __init__(self, monsterCoord, monsterType, spawnTimer):
        self.__monsterCoord = monsterCoord
        self.__monsterNextCoord = monsterCoord
        self.__monsterVisitedCells = []
        self.__monsterType = monsterType
        self.__spawnTimer = spawnTimer
        self.__monsterFacing = []
        self.__monsterIsSpawned = False
        self.__monsterAlive = True
        self.__monsterEnd = False
        self.__isTargetedTick = -1
        if monsterType == 10:
            self.__monsterName = "Monstre Standard"
            self.__monsterHealth = 3
            self.__monsterSpeed = 2.5
            self.__monsterGold = 50
            self.__monsterSprite = pygame.image.load("Images\monster10.png")
            self.__monsterDamage = 100
        elif monsterType == 20:
            self.__monsterName = "Monstre Résistant"
            self.__monsterHealth = 7
            self.__monsterSpeed = 2
            self.__monsterGold = 100
            self.__monsterSprite = pygame.image.load("Images\monster20.png")
            self.__monsterDamage = 150
        elif monsterType == 21:
            self.__monsterName = "Monstre Résistant +"
            self.__monsterHealth = 10
            self.__monsterSpeed = 2.5
            self.__monsterGold = 150
            self.__monsterSprite = pygame.image.load("Images\monster21.png")
            self.__monsterDamage = 200
        elif monsterType == 30:
            self.__monsterName = "Monstre Rapide"
            self.__monsterHealth = 4
            self.__monsterSpeed = 50/16
            self.__monsterGold = 100
            self.__monsterSprite = pygame.image.load("Images\monster30.png")
            self.__monsterDamage = 100
        elif monsterType == 31:
            self.__monsterName = "Monstre Rapide +"
            self.__monsterHealth = 4
            self.__monsterSpeed = 5
            self.__monsterGold = 150
            self.__monsterSprite = pygame.image.load("Images\monster31.png")
            self.__monsterDamage = 150
        elif monsterType == 40:
            self.__monsterName = "Monstre Volant"
            self.__monsterHealth = 3
            self.__monsterSpeed = 2.5
            self.__monsterGold = 100
            self.__monsterSprite = pygame.image.load("Images\monster40.png")
            self.__monsterDamage = 100
        elif monsterType == 50:
            self.__monsterName = "Monstre Puissant"
            self.__monsterHealth = 7
            self.__monsterSpeed = 2.5
            self.__monsterGold = 150
            self.__monsterSprite = pygame.image.load("Images\monster50.png")
            self.__monsterDamage = 300
        elif monsterType == 51:
            self.__monsterName = "Monstre Boss"
            self.__monsterHealth = 12
            self.__monsterSpeed = 50/16
            self.__monsterGold = 200
            self.__monsterSprite = pygame.image.load("Images\monster51.png")
            self.__monsterDamage = 400
        elif monsterType == 5:
            self.__monsterName = "Monstre test"
            self.__monsterHealth = 5
            self.__monsterSpeed = 2.5
            self.__monsterGold = 200
            self.__monsterSprite = pygame.image.load("Images\monster4.png")
            self.__monsterDamage = 1


    def getMonsterCoord(self):
        return self.__monsterCoord
    
    def getMonsterNextCoord(self):
        return self.__monsterNextCoord
    
    def getMonsterVisitedCells(self):
        return self.__monsterVisitedCells

    def getMonsterX(self):
        return self.__monsterCoord[0]

    def getMonsterY(self):
        return self.__monsterCoord[1]

    def getMonsterType(self):
        return self.__monsterType

    def getSpawnTimer(self):
        return self.__spawnTimer
    
    def getMonsterFacing(self):
        return self.__monsterFacing

    def getMonsterIsSpawned(self):
        return self.__monsterIsSpawned

    def getMonsterAlive(self):
        return self.__monsterAlive

    def getMonsterEnd(self):
        return self.__monsterEnd
    
    def getIsTargetedTick(self):
        return self.__isTargetedTick
    

    def getMonstyerName(self):
        return self.__monsterName

    def getMonsterHealth(self):
        return self.__monsterHealth

    def getMonsterSpeed(self):
        return self.__monsterSpeed

    def getMonsterGold(self):
        return self.__monsterGold

    def getMonsterSprite(self):
        return self.__monsterSprite
    
    def getMonsterDamage(self):
        return self.__monsterDamage


    def monsterTestMove(self, direction):
        self.__monsterCoord[direction] += self.__monsterSpeed

    def setMonsterX(self, moveX):
        self.__monsterCoord[0] += moveX

    def setMonsterY(self, moveY):
        self.__monsterCoord[1] += moveY

    def monsterMove(self, move):
        for i in range(len(move)):
            self.__monsterCoord[i] += move[i]*self.__monsterSpeed

    def setMonsterNextCoord(self, nextCoord):
        self.__monsterNextCoord = nextCoord

    def setMonsterVisitedCells(self, newCell):
        self.__monsterVisitedCells.append(newCell)

    def monsterNewPosition(self, newPos):
        self.__monsterCoord = newPos

    def setMonsterFacing(self, newFacing):
        self.__monsterFacing = newFacing

    def monsterCanBeSpawned(self, newVal):
        self.__monsterIsSpawned = newVal

    def monsterIsDead(self):
        self.__monsterAlive = False
        self.__monsterCoord = [-100, -100]

    def monsterTakeDamage(self, damage):
        self.__monsterHealth -= damage
        '''print("--------")
        print(self.__monsterHealth)
        print(damage)'''
        if self.__monsterHealth <= 0:
            self.monsterIsDead()
            self.setMonsterEnd(True)
            return True
        return False
    
    def monsterCalculateDamage(self, damage):
        monsterHealth = self.__monsterHealth
        monsterHealth -= damage
        if monsterHealth <= 0:
            return True
        return False
        
    def setMonsterEnd(self, valueEnd):
        self.__monsterEnd = valueEnd

    def startTargetTick(self):
        self.__isTargetedTick = 10

    def decreaseTargetTick(self):
        self.__isTargetedTick -= 1

    def setMonsterIsTargetedTick(self):
        self.__isTargetedTick = -1


    def resetAllAttribute(self):
        pass


    """
    Pour la version finale:

    def move(self):
        self.position = (self.position[0] + self.vitesse, self.position[1])
        self.rect.center = self.position

    def monsterUpgrade(self):
        self.vitesse *= 2
        self.vie *= 1.25
        self.nombre *= 4"""