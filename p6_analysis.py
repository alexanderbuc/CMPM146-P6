__author__ = 'Alexander'

from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    queue = []
    visited = []
    # TODO: fill in this function, populating the ANALYSIS dict
    init = sim.get_initial_state()
    moves = sim.get_moves()
    next_state = sim.get_next_state(init, moves[0])
    queue.append((init, [init]))
    visited.append(init)
    while queue:
        (prev,path) = queue.pop(0)
        for each in moves:
            next_state = sim.get_next_state(prev, each)
            if next_state not in ANALYSIS and next_state is not None:
                if next_state not in visited:
                    ANALYSIS[next_state] = path
                    queue.append((next_state, path + [next_state]))
                    visited.append(next_state)

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
     for each in ANALYSIS.keys():
        if i is each[0][0] and j is each[0][1]:
            path = ANALYSIS[each]
    raise NotImplementedError
