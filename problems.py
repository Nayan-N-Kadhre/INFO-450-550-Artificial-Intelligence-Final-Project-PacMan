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

   def showState(self, ms=600, state=None):

      if state is None:
         state = self.state
      
      img = np.zeros(360, 360, 3)
      
      for i in range(1, 3):
         cv2.line(img, (i * 120, 0), (i * 120, 360), (255, 255, 255), 2)
         cv2.line(img, (0, i * 120), (360, i * 120), (255, 255, 255), 2)

      def center(square):
         return (square[1] * 120 + 60, square[0] * 120 + 60)

      for r in range(3):
         for c in range(3):
            if state.pellets[r, c]:
               cv2.circle(img, center((r, c)), 12, (255, 255, 255), -1)
      cv2.circle(img, center(state.pacman), 45, (0, 255, 255), -1)
      cv2.circle(img, center(state.ghost), 45, (255, 255, 255), -1)
      cv2.imshow('Pac-Man', img)
      cv2.waitKey(ms)

   MOVES = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}

   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      if state.turn == 0:
         r, c = state.pacman
      else:
         r, c = state.ghost
      
      legalMoves = []
      for move, (dr, dc) in self.MOVES.items():
         newRow = r + dr
         newCol = c + dc
         if 0 <= newRow < 3 and 0 <= newCol < 3:
            legalMoves.append(move)
      return legalMoves

   def getSuccessor(self, move, state):
      r, c  = self.MOVES[move]
      pacman, ghost, pellets = state.pacman, state.shost, state.pellets
      if state.turn == 0:
         pacman = (pacman[0] + r, pacman[1] + c)
         pellets = pellets.copy()
         pellets[pacman] = False 
      else:
         ghost = (ghost[0] + r, ghost[1] + c)
      return PacManState(pacman, ghost, pellets, 1 - state.turn, state.moves + 1)

   def doMove(self, move):
      self.state = self.getSuccessor(move, self.state)

   def getWinner(self, state = None):
      if state is None:
         state = self.state
      if state.pacman == state.ghost:
         return 1
      if not state.pellets.any():
         return 0
      return -1

   def isTerminal(self, state = None):
      return self.getWinner(state) != -1


   


