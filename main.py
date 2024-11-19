import pygame
from map1 import *
from map2 import *
from map3 import *
from map4 import *
from map5 import *
from map6 import *
from ClassTower import *
from ClassPlayer import *
from ClassMap import *
from ClassProjectile import *

from facingDirection import *

# Initialisations -----------------------------------------------------------------------------------------------------
pygame.init()

mouseCoord = None
cellMouseCoordX = None
cellMouseCoordY = None
roundMouseCoordX = None
roundMouseCoordY = None


mapGrid = None
playedMap = None
player1 = None


def displayText(openWindow, fontSize, textToDisplay, posX, posY, fontColor="#000000"):
    fontTowerLeft = pygame.font.Font('freesansbold.ttf', fontSize)
    finalDisplayText= fontTowerLeft.render(textToDisplay, 1, fontColor)
    openWindow.blit(finalDisplayText, (posX, posY))


window = pygame.display.set_mode((1400, 1000))

runningMenu = True
runningGame = False
endLevelScreen = True
runningApplication = True

# Plateau test

p1TowerList = None
monsterList = None
resetMonsterList = None
projectileList = None


# Création de la fenêtre
clock = pygame.time.Clock()
tickTimer = 0
secondTimer = tickTimer//60
pygame.display.set_caption('Tower Defense')


# Chargements images
grass = pygame.image.load("Images/grass50px.jpg").convert()
dirt = pygame.image.load("Images/dirt50px.jpg").convert()
portal = pygame.image.load("Images/portal50px.jpg").convert()
tower1 = pygame.image.load("Images/tower1.png").convert()
tower2 = pygame.image.load("Images/tower2.png").convert()
tower3 = pygame.image.load("Images/tower3.png").convert()
tower4 = pygame.image.load("Images/tower4.png").convert()
towerIcon1 = pygame.image.load("Images/towerIcon1.png").convert()
towerIcon2 = pygame.image.load("Images/towerIcon2.png").convert()
towerIcon3 = pygame.image.load("Images/towerIcon3.png").convert()
towerIcon4 = pygame.image.load("Images/towerIcon4.png").convert()
statTower1 = pygame.image.load("Images/statTower1.png").convert()
statUpgradeTower = pygame.image.load("Images/statUpgradeTower.png").convert()
green = pygame.image.load("Images/green40px.png").convert()
green.set_alpha(135)
endScreen = pygame.image.load("Images/endscreen.png").convert()
endScreen.set_alpha(135)

# Fonctions -----------------------------------------------------------------------------------------------------------
# Effets Visuels
def mouseOverGrass():
    global cellMouseCoordX
    global cellMouseCoordY
    for i in range(len(mapGrid)):
        if i == cellMouseCoordY:
            for j in range(len(mapGrid[i])):
                if j == cellMouseCoordX:
                    if mapGrid[i][j] == 0:
                        window.blit(green, ((j*50)+5, (i*50)+5))

def showTowerRange():
    for placedTower in range(len(p1TowerList)):
        currentTower = p1TowerList[placedTower]
        rangeRadius = (currentTower.getAttackRange()*50)+25
        if currentTower.getTowerCoord() == [roundMouseCoordX, roundMouseCoordY]:
            drawRange = pygame.Surface((rangeRadius*2, rangeRadius*2), pygame.SRCALPHA)
            pygame.draw.circle(drawRange, (255, 255, 255, 40), (rangeRadius, rangeRadius), rangeRadius)
            window.blit(drawRange, (roundMouseCoordX-rangeRadius+25, roundMouseCoordY-rangeRadius+25))

def newProjectile(attackingTower, attackedMonster):
    coordTower = attackingTower.getTowerCoord()
    coordMonster = attackedMonster.getMonsterCoord()
    xStart = coordTower[0] + 10
    yStart = coordTower[1] + 10
    xEnd = coordMonster[0] + 10
    yEnd = coordMonster[1] + 10
    projectile = Projectile([xStart, yStart], [xEnd, yEnd])
    projectileList.append(projectile)

