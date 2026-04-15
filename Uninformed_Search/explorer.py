from searching_framework import *
from searching_framework.utils import *

class Explorer(Problem):
    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)
        self.max_x = 7
        self.max_y = 5

    def moveObstacle(self,obx,oby,dir):
        '''dir = 0 -> UP
            dir = 1 -> DOWN'''
        if dir == 0:
            if oby == self.max_y:
                dir = 1
                oby -= 1
            else:
                oby += 1

        else:
            if oby == 0:
                dir = 0
                oby += 1
            else: oby -= 1

        return obx,oby,dir


    def successor(self, state):

        successors = dict()

        man_x, man_y, ob1_x, ob1_y, ob1_dir, ob2_x, ob2_y, ob2_dir = state

        ob1_x,ob1_y,ob1_dir = self.moveObstacle(ob1_x,ob1_y,ob1_dir)

        obstacles = [(ob1_x,ob1_y),(ob2_x,ob2_y)]

        moves = [
            ("Right" , man_x+1, man_y),
            ("Left" , man_x-1, man_y),
            ("Up" , man_x, man_y+1),
            ("Down" , man_x, man_y-1)
        ]

        for action, nx, ny in moves:
            in_bounds = (nx >= 0 and nx <= self.max_x) and (ny >= 0 and ny <= self.max_y)
            no_collision = (nx,ny) not in obstacles

            if in_bounds and no_collision:
                new_state = (nx,ny,
                             ob1_x,ob1_y,ob1_dir,
                             ob2_x,ob2_y,ob2_dir)
                successors[action] = new_state



        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0],state[1])
        return position == self.goal


if __name__ == '__main__':

    initial = (0,2)
    goal = (7,4)
    ob1 = (2,5,1)
    ob2 = (5,0,0)

    start = (initial[0],initial[1],
             ob1[0],ob1[1],ob1[2],
             ob2[0],ob2[1],ob2[2])

    explorer = Explorer(start,goal)

    result = breadth_first_graph_search(explorer)

    print(result.solve())
    print()
    print(result.solution())


