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


def constructPath(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def extractActions(path):
    actions_sequence = []
    for currState, nextState in zip(path, path[1:]):
        print(currState, nextState)
        if currState.boatIsOnLeftSide:
            missionaries_moved = currState.missionaries_left - nextState.missionaries_left
            cannibals_moved = currState.cannibals_left - nextState.cannibals_left
            direction = "left to right"
            actions_sequence.append((missionaries_moved, cannibals_moved, direction))
        else:
            missionaries_moved = nextState.missionaries_left - currState.missionaries_left
            cannibals_moved = nextState.cannibals_left - currState.cannibals_left
            direction = "right to left"
            actions_sequence.append((missionaries_moved, cannibals_moved, direction))
    return actions_sequence


def printSolution(actions_sequence):
    for action in actions_sequence:
        print("Move ", action[0], "Missionaries and ", action[1], "Cannibals from ", action[2])


# Make sure a certain action from the current state is feasible
def feasible(state, missionaries_to_move, cannibals_to_move):
    if state.boatIsOnLeftSide:
        return missionaries_to_move <= state.missionaries_left and cannibals_to_move <= state.cannibals_left
    return (3 - state.missionaries_left) >= missionaries_to_move and (3 - state.cannibals_left) >= cannibals_to_move


# Make sure a feasible action doesn't cause missionaries to be outnumbered by cannibals.
def legal(state, missionaries_to_move, cannibals_to_move):
    if state.boatIsOnLeftSide:
        return (state.missionaries_left - missionaries_to_move >= state.cannibals_left - cannibals_to_move
                or (state.missionaries_left - missionaries_to_move) == 0) \
               and (
               (3 - state.missionaries_left + missionaries_to_move) >= (3 - state.cannibals_left + cannibals_to_move)
               or (3 - state.missionaries_left + missionaries_to_move == 0))

    return (state.missionaries_left + missionaries_to_move >= state.cannibals_left + cannibals_to_move
            or (state.missionaries_left + missionaries_to_move) == 0) \
           and ((3 - state.missionaries_left - missionaries_to_move) >= (3 - state.cannibals_left - cannibals_to_move)
                or (3 - state.missionaries_left - missionaries_to_move == 0))


def validateAction(state, missionaries_to_move, cannibals_to_move):
    return feasible(state, missionaries_to_move, cannibals_to_move) and \
           legal(state, missionaries_to_move, cannibals_to_move)


# generate a new state from (state, action)
def exploreAction(parent_state, missionaries_to_move, cannibals_to_move):
    if parent_state.boatIsOnLeftSide:
        return State(parent_state.missionaries_left - missionaries_to_move,
                     parent_state.cannibals_left - cannibals_to_move,
                     not parent_state.boatIsOnLeftSide)
    else:
        return State(parent_state.missionaries_left + missionaries_to_move,
                     parent_state.cannibals_left + cannibals_to_move,
                     not parent_state.boatIsOnLeftSide)


potential_actions = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]


def generateGraph(start_state, end_state):
    list_of_nodes = [start_state]
    adjacency_matrix = {start_state: {}}
    frontier = [start_state]
    parent = {}

    while len(frontier) > 0:

        state = frontier.pop(0)
        # print(state)
        for act in potential_actions:
            isValid = validateAction(state, act[0], act[1])
            # print("validateAction({}, {}) == {}".format(state, act, isValid))
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
                    parent[newState] = state
                    if newState == end_state:
                        path = constructPath(parent, start_state, end_state)
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
        print("from {}: ".format(i), end="")
        for j in adjacency_matrix[i].keys():
            print(str(adjacency_matrix.get(i).get(j)), end=' , ')
        print()

    print(path)
    actions_sequence = extractActions(path)
    printSolution(actions_sequence)


start_state = State(3, 3, True)
end_state = State(0, 0, 0)
generateGraph(start_state, end_state)
