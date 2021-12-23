import random 
class Nonogram():
    def __init__(self, scale, hardship= 0.3):
        self.scale = scale
        self.hardship = hardship
        # point -> (Column_Number, Row_Number)
        self.allpoints = dict() # All Points With It's Values -> { Point: Value,...}
        self.allpointslist = [] # List Of All Points -> [ point1, point2, point3,....]
        self.Nonepoints = [] # List Of All Points Which It's Values Is 'None'
        self.truePoints = [] # List Of All Points Which It's Values Is 'True'
        self.helpcolumns, self.helprows = dict(), dict() # All Column & Row Guides -> {Column Or Row: Guide List}
        # Generate All Points With Initial Value Of 'True'
        for i in range(1, scale+1):
            for j in range(1, scale+1):
                self.allpoints[(i,j)] = True
        self.allpointslist = [x for x in self.allpoints.keys()]
        # Generate Random Points With Value 'None' Based on 'self.hardship'
        while len(self.Nonepoints) != int((scale**2)*self.hardship):
            x = random.choice(self.allpointslist)
            if (x not in self.Nonepoints): 
                self.allpoints[x] = None
                self.Nonepoints.append(x)
        # Generate True Points List  
        self.truePoints = list(filter(lambda x: x not in self.Nonepoints, self.allpointslist))
        # Generate Column & Row Guides
        self.columnGuidesGenerator()
        self.rowGuidesGenerator()

    def columnGuidesGenerator(self):
        for i in range(1, int((self.scale+1))):
            scope, n = [], 0
            for point in self.allpointslist:
                if point[0] == i and self.allpoints[point] != None: n+=1
                if (point[0] == i and self.allpoints[point] == None and n != 0) or (point[1] == self.scale and self.allpoints[point] != None and n != 0):
                    scope.append(str(n)) 
                    n = 0
            self.helpcolumns[f'C{i}'] = scope
            
    def rowGuidesGenerator(self):
        for i in range(1, int((self.scale+1))):
            scope, n = [], 0
            for point in self.allpointslist:
                if point[1] == i and self.allpoints[point] != None: n+=1
                if (point[1] == i and self.allpoints[point] == None and n != 0) or (point[0] == self.scale and point[1] == i and self.allpoints[point] != None and n != 0):
                    scope.append(str(n))
                    n = 0
            self.helprows[f'R{i}'] = scope
            