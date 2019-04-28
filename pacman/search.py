# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    # from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    inicio = problem.getStartState()
    aux = problem.getStartState()
    visitado = []
    visitado.append(inicio)
    estados = util.Stack()
    estadosLista = (inicio, [])
    estados.push(estadosLista)
    while not estados.isEmpty() and not problem.isGoalState(aux):
        estado, acoes = estados.pop()
        visitado.append(estado)
        proximo = problem.getSuccessors(estado)
        for i in proximo:
            coordenadas = i[0]
            if not coordenadas in visitado:
                aux = i[0]
                direcao = i[1]
                estados.push((coordenadas, acoes + [direcao]))
    return acoes + [direcao]
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    DICA: Utilizar util.PriorityQueue
    *** YOUR CODE HERE ***
    """
    inicio = problem.getStartState()
    visitado = []
    visitado.append(inicio)
    estados = util.Queue()
    estadoLista = (inicio, [])
    estados.push(estadoLista)
    while not estados.isEmpty():
        estado, acao = estados.pop()
        if problem.isGoalState(estado):
            return acao
        proximo = problem.getSuccessors(estado)
        for i in proximo:
            coordenadas = i[0]
            if not coordenadas in visitado:
                direcao = i[1]
                visitado.append(coordenadas)
                estados.push((coordenadas, acao + [direcao]))
    return acao
    util.raiseNotDefined()

    
def uniformCostSearch(problem):
    """Search the node of least total cost first.
    *** YOUR CODE HERE ***
    """
    inicio = problem.getStartState()
    visitado = []
    estados = util.PriorityQueue()
    estados.push((inicio, []) ,0)
    while not estados.isEmpty():
        estado, acoes = estados.pop()
        if problem.isGoalState(estado):
            return acoes
        if estado not in visitado:
            proximos = problem.getSuccessors(estado)
            for prox in proximos:
                coordenadas = prox[0]
                if coordenadas not in visitado:
                    direcoes = prox[1]
                    custo = acoes + [direcoes]
                    estados.push((coordenadas, acoes + [direcoes]), problem.getCostOfActions(custo))
        visitado.append(estado)
    return acoes
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    inicio = problem.getStartState()
    visitado = []
    estados = util.PriorityQueue()
    estados.push((inicio, []), nullHeuristic(inicio, problem))
    custo = 0
    while not estados.isEmpty():
        estado, acoes = estados.pop()
        if problem.isGoalState(estado):
            return acoes
        if estado not in visitado:
            proximos = problem.getSuccessors(estado)
            for prox in proximos:
                coordenadas = prox[0]
                if coordenadas not in visitado:
                    direcoes = prox[1]
                    nAcoes = acoes + [direcoes]
                    custo = problem.getCostOfActions(nAcoes) + heuristic(coordenadas, problem)
                    estados.push((coordenadas, acoes + [direcoes]), custo)
        visitado.append(estado)
    return acoes
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
