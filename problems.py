'''
This file contains code for PacMan game problem. 

THe two players, Pacman and Ghost takes turns to play the game starting in a 3x3 grid in random position
Pacman wins by collecting all the pellets   
Ghost wins if it eats the PacMan before he can collects all the pellets
'''

import numpy as np
import cv2
import random

class Game:

    def __init__(self, problem, pZero, pOne,verbose=True):
      self.problem = problem      
      self.players = [pZero,pOne]   
      self.verbose = verbose   
      if self.verbose:
         self.problem.showState()               
    
    def playGame(self):
      pCur=0
      while self.problem.isTerminal()==False:           
         move = self.players[pCur].getMove(self.problem)           
         self.problem.doMove(move)
         if self.verbose:
            self.problem.showState()
            print(f"Move {self.problem.ticks}:")
            print(self.problem.state)
         pCur = np.abs(pCur-1)
        
      wIndex = self.problem.getWinner()
      winner = self.players[wIndex]
      if wIndex == -1:
         winner = "DRAW"
      #display final state
      print(f"The Winner is {winner} ({wIndex})!")
      if self.verbose:
         self.problem.showState(4000)
      return wIndex
         
class PacManState:

   def __init__(self, pacman, ghost, pellets, turn=0, moves=0):
      self.pacman = pacman
      self.ghost = ghost
      self.pellets = pellets
      self.turn = turn
      self.moves = moves

   def __str__(self):
      return f"Total moves: {self.moves}"

class PacMan:

   def __init__(self):
      squares = [(r, c) for r in range(3) for c in range(3)]
      pacman, ghost = random.sample(squares, 2)
      pellets = np.ones((3, 3), dtype=bool)
      pellets[pacman] = False
      pellets[ghost] = False
      self.state = PacManState(pacman, ghost, pellets)

