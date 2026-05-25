from searching_framework import Problem, astar_search

class RobotProblem(Problem):
    def __init__(self, initial, goal, walls, chargers, B):
        super().__init__(initial, goal)
        self.walls = set(walls)
        self.chargers = set(chargers)
        self.B = B

    def actions(self, state):
        x, y, battery = state
        if battery == 0:
            return []
        dirs = {"Up": (0, 1), "Down": (0, -1), "Left": (-1, 0), "Right": (1, 0)}
        valid = []
        for action, (dx, dy) in dirs.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 9 and 0 <= ny <= 9 and (nx, ny) not in self.walls:
                valid.append(action)
        return valid

    def result(self, state, action):
        x, y, battery = state
        dirs = {"Up": (0, 1), "Down": (0, -1), "Left": (-1, 0), "Right": (1, 0)}
        dx, dy = dirs[action]
        nx, ny = x + dx, y + dy
        new_battery = self.B if (nx, ny) in self.chargers else battery - 1
        return (nx, ny, new_battery)

    def goal_test(self, state):
        x, y, battery = state
        gx, gy = self.goal
        return x == gx and y == gy

    def h(self, node):
        x, y, battery = node.state
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)


if __name__ == '__main__':
    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9)]

    line1 = input().split(',')
    x, y = int(line1[0]), int(line1[1])

    line2 = input().split(',')
    gx, gy = int(line2[0]), int(line2[1])

    B = int(input())

    n = int(input())
    chargers = []
    for _ in range(n):
        parts = input().split(',')
        chargers.append((int(parts[0]), int(parts[1])))

    initial = (x, y, B)
    goal = (gx, gy)

    problem = RobotProblem(initial, goal, walls, chargers, B)
    solution = astar_search(problem)

    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")