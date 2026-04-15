from searching_framework import *
from searching_framework.utils import *


class Molecule(Problem):
    def __init__(self,obstacles,initial,goal=None):
        super().__init__(initial,goal)
        self.max_x = 9
        self.max_y = 7
        self.obstacles = obstacles


    def moveRight(self,x1,y1,x2,y2,x3,y3):
        while x1 < self.max_x-1 and (x1+1,y1) not in self.obstacles and (x1+1,y1) != (x2,y2) and (x1+1,y1) != (x3,y3):
            x1 += 1
        return x1

    def moveLeft(self,x1,y1,x2,y2,x3,y3):
        while x1 > 0 and (x1-1,y1) not in self.obstacles and (x1-1,y1) != (x2,y2) and (x1-1,y1) != (x3,y3):
            x1-=1
        return x1

    def moveUp(self,x1,y1,x2,y2,x3,y3):
        while y1 < self.max_y-1 and (x1,y1+1) not in self.obstacles and (x1,y1+1) != (x2,y2) and (x1,y1+1) != (x3,y3):
            y1+=1
        return y1

    def moveDown(self,x1,y1,x2,y2,x3,y3):
        while y1 > 0 and (x1,y1-1) not in self.obstacles and (x1,y1-1) != (x2,y2) and (x1,y1-1) != (x3,y3):
            y1-=1
        return y1






    def successor(self, state):

        successors = dict()

        H1_x, H1_y ,Ox,Oy, H2_x,H2_y = state

        #H1
        newX = self.moveRight(H1_x,H1_y,Ox,Oy,H2_x,H2_y)
        if newX != H1_x:
            successors["RightH1"] = (newX,H1_y,Ox,Oy,H2_x,H2_y)

        newX = self.moveLeft(H1_x, H1_y ,Ox,Oy, H2_x,H2_y)
        if newX != H1_x:
            successors["LeftH1"] = (newX,H1_y,Ox,Oy,H2_x,H2_y)

        newY = self.moveUp(H1_x, H1_y ,Ox,Oy, H2_x,H2_y)
        if newY != H1_y:
            successors["UpH1"] = (H1_x,newY,Ox,Oy,H2_x,H2_y)

        newY = self.moveDown(H1_x, H1_y ,Ox,Oy, H2_x,H2_y)
        if newY != H1_y:
            successors["DownH1"] = (H1_x,newY,Ox,Oy,H2_x,H2_y)

        #O
        newX = self.moveRight(Ox, Oy, H1_x, H1_y,H2_x, H2_y)
        if newX != Ox:
            successors["RightO"] = (H1_x, H1_y, newX, Oy, H2_x, H2_y)

        newX = self.moveLeft(Ox, Oy, H1_x, H1_y,H2_x, H2_y)
        if newX != Ox:
            successors["LeftO"] = (H1_x, H1_y, newX, Oy, H2_x, H2_y)

        newY = self.moveUp(Ox, Oy, H1_x, H1_y,H2_x, H2_y)
        if newY != Oy:
            successors["UpO"] = (H1_x, H1_y, Ox, newY, H2_x, H2_y)

        newY = self.moveDown(Ox, Oy, H1_x, H1_y,H2_x, H2_y)
        if newY != Oy:
            successors["DownO"] = (H1_x, H1_y, Ox, newY, H2_x, H2_y)

         # H2
        newX = self.moveRight(H2_x, H2_y,H1_x, H1_y, Ox, Oy)
        if newX != H2_x:
            successors["RightH2"] = (H1_x, H1_y, Ox, Oy, newX, H2_y)

        newX = self.moveLeft(H2_x, H2_y,H1_x, H1_y, Ox, Oy)
        if newX != H2_x:
            successors["LeftH2"] = (H1_x, H1_y, Ox, Oy, newX, H2_y)

        newY = self.moveUp(H2_x, H2_y,H1_x, H1_y, Ox, Oy)
        if newY != H2_y:
            successors["UpH2"] = (H1_x, H1_y, Ox, Oy, H2_x, newY)

        newY = self.moveDown(H2_x, H2_y,H1_x, H1_y, Ox, Oy)
        if newY != H2_y:
            successors["DownH2"] = (H1_x, H1_y, Ox, Oy, H2_x, newY)


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return (state[1] == state[3] == state[5]) and (state[2] == state[0]+1 == state[4]-1)


if __name__ == '__main__':

    obstacles = {(3,6),(5,6),(7,6),
                 (2,5),(8,5),
                 (1,3),(6,3),(7,3),
                 (4,2),(6,2),
                 (0,1),(1,1),(3,1),(6,1)}


    h1 = (2,1)
    h2 = (2,6)
    o = (7,2)
    start = (h1[0],h1[1],o[0],o[1],h2[0],h2[1])
    molecule = Molecule(obstacles,start)
    result = breadth_first_graph_search(molecule)

    print(result.solution())
    print()
    print(result.solve())