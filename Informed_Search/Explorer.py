from searching_framework import *
from searching_framework.utils import *

class Explorer(Problem):
    def __init__(self,initial,goal):
        super().__init__(initial,goal)
        self.max_x = 8
        self.max_y = 6

    def moveObstacles(self,x,y,d):
        if d == -1:
            if y == 0:
                d = 1
                y += 1
            else:
                y -= 1
        else:
            if y == self.max_y-1:
                d = -1
                y -= 1
            else:
                y += 1

        return x,y,d

    def successor(self, state):

        successors = dict()

        mx,my = state[0],state[1]
        (o1x, o1y, o1d) = state[2]
        (o2x, o2y, o2d) = state[3]

        new_o1 = self.moveObstacles(o1x,o1y,o1d)
        new_o2 = self.moveObstacles(o2x,o2y,o2d)

        obstacles = [(new_o1[0],new_o1[1]),(new_o2[0],new_o2[1])]
        directions = {"Up": (0,1), "Down": (0,-1), "Left": (-1,0), "Right": (1,0)}


        for action, (dx,dy) in directions.items():
            nx,ny = mx+dx, my+dy
            if 0 <= nx < self.max_x and 0 <= ny < self.max_y and (nx,ny) not in obstacles:
                successors[action] = (nx,ny,new_o1,new_o2)

        # # Move Right
        # nx = mx+1
        # if nx < self.max_x and (nx,my) not in obstacles:
        #     successors["Right"] = (nx,my,new_o1,new_o2)
        #
        # # Move Left
        # nx = mx-1
        # if nx >= 0 and (nx,my) not in obstacles:
        #     successors["Left"] = (nx,my,new_o1,new_o2)
        #
        # # Move Up
        # ny = my+1
        # if ny < self.max_y and (mx,ny) not in obstacles:
        #     successors["Up"] = (mx,ny,new_o1,new_o2)
        #
        # # Move Down
        # ny = my-1
        # if ny >= 0 and (mx,ny) not in obstacles:
        #     successors["Down"] = (mx,ny,new_o1,new_o2)


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        mx, my = state[0],state[1]
        return (mx,my) == self.goal

    def h(self,node):
        mx = node.state[0]
        my = node.state[1]
        hx = self.goal[0]
        hy = self.goal[1]
        return abs(mx-hx) + abs(my-hy)


if __name__ == '__main__':

    initial = (0,2)
    goal = (7,4)
    obstacle1 = (2,5,-1)
    obstacle2 = (5,0,1)

    explorer = Explorer((initial[0],initial[1],obstacle1,obstacle2),goal)

    result = astar_search(explorer)
    print(result.solution())
















