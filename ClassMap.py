class Map:
    def __init__(self, levelMap, startingGold, monsterList):
        self.__levelMap = levelMap
        self.__startingGold = startingGold
        self.__monsterList = monsterList
        self.__resetMonsterList = monsterList
        self.__monsterLeft = len(monsterList)
        self.__end = []
        for i in range(len(levelMap)):
            for j in range(len(levelMap[i])):
                '''if levelMap[i][j] == 2:
                    self.__start = [i, j]'''
                if levelMap[i][j] == 3:
                    self.__end.append([i, j])
        


    def getLevelMap(self): #matrice de la carte
        return self.__levelMap

    def getStartingGold(self): #or de départ
        return self.__startingGold

    def getMoveList(self): #trajectoire effectuée par les monstres
        return self.__moveList

    def getMonsterList(self): #liste des monstres pour ce niveau
        return self.__monsterList
    
    def getResetMonsterList(self): #liste des monstres pour ce niveau
        return self.__resetMonsterList

    def getMonsterLeft(self): #point d'apparition des entités
        return self.__monsterLeft

    def getEnd(self): #point d'arrivée des entités
        return self.__end


    def setLevelMap(self, levelMap):
        self.__levelMap = levelMap

    def setStartingGold(self, startingGold):
        self.__startingGold = startingGold

    def setMoveList(self, moveList):
        self.__moveList = moveList

    def setMonstrList(self, monsterList):
        self.__monsterList = monsterList

    def decreaseMonsterLeft(self):
        self.__monsterLeft -= 1

    def setEnd(self, end):
        self.__end = end

