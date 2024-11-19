class Player():
    def __init__(self, playerName, playerGold):
        self.__playerName = playerName
        self.__playerGold = playerGold
        self.__playerHP = 500
        self.__playerTowerList = []
        self.__selectedTower = 0
        self.__unlockedLevel = 1


    def getPlayerNb(self):
        return self.__playerNb

    def getPlayerGold(self):
        return self.__playerGold
    
    def getPlayerHP(self):
        return self.__playerHP
    
    def getPlayerTowerList(self):
        return self.__playerTowerList

    def getSelectedTower(self):
        return self.__selectedTower
    
    def getUnlockedLevel(self):
        return self.__unlockedLevel


    def buyTower(self, towerCost):
        self.__playerGold -= towerCost

    def sellTower(self, towerCost):
        goldToAdd = int(towerCost/2)
        self.__playerGold += goldToAdd

    def winGold(self, gold):
        self.__playerGold += gold

    def setPlayerGold(self, gold):
        self.__playerGold += gold

    def setPlayerHP(self, newHP):
        self.__playerHP = newHP

    def loseHP(self, loseHP):
        self.__playerHP -= loseHP

    def addTowerToPlayer(self, newTower):
        self.__playerTowerList.append(newTower)

    def removeTowerToPlayer(self, removedTower):
        self.__playerTowerList.pop(removedTower)

    def setSelectedTower(self, newSelect):
        self.__selectedTower = newSelect

    def increaseUnlockedLevel(self):
        self.__unlockedLevel += 1