def projectileAnimation():
    for projectile in projectileList:
        if projectile.getPTickLeft() == 0:
            projectileList.pop(0)
        else:
            distX = projectile.getPEndX() - projectile.getPStartX()
            distY = projectile.getPEndY() - projectile.getPStartY()
            calculTick = 1 - (projectile.getPTickLeft() / 10)
            pCoordX = projectile.getPStartX() + (distX * calculTick)
            pCoordY = projectile.getPStartY() + (distY * calculTick)
            window.blit(projectile.getPSprite(), (pCoordX, pCoordY))
            projectile.decreasePTickLeft()

# Tours
def addTower():
    global cellMouseCoordX
    global cellMouseCoordY
    goldLeft = player1.getPlayerGold()
    for i in range(len(mapGrid)):
        if i == cellMouseCoordY:
            for j in range(len(mapGrid[i])):
                if j == cellMouseCoordX:
                   if mapGrid[i][j] == 0:
                        coordTowerList = []
                        for objectTower in p1TowerList:
                            coordTowerList.append(objectTower.getTowerCoord())
                        if [j*50,i*50] not in coordTowerList and player1.getSelectedTower() == 0:
                            newTower = Tower([j*50,i*50], player1.getSelectedTower())
                            p1TowerList.append(newTower)
                            if (goldLeft - newTower.getCost()) < 0:
                                deleteTower(None)
                            else:
                                player1.buyTower(newTower.getCost())
                        elif [j*50,i*50] in coordTowerList and player1.getSelectedTower() != 0:
                            # Upgrade Tower
                            for objectTower in p1TowerList:
                                if objectTower.getTowerCoord() == [j*50,i*50] and player1.getPlayerGold() >= 100:
                                    objectTower.upgradeTower(player1.getSelectedTower())
                                    player1.buyTower(objectTower.getCost())

def deleteTower(why):
    for placedTower in range(len(p1TowerList)):
        currentTower = p1TowerList[placedTower]
        if currentTower.getTowerCoord() == [roundMouseCoordX, roundMouseCoordY]:
            if why == 1:
                if currentTower.getTowerType() == 0:
                    player1.sellTower(currentTower.getCost())
                else:
                    player1.sellTower((currentTower.getCost())*2)
            p1TowerList.pop(placedTower)
            break

def autoAttackTower():
    global monsterPosTest
    global monsterList
    for placedTower in range(len(p1TowerList)):
        currentTower = p1TowerList[placedTower]
        monsterList = playedMap.getMonsterList()
        for spawnedMonster in range(len(monsterList)):
            currentMonster = monsterList[spawnedMonster]
            currentMonsterCoord = currentMonster.getMonsterCoord()
            rangeTower = (currentTower.getAttackRange()*50)+25
            centerTower = [(currentTower.getTowerX())+25, (currentTower.getTowerY())+25]
            monsterHurtbox = [currentMonsterCoord, [currentMonsterCoord[0]+50, currentMonsterCoord[1]], [currentMonsterCoord[0], currentMonsterCoord[1]+50], [currentMonsterCoord[0]+50, currentMonsterCoord[1]+50]] #HG - HD - BG - BD
            for mhb in monsterHurtbox:
                distMonX = (mhb[0]-centerTower[0])**2
                distMonY = (mhb[1]-centerTower[1])**2
                distTot = (distMonX + distMonY)**0.5
                if distTot < rangeTower:
                    if currentTower.getAttackCooldown() == 0 and currentMonster.getMonsterIsSpawned() == True:
                        if currentMonster.getMonsterType() == 40:
                            if currentTower.getTowerType() == 1:
                                currentTower.tickAttackCooldown()
                                newProjectile(currentTower, currentMonster)
                                currentMonster.startTargetTick()
                        else:
                            currentTower.tickAttackCooldown()
                            newProjectile(currentTower, currentMonster)
                            currentMonster.startTargetTick()

    for spawnedMonster in range(len(monsterList)):
        currentMonster = monsterList[spawnedMonster]
        if currentMonster.getIsTargetedTick() == 0:
            if currentMonster.monsterCalculateDamage(currentTower.getTowerDamage()) == True:
                currentMonster.monsterTakeDamage(currentTower.getTowerDamage())
                currentMonster.setMonsterIsTargetedTick()
                player1.winGold(currentMonster.getMonsterGold())
                playedMap.decreaseMonsterLeft()
            else:
                currentMonster.setMonsterIsTargetedTick()
                currentMonster.monsterTakeDamage(currentTower.getTowerDamage())
        elif currentMonster.getIsTargetedTick() > 0:
            currentMonster.decreaseTargetTick()
               
