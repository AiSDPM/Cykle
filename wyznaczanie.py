import random
import time
import sys


class GraphM:

    def __init__(self, n, g):
        self.matrix = []
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
        for i in range(n - 1):
            self.matrix[i][i + 1] = 1
            self.matrix[i + 1][i] = 1
        self.matrix[0][n - 1] = 1
        self.matrix[n - 1][0] = 1
        MAXedge = round(n * (n - 1) * (g / 100) / 2)
        edge = n
        while edge < MAXedge:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            z = random.randint(0, n - 1)
            if z == x or x == y or z == y or self.matrix[x][y] == 1 or self.matrix[x][z] == 1 or self.matrix[y][z] == 1:
                continue
            else:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                self.matrix[x][z] = 1
                self.matrix[z][x] = 1
                self.matrix[z][y] = 1
                self.matrix[y][z] = 1
                edge += 3
        for i in range(n):
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if x != y:
                self.matrix[x], self.matrix[y] = self.matrix[y], self.matrix[x]
                for i in range(n):
                    self.matrix[i][x], self.matrix[i][y] = self.matrix[i][y], self.matrix[i][x]

    def __str__(self):
        out = ""
        for i in range(len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def Euler(self, sv):
        out = []
        stack = [sv]
        while stack:
            v = stack[-1]
            is_edge = 0
            for i in range(len(self.matrix)):
                if self.matrix[v][i] == 1:
                    self.matrix[v][i] = -1
                    self.matrix[i][v] = -1
                    stack.append(i)
                    is_edge = 1
                    break
            if is_edge == 1:
                continue
            stack.pop()
            out.append(v)
        return out

    def _Hamilton(self, out, start, v):
        for i in range(len(self.matrix)):
            if len(out) == len(self.matrix) + 1:
                break
            elif self.matrix[v][i] == -1 and not (i in out):
                out.append(i)
                out = self._Hamilton(out, start, i)
        if len(out) >= len(self.matrix):
            if len(out) == len(self.matrix) and self.matrix[v][start] == -1:
                out.append(start)
        else:
            out.pop()
        return out

    def Hamilton(self, v):
        out = [v]
        start = v
        return self._Hamilton(out, start, v)

sys.setrecursionlimit(4500)


outE = open("Euler30.txt", 'w')
outH = open("Hamilton30.txt", 'w')
for i in range(1, 16):
    matrix = GraphM(10 * i, 30)
    startTime = time.time()
    matrix.Euler(0)
    endTime = time.time()
    Time = endTime - startTime
    outE.write("Euler" + str(Time) + "\n")
    startTime = time.time()
    matrix.Hamilton(0)
    endTime = time.time()
    Time = endTime - startTime
    outH.write("Hamilton" + str(Time) + "\n")
    print(str(i))
outM.close()
outL.close()
