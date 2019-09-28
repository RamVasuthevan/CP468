# (missionaries_left, cannibals_left, missionaries_right, cannibals_right, boatIsOnLeftSide)

class State(object):
    missionaries_left = 0
    cannibals_left = 0
    boatIsOnLeftSide = True

    def __init__(self, missionaries_left, cannibals_left, boatIsOnLeftSide):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boatIsOnLeftSide = boatIsOnLeftSide

    def __str__(self):
        return "({},{},{})".format(self.missionaries_left, self.cannibals_left, self.boatIsOnLeftSide)

    def __repr__(self):
        return "({},{},{})".format(self.missionaries_left, self.cannibals_left, self.boatIsOnLeftSide)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boatIsOnLeftSide))

    def __eq__(self, other):
        return ((self.missionaries_left, self.cannibals_left, self.boatIsOnLeftSide) == (
        other.missionaries_left, other.cannibals_left, other.boatIsOnLeftSide))


def validateAction(state, missionaries_to_move, cannibals_to_move):
    if missionaries_to_move + cannibals_to_move > 2 or missionaries_to_move + cannibals_to_move < 1:
        #print("vAF1")
        return False

    if state.boatIsOnLeftSide:
        if state.missionaries_left >= missionaries_to_move \
                and state.cannibals_left >= cannibals_to_move \
                and ((state.missionaries_left - missionaries_to_move) >= (state.cannibals_left - cannibals_to_move) or (state.missionaries_left) == 0) \
                and (3 - state.missionaries_left + missionaries_to_move >= 3 - state.cannibals_left + cannibals_to_move or (3 - state.missionaries_left + missionaries_to_move) == 0):
            return True
        else:
            #print("vAF2")
            return False
    else:
        if (3 - state.missionaries_left) >= missionaries_to_move \
                and (3 - state.cannibals_left) >= cannibals_to_move \
                and (3 - state.missionaries_left - missionaries_to_move >= 3 - state.cannibals_left - cannibals_to_move or (3 - state.missionaries_left - missionaries_to_move) == 0)\
                and ((state.missionaries_left + missionaries_to_move) >= (state.cannibals_left + cannibals_to_move) or (state.missionaries_left + missionaries_to_move) == 0):
            return True
        else:
            #print("vAF3")
            return False


# generate a new state from (state, action)
def exploreAction(parent_state, missionaries_to_move, cannibals_to_move):
    if parent_state.boatIsOnLeftSide:
       return State(parent_state.missionaries_left - missionaries_to_move, parent_state.cannibals_left - cannibals_to_move,
                 not parent_state.boatIsOnLeftSide)
    else:
        return State(parent_state.missionaries_left + missionaries_to_move, parent_state.cannibals_left + cannibals_to_move,
                 not parent_state.boatIsOnLeftSide)


potential_actions = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]


def generateGraph(root_node):
    list_of_nodes = [root_node]
    adjacency_matrix = {root_node: {}}
    frontier = [root_node]

    while len(frontier) > 0:
        state = frontier.pop()
        #print(state)
        for act in potential_actions:
            isValid = validateAction(state, act[0], act[1])
            #print("validateAction({}, {}) == {}".format(state, act, isValid))
            if (isValid):
                newState = exploreAction(state, act[0], act[1])
                if newState in list_of_nodes:
                    if newState in adjacency_matrix[state].keys():
                        # repeat state, and we have been here before from this parent
                        continue
                    else:
                        # repeat state, but we have NOT been here before from this parent
                        adjacency_matrix[state][newState] = {newState}
                else:
                    # new state: never been here before
                    list_of_nodes.append(newState)
                    adjacency_matrix[state][newState] = {newState}
                    adjacency_matrix[newState] = {}
                    frontier.append(newState)
                    print("found new state: {} with act: {} from: {}".format(newState, act, state))

    for i in list_of_nodes:
        print(i, end=" , ")

    print("\n\n")

    for i in list_of_nodes:
        print("from {}: ".format(i), end= "")
        for j in adjacency_matrix[i].keys():
            print(str(adjacency_matrix.get(i).get(j)), end=' , ')
        print()


root = State(3, 3, True)
generateGraph(root)
