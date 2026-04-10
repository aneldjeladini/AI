from searching_framework import *
from searching_framework.utils import *


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 8]

    def moveKnight(self, kx, ky, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, type):
        if type == 1:
            newPos = (kx - 1, ky + 2)
            if newPos != (bx, by) and kx - 1 >= 0 and ky + 2 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 2:
            newPos = (kx + 1, ky + 2)
            if newPos != (bx, by) and kx + 1 <= 7 and ky + 2 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 3:
            newPos = (kx + 2, ky + 1)
            if newPos != (bx, by) and kx + 2 <= 7 and ky + 1 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 4:
            newPos = (kx + 2, ky - 1)
            if newPos != (bx, by) and kx + 2 <= 7 and ky - 1 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 5:
            newPos = (kx + 1, ky - 2)
            if newPos != (bx, by) and kx + 1 <= 7 and ky - 2 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 6:
            newPos = (kx - 1, ky - 2)
            if newPos != (bx, by) and kx - 1 >= 0 and ky - 2 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 7:
            newPos = (kx - 2, ky - 1)
            if newPos != (bx, by) and kx - 2 >= 0 and ky - 1 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

        if type == 8:
            newPos = (kx - 2, ky + 1)
            if newPos != (bx, by) and kx - 2 >= 0 and ky + 1 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (kx, ky, s1_e, s2_e, s3_e)

    def moveBishop(self, bx, by, hx, hy, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, type):
        if type == 1:
            newPos = (bx - 1, by + 1)
            if newPos != (hx, hy) and bx - 1 >= 0 and by + 1 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (bx, by, s1_e, s2_e, s3_e)

        if type == 2:
            newPos = (bx + 1, by + 1)
            if newPos != (hx, hy) and bx + 1 <= 7 and by + 1 <= 7:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (bx, by, s1_e, s2_e, s3_e)

        if type == 3:
            newPos = (bx - 1, by - 1)
            if newPos != (hx, hy) and bx - 1 >= 0 and by - 1 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (bx, by, s1_e, s2_e, s3_e)

        if type == 4:
            newPos = (bx + 1, by - 1)
            if newPos != (hx, hy) and bx + 1 <= 7 and by - 1 >= 0:
                if newPos == (s1_x, s1_y):
                    s1_e = -1
                if newPos == (s2_x, s2_y):
                    s2_e = -1
                if newPos == (s3_x, s3_y):
                    s3_e = -1
                return (newPos[0], newPos[1], s1_e, s2_e, s3_e)
            return (bx, by, s1_e, s2_e, s3_e)

    def successor(self, state):
        successors = dict()

        hx,  hy  = state[0],  state[1]
        bx,  by  = state[2],  state[3]
        s1_x, s1_y, s1_e = state[4],  state[5],  state[6]
        s2_x, s2_y, s2_e = state[7],  state[8],  state[9]
        s3_x, s3_y, s3_e = state[10], state[11], state[12]

        # Knight move 1
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 1)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K1"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 2
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 2)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K2"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 3
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 3)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K3"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 4
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 4)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K4"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 5
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 5)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K5"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 6
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 6)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K6"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 7
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 7)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K7"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Knight move 8
        newPos = self.moveKnight(hx, hy, bx, by, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 8)
        if (newPos[0], newPos[1]) != (hx, hy):
            successors["K8"] = (newPos[0], newPos[1], bx, by, s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Bishop move 1
        newPos = self.moveBishop(bx, by, hx, hy, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 1)
        if (newPos[0], newPos[1]) != (bx, by):
            successors["B1"] = (hx, hy, newPos[0], newPos[1], s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Bishop move 2
        newPos = self.moveBishop(bx, by, hx, hy, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 2)
        if (newPos[0], newPos[1]) != (bx, by):
            successors["B2"] = (hx, hy, newPos[0], newPos[1], s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Bishop move 3
        newPos = self.moveBishop(bx, by, hx, hy, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 3)
        if (newPos[0], newPos[1]) != (bx, by):
            successors["B3"] = (hx, hy, newPos[0], newPos[1], s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        # Bishop move 4
        newPos = self.moveBishop(bx, by, hx, hy, s1_x, s1_y, s1_e, s2_x, s2_y, s2_e, s3_x, s3_y, s3_e, 4)
        if (newPos[0], newPos[1]) != (bx, by):
            successors["B4"] = (hx, hy, newPos[0], newPos[1], s1_x, s1_y, newPos[2], s2_x, s2_y, newPos[3], s3_x, s3_y, newPos[4])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[6] == state[9] == state[12] == -1


if __name__ == '__main__':

    knight = (2, 5)
    bishop = (5, 1)
    stars_pos = ((1, 1), (4, 3), (6, 6))

    initial = (knight[0], knight[1],
               bishop[0], bishop[1],
               stars_pos[0][0], stars_pos[0][1], 0,
               stars_pos[1][0], stars_pos[1][1], 0,
               stars_pos[2][0], stars_pos[2][1], 0)

    stars = Stars(initial)
    result = breadth_first_graph_search(stars)
    print(result.solution())