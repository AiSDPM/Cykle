import random
import time


class Edge:
    def __init__(self, x=-1, y=-1, val=9999):
        self.val = val
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        out = "[(" + str(self.x) + "," + str(self.y) + ");" + str(self.val) + "]"
        return out


class GraphM:

    def __init__(self, n, g):
        self.matrix = []
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
        for i in range(n-1):
            self.matrix[i][i+1] = 1
            self.matrix[i+1][i] = 1
        self.matrix[0][n-1] = 1
        self.matrix[n-1][0] = 1
        MAXedge = round(n * (n - 1) * (g / 100) / 2)
        edge = n
        while edge < MAXedge:
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            z = random.randint(0,n-1)
            if z==x or x==y or z==y or  self.matrix[x][y] == 1 or self.matrix[x][z] == 1 or self.matrix[y][z] == 1:
                continue
            else:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                self.matrix[x][z] = 1
                self.matrix[z][x] = 1
                self.matrix[z][y] = 1
                self.matrix[y][z] = 1
                edge +=3

    def __str__(self):
        out = ""
        for i in range(len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

class GraphL:
    def __init__(self, matrix):
        self.list = []
        l = len(matrix.matrix)
        for i in range(l):
            self.list.append([])
            for j in range(l):
                val = matrix.matrix[i][j]
                if val != 0:
                    self.list[i].append(j)

    def __str__(self):
        l = len(self.list)
        out = ""
        for i in range(l):
            pom = str(i) + ":  "
            li = len(self.list[i])
            for j in range(li):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out
    
    def _Euler(self, out , v):
        for i in self.list[v]:
            self.list[v].remove(i) #tu moze sie wysypac
            out = self._Euler(i)
        out.append(v)
        return out

    def Euler(self, v):
        out = []
        stack = []
        return self._Euler(out, stack, v)


    def Hamilton(self,v):
        pass

matrix = GraphM(10, 30)
print (matrix)
Lmatrix = GraphL(matrix)
print(Lmatrix)

"""
outM = open("Euler30.txt", 'w')
outL = open("Hamilton30.txt", 'w')
for i in range(1, 16):
    matrix = GraphM(500 * i, 70)
    list = GraphL(matrix)
    startTime = time.time()
    list.euler(0)
    endTime = time.time()
    Time = endTime - startTime
    outM.write("Euler" + str(Time) + "\n")
    startTime = time.time()
    list.hamilton(0)
    endTime = time.time()
    Time = endTime - startTime
    outL.write("Hamilton" + str(Time) + "\n")
    print(str(i))
    del list
outM.close()
outL.close() """