def allTowerAttackCooldown():
    for placedTower in range(len(p1TowerList)):
        if p1TowerList[placedTower].getAttackCooldown() != 0:
            if p1TowerList[placedTower].getAttackCooldown() == p1TowerList[placedTower].getAttackRate():
                p1TowerList[placedTower].setAttackCooldown(0)
            else:
                p1TowerList[placedTower].tickAttackCooldown()

def buttonChooseTower(mouseCoord):
    if 1015 <= mouseCoord[0] <= 1115 and 185 <= mouseCoord[1] <= 285:
        player1.setSelectedTower(0)
    elif 1015 <= mouseCoord[0] <= 1115 and 365 <= mouseCoord[1] <= 465:
        player1.setSelectedTower(1)
    elif 1150 <= mouseCoord[0] <= 1250 and 365 <= mouseCoord[1] <= 465:
        player1.setSelectedTower(2)
    elif 1285 <= mouseCoord[0] <= 1385 and 365 <= mouseCoord[1] <= 465:
        player1.setSelectedTower(3)

def displayButtonChooseTower():
    color0 = "#969696"
    color1 = "#969696"
    color2 = "#969696"
    color3 = "#969696"
    if player1.getSelectedTower() == 0:
        color0 = "#ffffff"
    elif player1.getSelectedTower() == 1:
        color1 = "#ffffff"
    elif player1.getSelectedTower() == 2:
        color2 = "#ffffff"
    elif player1.getSelectedTower() == 3:
        color3 = "#ffffff"
    pygame.draw.rect(window, color0, (1015, 185, 100, 100))
    pygame.draw.rect(window, color1, (1015, 365, 100, 100))
    pygame.draw.rect(window, color2, (1150, 365, 100, 100))
    pygame.draw.rect(window, color3, (1285, 365, 100, 100))
    window.blit(towerIcon1, (1025, 195))
    window.blit(towerIcon2, (1025, 375))
    window.blit(towerIcon3, (1160, 375))
    window.blit(towerIcon4, (1295, 375))

