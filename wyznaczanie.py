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
        edge =  int(n*(n-1)*(g/100) )
        if edge % 2 == 1:
            edge +=1
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


    def __str__(self):
        out = ""
        for i in range(len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def Euler(self, start):
        pass

    def Hamilton(self,start):
        pass
    
matrix = GraphM(10, 30)
print (matrix)


"""
outM = open("PRIM70M.txt", 'w')
outL = open("PRIM70L.txt", 'w')

for i in range(1, 16):
    matrix = GraphM(500 * i, 70)

    startTime = time.time()
    matrix.euler(0)
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