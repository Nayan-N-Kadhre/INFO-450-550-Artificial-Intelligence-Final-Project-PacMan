'''
This file contains implementation of a Greedy Agent.
'''
import random

class GreedyAgent:
  def __str__(self):
    return "Greedy Agent"

  def getMove(self, problem):
    player = problem.state.turn
    moves = problem.getLegalMoves()

    scores = []
    for move in moves:
      nextState = problem.getSuccessor(move, problem.state)
      score = problem.evaluate(nextState, player)
      scores.append(score)

    best = max(scores)

    bestMoves = []
    for i in range(len(moves)):
      if scores[i] == best:
        bestMoves.append(moves[i])

    return random.choice(bestMoves)
