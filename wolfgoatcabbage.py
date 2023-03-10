# Kaitlin Frani, Kelly Vu, Julian Ogata
# CPSC481-05 Project #1
from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'G', 'W', 'C'}), goal=frozenset()):
        super().__init__(initial, goal)

    def actions(self, state):
        movement = [{'F'}, {'G', 'F'}, {'W', 'F'}, {'C', 'F'}]
        length = len(state)

        # if {F, G, W, C}
        if length == 4:
            return [movement[1]]

        # if state == G
        if length == 1:
            if 'G' in state:
                return [movement[0]]
            if 'W' in state:
                return [movement[1]]
            if 'C' in state:
                return [movement[1]]

        # if Farmer and purchase aren't on the same side of the bank, they can't move together
        purchase = ['W', 'G', 'C']
        for item in purchase:
            if ('F' not in state) or (item not in state):
                movement.remove({item, 'F'})
        return movement

    def result(self, state, action):
        new_state = set(state)
        new_state = new_state.symmetric_difference(set(action))        
        return frozenset(new_state)

    def goal_test(self, state):
        return state == self.goal
 
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)