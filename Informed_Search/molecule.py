from searching_framework import *
from searching_framework.utils import *

class Molecule(Problem):
    def __init__(self,initial,obstacles,goal=None):
        super().__init__(initial,goal)
        self.obstacles = obstacles
        self.max_x = 9
        self.max_y = 7

    def moveUp(self,x,y,a2x,a2y,a3x,a3y):
        while y < self.max_y-1 and (x,y+1) != (a2x,a2y) and (x,y+1) != (a3x,a3y) and (x,y+1) not in self.obstacles:
            y += 1
        return x,y

    def moveDown(self,x,y,a2x,a2y,a3x,a3y):
        while y > 0 and (x,y-1) != (a2x,a2y) and (x,y-1) != (a3x,a3y) and (x,y-1) not in self.obstacles:
            y-=1
        return x,y

    def moveLeft(self,x,y,a2x,a2y,a3x,a3y):
        while x > 0 and (x-1,y) != (a2x,a2y) and (x-1,y) != (a3x,a3y) and (x-1,y) not in self.obstacles:
            x-=1
        return x,y

    def moveRight(self,x,y,a2x,a2y,a3x,a3y):
        while x < self.max_x-1 and (x+1,y) != (a2x,a2y) and (x+1,y) != (a3x,a3y) and (x+1,y) not in self.obstacles:
            x+=1
        return x,y

    def successor(self, state):

        successors = dict()

        h1x, h1y = state[0], state[1]
        ox,oy = state[2], state[3]
        h2x, h2y = state[4], state[5]

        # H1
        newx,newy = self.moveUp(h1x,h1y,ox,oy,h2x,h2y) # move up
        if (newx,newy) != (h1x,h1y):
            successors["UpH1"] = (newx,newy,ox,oy,h2x,h2y)

        newx, newy = self.moveDown(h1x, h1y, ox, oy, h2x, h2y)  # move down
        if (newx, newy) != (h1x, h1y):
            successors["DownH1"] = (newx, newy, ox, oy, h2x, h2y)

        newx, newy = self.moveLeft(h1x, h1y, ox, oy, h2x, h2y)  # move left
        if (newx, newy) != (h1x, h1y):
            successors["LeftH1"] = (newx, newy, ox, oy, h2x, h2y)

        newx, newy = self.moveRight(h1x, h1y, ox, oy, h2x, h2y)  # move right
        if (newx, newy) != (h1x, h1y):
            successors["RightH1"] = (newx, newy, ox, oy, h2x, h2y)


        # O
        newx, newy = self.moveUp(ox,oy,h1x,h1y,h2x,h2y) # move up
        if (newx,newy) != (ox,oy):
            successors["UpO"] = (h1x,h1y,newx,newy,h2x,h2y)

        newx, newy = self.moveDown(ox, oy, h1x, h1y, h2x, h2y)  # move down
        if (newx, newy) != (ox, oy):
            successors["DownO"] = (h1x, h1y, newx, newy, h2x, h2y)

        newx, newy = self.moveLeft(ox, oy, h1x, h1y, h2x, h2y)  # move left
        if (newx, newy) != (ox, oy):
            successors["LeftO"] = (h1x, h1y, newx, newy, h2x, h2y)

        newx, newy = self.moveRight(ox, oy, h1x, h1y, h2x, h2y)  # move right
        if (newx, newy) != (ox, oy):
            successors["RightO"] = (h1x, h1y, newx, newy, h2x, h2y)


        # H2
        newx,newy = self.moveUp(h2x,h2y,ox,oy,h1x,h1y) # move down
        if (newx,newy) != (h2x,h2y):
            successors["UpH2"] = (h1x,h1y,ox,oy,newx,newy)

        newx, newy = self.moveDown(h2x, h2y, ox, oy, h1x, h1y)  # move down
        if (newx, newy) != (h2x, h2y):
            successors["DownH2"] = (h1x, h1y, ox, oy, newx, newy)

        newx, newy = self.moveLeft(h2x, h2y, ox, oy, h1x, h1y)  # move left
        if (newx, newy) != (h2x, h2y):
            successors["LeftH2"] = (h1x, h1y, ox, oy, newx, newy)

        newx, newy = self.moveRight(h2x, h2y, ox, oy, h1x, h1y)  # move right
        if (newx, newy) != (h2x, h2y):
            successors["RightH2"] = (h1x, h1y, ox, oy, newx, newy)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        h1x,h1y = state[0],state[1]
        ox,oy = state[2],state[3]
        h2x,h2y = state[4],state[5]

        return (h1x+1,h1y) == (ox,oy) == (h2x-1,h2y)

    def h(self,node):
        h1x,h1y,ox,oy,h2x,h2y = node.state

        target_h1 = (ox-1,oy)
        target_h2 = (ox+1,oy)

        d1 = abs(h1x - target_h1[0]) + abs(h1y - target_h1[1])
        d2 = abs(h2x - target_h2[0]) + abs(h2y - target_h2[1])

        return d1 + d2




if __name__ == '__main__':

    obstacles = ([0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5])


    h1_pos = (2,1)
    h2_pos = (2,6)
    o_pos = (7,2)

    initial = (h1_pos[0],h1_pos[1],o_pos[0],o_pos[1],h2_pos[0],h2_pos[1])

    molecule = Molecule(initial,obstacles)

    result = astar_search(molecule)

    print(result.solution())