from searching_framework import *

class Robot(Problem):
    def __init__(self, initial, walls, M1_pos, M2_pos, M1_req_steps, M2_req_steps, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.grid_size = 10
        self.M1_pos = M1_pos
        self.M2_pos = M2_pos
        self.M1_req_steps = M1_req_steps
        self.M2_req_steps = M2_req_steps

        self.dirs = {
            "Up": (0, 1),
            "Down": (0, -1),
            "Left": (-1, 0),
            "Right": (1, 0),
            "Repair": (0, 0)
        }

    def valid(self, x, y):
        return self.grid_size > x >= 0 and self.grid_size > y >= 0 and (x, y) not in self.walls

    def successor(self, state):
        succ = {}

        robot_pos, parts_M1, parts_M2, M1_steps, M2_steps, repaired_M1, repaired_M2, collected_all_parts_M1, collected_all_parts_M2 = state
        robot_x = robot_pos[0]
        robot_y = robot_pos[1]

        for dir in self.dirs:
            nx = robot_x + self.dirs[dir][0]
            ny = robot_y + self.dirs[dir][1]

            if not self.valid(nx, ny):
                continue

            new_M1_steps = M1_steps
            new_M2_steps = M2_steps
            new_repaired_M1 = repaired_M1
            new_repaired_M2 = repaired_M2
            new_collected_all_parts_M1 = collected_all_parts_M1
            new_collected_all_parts_M2 = collected_all_parts_M2

            new_parts_M1 = list(parts_M1)
            new_parts_M2 = list(parts_M2)

            if len(parts_M1) == 0:
                new_collected_all_parts_M1 = True

            if len(parts_M2) == 0:
                new_collected_all_parts_M2 = True

            if dir == "Repair":
                on_M1 = (nx, ny) == self.M1_pos
                on_M2 = (nx, ny) == self.M2_pos

                if not (on_M1 and new_collected_all_parts_M1 and not new_repaired_M1) and \
                        not (on_M2 and new_collected_all_parts_M2 and new_repaired_M1 and not new_repaired_M2):
                    continue

                if on_M1 and new_collected_all_parts_M1 and not new_repaired_M1:
                    if new_M1_steps < self.M1_req_steps:
                        new_M1_steps += 1
                    if new_M1_steps == self.M1_req_steps:
                        new_repaired_M1 = True

                if on_M2 and new_collected_all_parts_M2 and new_repaired_M1 and not new_repaired_M2:
                    if new_M2_steps < self.M2_req_steps:
                        new_M2_steps += 1
                    if new_M2_steps == self.M2_req_steps:
                        new_repaired_M2 = True

            else:
                new_M1_steps = 0
                new_M2_steps = 0

                if (nx, ny) in new_parts_M1:
                    new_parts_M1.remove((nx, ny))
                    if len(new_parts_M1) == 0:
                        new_collected_all_parts_M1 = True

                if (nx, ny) in new_parts_M2 and new_repaired_M1:
                    new_parts_M2.remove((nx, ny))
                    if len(new_parts_M2) == 0:
                        new_collected_all_parts_M2 = True

            succ[dir] = (
                (nx, ny),
                tuple(new_parts_M1),
                tuple(new_parts_M2),
                new_M1_steps,
                new_M2_steps,
                new_repaired_M1,
                new_repaired_M2,
                new_collected_all_parts_M1,
                new_collected_all_parts_M2
            )

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[5] and state[6]


if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())

    parts_M1 = int(input())
    to_collect_M1 = tuple(tuple(map(int, input().split(','))) for _ in range(parts_M1))

    parts_M2 = int(input())
    to_collect_M2 = tuple(tuple(map(int, input().split(','))) for _ in range(parts_M2))

    walls = [
        (4, 0), (5, 0), (7, 5), (8, 5), (9, 5),
        (1, 6), (1, 7), (0, 6), (0, 8), (0, 9),
        (1, 9), (2, 9), (3, 9)
    ]

    initial = (
        robot_start_pos,
        to_collect_M1,
        to_collect_M2,
        0,
        0,
        False,
        False,
        False,
        False
    )

    problem = Robot(initial, tuple(walls), M1_pos, M2_pos, M1_steps, M2_steps)
    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")