# Monsters
def displayMonsters():
    global monsterList
    for objectMonster in range(len(monsterList)):
            currentMonster = monsterList[objectMonster]
            if currentMonster.getMonsterIsSpawned() == False:
                if currentMonster.getSpawnTimer() <= secondTimer:
                    monsterList[objectMonster].monsterCanBeSpawned(True)

            elif currentMonster.getMonsterEnd() == False:
                window.blit(currentMonster.getMonsterSprite(), currentMonster.getMonsterCoord())

                end = playedMap.getEnd()
                coordMonsterX = currentMonster.getMonsterCoord()[0]
                coordMonsterY = currentMonster.getMonsterCoord()[1]
                coordMonster = [coordMonsterY/50, coordMonsterX/50,]
                if coordMonster in end:
                    currentMonster.setMonsterEnd(True)
                    player1.loseHP(currentMonster.getMonsterDamage())


                if currentMonster.getMonsterCoord() == currentMonster.getMonsterNextCoord():
                    map = playedMap.getLevelMap()
                    for i in range(len(map)):
                        for j in range(len(map[i])):
                            coordMap = [j*50, i*50]
                            if coordMap == currentMonster.getMonsterCoord():
                                if i < (len(map))-1 and map[i+1][j] >= 1 and [i+1, j] not in currentMonster.getMonsterVisitedCells():
                                    #print("SUD")
                                    currentMonster.setMonsterNextCoord([j*50, (i+1)*50])
                                    currentMonster.setMonsterVisitedCells([i, j])
                                    currentMonster.setMonsterFacing(south)
                                    currentMonster.monsterMove(south)
                                elif i > 0 and map[i-1][j] >= 1 and [i-1, j] not in currentMonster.getMonsterVisitedCells():
                                    #print("NORD")
                                    currentMonster.setMonsterNextCoord([j*50, (i-1)*50])
                                    currentMonster.setMonsterVisitedCells([i, j])
                                    currentMonster.setMonsterFacing(north)
                                    currentMonster.monsterMove(north)
                                elif j < (len(map[i]))-1 and map[i][j+1] >= 1 and [i, j+1] not in currentMonster.getMonsterVisitedCells():
                                    #print("EST")
                                    currentMonster.setMonsterNextCoord([(j+1)*50, i*50])
                                    currentMonster.setMonsterVisitedCells([i, j])
                                    currentMonster.setMonsterFacing(east)
                                    currentMonster.monsterMove(east)
                                elif j > 0 and map[i][j-1] >= 1 and [i, j-1] not in currentMonster.getMonsterVisitedCells():
                                    #print("OUEST")
                                    currentMonster.setMonsterNextCoord([(j-1)*50, i*50])
                                    currentMonster.setMonsterVisitedCells([i, j])
                                    currentMonster.setMonsterFacing(west)
                                    currentMonster.monsterMove(west)
                else:
                    monsterList[objectMonster].monsterMove(monsterList[objectMonster].getMonsterFacing())

