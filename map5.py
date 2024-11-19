from ClassMonster import *
from ClassMap import *

map5Grid = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
  [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 3], 
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0], 
  [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], 
  [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]]


def fMonsterListMap5():
  monsterListMap5 = []
  monsterListMap5.append(Monster([0, 150], 10, 3))
  monsterListMap5.append(Monster([0, 150], 10, 6))
  monsterListMap5.append(Monster([0, 150], 10, 8))
  monsterListMap5.append(Monster([0, 150], 20, 12))
  monsterListMap5.append(Monster([0, 150], 30, 20))
  monsterListMap5.append(Monster([0, 150], 50, 24))

  monsterListMap5.append(Monster([0, 150], 31, 34))
  monsterListMap5.append(Monster([0, 150], 40, 37))
  monsterListMap5.append(Monster([0, 150], 20, 39))
  monsterListMap5.append(Monster([0, 150], 10, 40))
  monsterListMap5.append(Monster([0, 150], 10, 41))
  monsterListMap5.append(Monster([0, 150], 21, 45))
  monsterListMap5.append(Monster([0, 150], 40, 47))


  monsterListMap5.append(Monster([150, 950], 10, 4))
  monsterListMap5.append(Monster([150, 950], 10, 9))
  monsterListMap5.append(Monster([150, 950], 40, 13))
  monsterListMap5.append(Monster([150, 950], 10, 15))
  monsterListMap5.append(Monster([150, 950], 10, 16))
  monsterListMap5.append(Monster([150, 950], 21, 19))

  monsterListMap5.append(Monster([150, 950], 20, 34))
  monsterListMap5.append(Monster([150, 950], 20, 36))
  monsterListMap5.append(Monster([150, 950], 31, 38))
  monsterListMap5.append(Monster([150, 950], 10, 41))
  monsterListMap5.append(Monster([150, 950], 20, 42))
  monsterListMap5.append(Monster([150, 950], 21, 44))
  monsterListMap5.append(Monster([150, 950], 51, 48))


  return monsterListMap5