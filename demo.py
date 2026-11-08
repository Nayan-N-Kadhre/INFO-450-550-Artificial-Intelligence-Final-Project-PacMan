import problems as prb
import algorithms as alg

'''
This file contains demonstration of solving Pac-Man using Greedy Algorithm, for both the player (Pac-Man) and for the Adversary (Ghost) 
'''

demoGame = prb.Game(prb.PacMan(),alg.GreedyAgent(),alg.GreedyAgent())
demoGame.playGame()