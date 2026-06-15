from logging import fatal

from searching_framework import *


class Laser(Problem):
    def __init__(self, initial,max_y,max_x,obstacles, goal=None):
        super().__init__(initial, goal)
        self.max_x = max_x
        self.max_y = max_y
        self.obstacles = obstacles

    dirs = {"Gore": (0, +1), "Dolu": (0, -1), "Levo": (-1, 0), "Desno": (+1, 0),"Stoj":(0,0)}

    def valid(self,mx,my,lx,ly,timer):
        if mx < 0 or mx >= self.max_x or my < 0 or my >= self.max_y or (mx,my) in self.obstacles:
            return False

        if timer == 4 and ((mx == lx) or (my == ly)):
            return False

        return True



    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_pos = state[0]
        return man_pos == self.goal


    def successor(self, state):

        succ = {}

        man_pos,laser_pos,timer = state

        for dir,(x,y) in self.dirs.items():
            nx = man_pos[0] + x
            ny = man_pos[1] + y
            lx = laser_pos[0]
            ly = laser_pos[1]
            new_timer = -1

            if timer < 4: new_timer = timer + 1
            else: new_timer = 1

            if new_timer == 1:
                lx = nx
                ly = ny

            if not self.valid(nx,ny,lx,ly,new_timer):
                continue

            succ[dir] = (nx,ny), (lx,ly) , new_timer

        return succ


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    blocked = [read_two() for _ in range(int(input()))]

    initial = man_pos,laser_pos,timer
    problem = Laser(initial,N,M,tuple(blocked),target_pos)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