# Gameplay
def mouseGameCoord():
    global mouseCoord
    global cellMouseCoordX
    global cellMouseCoordY
    global roundMouseCoordX
    global roundMouseCoordY

    mouseCoord = pygame.mouse.get_pos()
    cellMouseCoordX = (mouseCoord[0]//50)
    cellMouseCoordY = (mouseCoord[1]//50)
    roundMouseCoordX = (cellMouseCoordX*50)
    roundMouseCoordY = (cellMouseCoordY*50)

def pygameEvents():
    global runningGame
    global endLevelScreen
    global runningApplication
    global mouseCoord
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mouseCoord[0] < 1000:
                addTower()
            else:
                buttonChooseTower(mouseCoord)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            deleteTower(1)
        if event.type == pygame.QUIT:
            endLevelScreen = False
            runningGame = False
            runningApplication = False


# Boucle Menu----------------------------------------------------------------------------------------------------------
def runMenu():
    global player1
    global playedMap
    global runningMenu
    global runningGame
    global runningApplication
    global mapGrid

    global mouseCoord
    global cellMouseCoordX
    global cellMouseCoordY
    global roundMouseCoordX
    global roundMouseCoordY

    while runningMenu:

        mouseGameCoord()
        window.fill((255, 255, 255))
        colorButton1 = colorButton2 = colorButton3 = colorButton4 = colorButton5 = colorButton6 = "#cfcfcf"
        if 180 <= mouseCoord[0] < 630 and 350 <= mouseCoord[1] < 510:
            colorButton1 = "#e3e3e3"
        elif 180 <= mouseCoord[0] < 630 and 565 <= mouseCoord[1] < 725:
            colorButton2 = "#e3e3e3"
        elif 180 <= mouseCoord[0] < 630 and 780 <= mouseCoord[1] < 940:
            colorButton3 = "#e3e3e3"
        elif 770 <= mouseCoord[0] < 1220 and 350 <= mouseCoord[1] < 510:
            colorButton4 = "#e3e3e3"
        elif 770 <= mouseCoord[0] < 1220 and 565 <= mouseCoord[1] < 725:
            colorButton5 = "#e3e3e3"
        elif 770 <= mouseCoord[0] < 1220 and 780 <= mouseCoord[1] < 940:
            colorButton6 = "#e3e3e3"
        pygame.draw.rect(window, colorButton1, (180, 350, 450, 160))
        pygame.draw.rect(window, colorButton2, (180, 565, 450, 160))
        pygame.draw.rect(window, colorButton3, (180, 780, 450, 160))
        pygame.draw.rect(window, colorButton4, (770, 350, 450, 160))
        pygame.draw.rect(window, colorButton5, (770, 565, 450, 160))
        pygame.draw.rect(window, colorButton6, (770, 780, 450, 160))

        displayText(window, 80, "Tower Defense", 390, 150)

        displayText(window, 30, "Carte 1", 200, 370)
        displayText(window, 30, "Carte 2", 200, 585)
        displayText(window, 30, "Carte 3", 200, 800)
        displayText(window, 30, "Carte 4", 790, 370)
        displayText(window, 30, "Carte 5", 790, 585)
        displayText(window, 30, "Carte 6", 790, 800)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningMenu = False
                runningApplication = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Map 1
                if 180 <= mouseCoord[0] < 630 and 350 <= mouseCoord[1] < 510:
                    playedMap = Map(map1Grid, 500, fMonsterListMap1())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False

                # Map 2
                elif 180 <= mouseCoord[0] < 630 and 565 <= mouseCoord[1] < 725:
                    playedMap = Map(map2Grid, 300, fMonsterListMap2())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False
                
                # Map 3
                elif 180 <= mouseCoord[0] < 630 and 780 <= mouseCoord[1] < 940:
                    playedMap = Map(map3Grid, 300, fMonsterListMap3())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False
                
                # Map 4
                elif 770 <= mouseCoord[0] < 1220 and 350 <= mouseCoord[1] < 510:
                    playedMap = Map(map4Grid, 400, fMonsterListMap4())
                    for monster in playedMap.getMonsterList():
                        print(monster.getMonsterEnd())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False
                
                # Map 5
                elif 770 <= mouseCoord[0] < 1220 and 565 <= mouseCoord[1] < 725:
                    playedMap = Map(map5Grid, 500, fMonsterListMap5())
                    for monster in playedMap.getMonsterList():
                        print(monster.getMonsterEnd())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False
                
                # Map 6
                elif 770 <= mouseCoord[0] < 1220 and 780 <= mouseCoord[1] < 940:
                    playedMap = Map(map6Grid, 600, fMonsterListMap6())
                    for monster in playedMap.getMonsterList():
                        print(monster.getMonsterEnd())
                    player1 = Player(1, playedMap.getStartingGold())
                    mapGrid = playedMap.getLevelMap()
                    runningGame = True
                    runningMenu = False
                    
        pygame.display.flip()

# Boucle Jeu-----------------------------------------------------------------------------------------------------------
def runGame():
    global runningGame
    global endLevelScreen
    global runningMenu
    global runningApplication
    
    global tickTimer
    global secondTimer
    tickTimer = 0

    global mouseCoord
    global cellMouseCoordX
    global cellMouseCoordY
    global roundMouseCoordX
    global roundMouseCoordY
    global p1TowerList

    while runningGame:

        mouseGameCoord()
        tickTimer += 1
        secondTimer = tickTimer//60

        # Plateau de jeu-------------------------------------------

        # Affichage plateau
        window.fill((0, 0, 0))
        for i in range(len(mapGrid)):
            for j in range(len(mapGrid[i])):
                if mapGrid[i][j] == 0:
                    window.blit(grass, (j*50, i*50))
                elif mapGrid[i][j] == 1:
                    window.blit(dirt, (j*50, i*50))
                elif mapGrid[i][j] > 1:
                    window.blit(portal, (j*50, i*50))


        # Lancement fonctions
        mouseOverGrass()
        showTowerRange()
        autoAttackTower()
        allTowerAttackCooldown()
        displayMonsters()
        projectileAnimation()

        # Interface de droite--------------------------------------
        actions = pygame.draw.rect(window, "#969696", (1000, 0, 400, 1000)) # (Optionnel: Remplacer fond par image OU Couleur personnalisable)
        # Texte Or restant
        textTowerLeft = "Or: " + str(player1.getPlayerGold())
        displayText(window, 28, textTowerLeft, 1215, 75)
        '''# Texte Coordonnées souris
        textCoordMouseX = "X: " + str(mouseCoord[0])
        textCoordMouseY = "Y: " + str(mouseCoord[1])
        displayText(window, 20, textCoordMouseX, 1020, 970)
        displayText(window, 20, textCoordMouseY, 1110, 970)'''
        # Texte chronomètre
        textTimer = "Timer: " + str(secondTimer)
        displayText(window, 24, textTimer, 1015, 15)
        p1HP = player1.getPlayerHP()
        if p1HP < 0:
            p1HP = 0
        textPlayerHP = "PV: " + str(p1HP)
        displayText(window, 28, textPlayerHP, 1015, 75)
        displayText(window, 36, "Placer une Tour", 1015, 140)
        displayText(window, 36, "Améliorer une Tour", 1015, 320)
        window.blit(statTower1, (1130, 195))
        window.blit(statUpgradeTower, (1015, 470))
        displayText(window, 20, "Tir aérien", 1015, 560, "#128218")
        monsterLeft = "Monstres restant: " + str(playedMap.getMonsterLeft())
        displayText(window, 28, monsterLeft, 1015, 640)
        '''#Tower 1
        displayText(window, 20, "Dégâts: 1", 1130, 195)
        displayText(window, 20, "Portée: 2", 1130, 225)
        displayText(window, 20, "Vitesse de tir: 1s", 1130, 255)

        #Tower 2
        displayText(window, 20, "Dégâts: 1", 1015, 470)
        displayText(window, 20, "Portée: 3", 1015, 500, "#128218")
        displayText(window, 20, "Vitesse: 1", 1015, 530)
        displayText(window, 20, "Tir aérien", 1015, 560, "#128218")

        #Tower 3
        displayText(window, 20, "Dégâts: 2", 1150, 470, "#128218")
        displayText(window, 20, "Portée: 2", 1150, 500)
        displayText(window, 20, "Vitesse: 1", 1150, 530)

        #Tower 4
        displayText(window, 20, "Dégâts: 1", 1285, 470)
        displayText(window, 20, "Portée: 2", 1285, 500)
        displayText(window, 20, "Vitesse: 0.5", 1285, 530, "#128218")'''

        displayButtonChooseTower()
        pygameEvents()

        # Affichage tours
        for objectTower in p1TowerList:
            window.blit(objectTower.getTowerSprite(), (objectTower.getTowerCoord()))

        victory = True
        if player1.getPlayerHP() <= 0:
            print("DEFAITE")
            victory = False
            window.blit(endScreen, (0, 0))
            displayText(window, 100, "Défaite", 300, 450)
            runningGame = False

        checkMonster = 0
        for monster in range(len(monsterList)):
            if monsterList[monster].getMonsterEnd() == True:
                checkMonster += 1
        if checkMonster == len(monsterList) and victory == True:
            print("VICTOIRE")
            window.blit(endScreen, (0, 0))
            displayText(window, 100, "Victoire", 300, 450)
            runningGame = False

        pygame.display.flip()
        clock.tick(60)
    print(endLevelScreen)
    while endLevelScreen:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                endLevelScreen = False
                runningMenu = True
            if event.type == pygame.QUIT:
                endLevelScreen = False
                runningApplication = False
        

# ---------------------------------------------------------------------------------------------------------------------

def main():
    global p1TowerList
    global monsterList
    global projectileList
    global endLevelScreen
    while runningApplication:
        runMenu()
        if runningGame == True:
            p1TowerList = player1.getPlayerTowerList()
            resetMonsterList = playedMap.getResetMonsterList()
            monsterList = resetMonsterList
            projectileList = []
            endLevelScreen = True
            runGame()

main()
 
pygame.quit()