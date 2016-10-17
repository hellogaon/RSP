#!/usr/python3
"""
==========
 RSP Game
==========

Created by : Sung woo Park.
===========================
Date : 2016.10.12

========== ========== =======
   COM        YOU    
========== ========== =======
Rock        Rock       Draw
Rock        Scissors   Lose
Rock        Paper      Win
Scissors    Rock       Win
Scissors    Scissors   Draw
Scissors    Paper      Lose
Paper       Rock       Lose
Paper       Scissors   Win
Paper       Paper      Draw
========== ========== =======

=============================

"""

import random
def RSP(you):
  """ 
    Do RSP Game.

    :param you: Your choice. (Rock, Scissors, Paper)
    :returns void: Nothing is returned.
  """
  rsp = ["Rock", "Scissors", "Paper"]
  random.shuffle(rsp)
  com = rsp[0]

  if((you==1 and com=="Rock") or (you==2 and com=="Scissors") or (you==3 and com=="Paper")):
    print("Computer: " + com + "\nDraw!")
  elif((you==1 and com=="Scissors") or (you==2 and com=="Paper") or (you==3 and com=="Rock")):
    print("Computer: " + com + "\nWin!")
  elif((you==1 and com=="Paper") or (you==2 and com=="Rock") or (you==3 and com=="Scissors")):
    print("Computer: " + com + "\nLose!")

if __name__ == "__main__":
  for _ in range(10):
    print("Choose 1)rock, 2)scissor: 3)paper: ",end="")
    you = int(input())
    RSP(you)