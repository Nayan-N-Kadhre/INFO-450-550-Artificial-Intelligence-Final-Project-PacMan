import problems as prb
import algorithms as alg

'''
This file contains demonstration of solving Pac-Man using two Greedy Algorithms, one for the player (Pac-Man) and one for the Adversary (Ghost) 
'''

demoGame = prb.Game(prb.PacMan(),alg.GreedyAgent(),alg.GreedyAgent())
demoGame.playGame()