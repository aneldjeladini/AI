from searching_framework import *


class Boxes(Problem):
    def __init__(self, initial,n,num_boxes, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.num_boxes = num_boxes

    moves = {"Gore": (0,1), "Desno": (1,0)}

    def valid(self,x,y,boxes):
        return 0 <= x < self.n and 0 <= y < self.n and (x,y) not in boxes

    def isAdjacent(self,x,y,bx,by):
        return abs(x - bx) < 2 and abs(y - by) < 2 and (x,y) != (bx,by)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == self.num_boxes

    def successor(self, state):

        succ = {}

        man_pos, boxes, boxes_filled = state

        for move, (x,y) in self.moves.items():
            boxes_filled_list = list(boxes_filled)
            nx = man_pos[0] + x
            ny = man_pos[1] + y

            if not self.valid(nx,ny,boxes):
                continue

            for box in boxes:
                if self.isAdjacent(nx,ny,box[0],box[1]):
                    if box not in boxes_filled_list:
                        boxes_filled_list.append(box)

            succ[move] = (nx,ny),boxes,tuple(boxes_filled_list)


        return succ


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))


    initial = man_pos,tuple(boxes),()

    problem = Boxes(initial,n,num_boxes)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
