import bisect
import sys


class Problem:

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        raise NotImplementedError

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):

        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0

        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):

        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):

        next_state = problem.result(self.state, action)

        return Node(
            next_state,
            self,
            action,
            problem.path_cost(
                self.path_cost,
                self.state,
                action,
                next_state
            )
        )

    def solution(self):

        return [node.action for node in self.path()[1:]]

    def path(self):

        x = self
        result = []

        while x:
            result.append(x)
            x = x.parent

        result.reverse()
        return result

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


class Queue:

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        raise NotImplementedError

    def extend(self, items):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, item):
        raise NotImplementedError


class FIFOQueue(Queue):

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


def graph_search(problem, fringe):

    closed = set()

    fringe.append(Node(problem.initial))

    while fringe:

        node = fringe.pop()

        if problem.goal_test(node.state):
            return node

        if node.state not in closed:

            closed.add(node.state)

            fringe.extend(node.expand(problem))

    return None


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())


class Balls(Problem):

    moves = {

        "Up Left": (-2, 2),
        "Up Right": (2, 2),
        "Down Left": (-2, -2),
        "Down Right": (2, -2),
        "Left": (-2, 0),
        "Right": (2, 0)
    }

    jumped = {

        "Up Left": (-1, 1),
        "Up Right": (1, 1),
        "Down Left": (-1, -1),
        "Down Right": (1, -1),
        "Left": (-1, 0),
        "Right": (1, 0)
    }

    def __init__(self, initial, N, obstacles):

        super().__init__(tuple(sorted(initial)))

        self.N = N
        self.obstacles = set(obstacles)
        self.goal_position = (N // 2, N - 1)

    def valid_move(self, x, y, move, balls):

        dx, dy = self.moves[move]
        jx, jy = self.jumped[move]

        nx = x + dx
        ny = y + dy

        mx = x + jx
        my = y + jy

        if not (0 <= nx < self.N and 0 <= ny < self.N):
            return False

        if (nx, ny) in self.obstacles:
            return False

        if (nx, ny) in balls:
            return False

        if (mx, my) not in balls:
            return False

        return True

    def successor(self, state):

        successors = {}

        balls = set(state)

        for (x, y) in balls:

            for move in self.moves:

                if self.valid_move(x, y, move, balls):

                    dx, dy = self.moves[move]
                    jx, jy = self.jumped[move]

                    nx = x + dx
                    ny = y + dy

                    mx = x + jx
                    my = y + jy

                    new_balls = set(balls)

                    new_balls.remove((x, y))

                    new_balls.remove((mx, my))

                    new_balls.add((nx, ny))

                    new_state = tuple(sorted(new_balls))

                    action = f"{move}: (x={x},y={y})"

                    successors[action] = new_state

        return successors

    def actions(self, state):
        return list(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):

        return (
            len(state) == 1 and
            state[0] == self.goal_position
        )


if __name__ == "__main__":

    N = int(input())

    num_balls = int(input())

    balls = []

    for _ in range(num_balls):

        x, y = map(int, input().split(','))

        balls.append((x, y))

    num_obstacles = int(input())

    obstacles = []

    for _ in range(num_obstacles):

        x, y = map(int, input().split(','))

        obstacles.append((x, y))

    problem = Balls(balls, N, obstacles)

    solution = breadth_first_graph_search(problem)

    if solution:
        print(solution.solution())
    else:
        print("No solution")