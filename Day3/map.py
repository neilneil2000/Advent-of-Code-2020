from io import IncrementalNewlineDecoder


class Map:

    def __init__(self,filename):
        self.landscape = []
        self.read_input_file(filename)
        self.length = len(self.landscape)
        self.width = len(self.landscape[0])
        self.trees_hit = 0
    

    def reset_skiier(self):
        for i,row in enumerate(self.landscape):
            for j,w in enumerate(row):
                if w == 'X':
                    self.landscape[i][j] = '#'
                if w == 'O':
                    self.landscape[i][j] = '.'
        self.trees_hit = 0


    def count_trees(self):
        for row in self.landscape:
            for location in row:
                if location == 'X':
                    self.trees_hit += 1

    def mark_descent(self,direction):
        right,down = direction
        point = direction
        while point[1] < self.length:
            point = self.mark_point(point)
            point = (point[0] + right, point[1] + down)


    def mark_point(self,point):
        x,y = point
        if x >= self.width:
            x -= self.width
        if self.landscape[y][x] == '.':
            self.landscape[y][x] = 'O'
        else:
            self.landscape[y][x] = 'X'
        return (x,y)


    def read_input_file(self,filename):
        with open(filename,'r') as f:
            for line in f:
                self.landscape.append(list(line.strip()))