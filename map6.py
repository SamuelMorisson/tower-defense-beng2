from ClassMonster import *
from ClassMap import *

map6Grid = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],  
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0], 
  [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  
  [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 1, 1, 3, 3, 0, 0, 0, 1, 1, 0, 1, 1, 2], 
  [2, 1, 1, 0, 1, 1, 0, 0, 0, 3, 3, 1, 1, 0, 1, 0, 0, 0, 0, 0], 
  [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  
  [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0], 
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],  
  [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0], 
  [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def fMonsterListMap6():
  monsterListMap6 = []
  monsterListMap6.append(Monster([0, 500], 10, 3))
  monsterListMap6.append(Monster([0, 500], 10, 5))
  monsterListMap6.append(Monster([0, 500], 10, 6))
  monsterListMap6.append(Monster([0, 500], 10, 7))
  monsterListMap6.append(Monster([0, 500], 40, 15))

  monsterListMap6.append(Monster([450, 0], 10, 3))
  monsterListMap6.append(Monster([450, 0], 20, 9))
  monsterListMap6.append(Monster([450, 0], 10, 10))
  monsterListMap6.append(Monster([450, 0], 30, 16))

  monsterListMap6.append(Monster([950, 450], 10, 3))
  monsterListMap6.append(Monster([950, 450], 20, 11))
  monsterListMap6.append(Monster([950, 450], 10, 13))
  monsterListMap6.append(Monster([950, 450], 50, 19))

  monsterListMap6.append(Monster([500, 950], 10, 3))
  monsterListMap6.append(Monster([500, 950], 30, 7))
  monsterListMap6.append(Monster([500, 950], 20, 11))


  monsterListMap6.append(Monster([0, 500], 40, 31))
  monsterListMap6.append(Monster([0, 500], 31, 35))
  monsterListMap6.append(Monster([0, 500], 10, 40))

  monsterListMap6.append(Monster([450, 0], 20, 32))
  monsterListMap6.append(Monster([450, 0], 20, 37))
  monsterListMap6.append(Monster([450, 0], 30, 39))
  monsterListMap6.append(Monster([450, 0], 50, 42))

  monsterListMap6.append(Monster([950, 450], 30, 32))
  monsterListMap6.append(Monster([950, 450], 10, 33))
  monsterListMap6.append(Monster([950, 450], 40, 36))
  monsterListMap6.append(Monster([950, 450], 10, 40))

  monsterListMap6.append(Monster([500, 950], 10, 30))
  monsterListMap6.append(Monster([500, 950], 10, 31))
  monsterListMap6.append(Monster([500, 950], 21, 35))
  monsterListMap6.append(Monster([500, 950], 10, 40))


  monsterListMap6.append(Monster([0, 500], 10, 52))
  monsterListMap6.append(Monster([0, 500], 30, 56))
  monsterListMap6.append(Monster([0, 500], 30, 59))
  monsterListMap6.append(Monster([0, 500], 51, 65))

  monsterListMap6.append(Monster([450, 0], 40, 53))
  monsterListMap6.append(Monster([450, 0], 50, 55))
  monsterListMap6.append(Monster([450, 0], 20, 57))
  monsterListMap6.append(Monster([450, 0], 21, 61))

  monsterListMap6.append(Monster([950, 450], 20, 52))
  monsterListMap6.append(Monster([950, 450], 21, 54))
  monsterListMap6.append(Monster([950, 450], 31, 60))

  monsterListMap6.append(Monster([500, 950],31, 52))
  monsterListMap6.append(Monster([500, 950],10, 54))
  monsterListMap6.append(Monster([500, 950],10, 55))
  monsterListMap6.append(Monster([500, 950],40, 58))
  return monsterListMap6