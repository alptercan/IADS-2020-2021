import math
import random


def euclid(p, q):
    x = p[0] - q[0]
    y = p[1] - q[1]
    return math.sqrt(x * x + y * y)


class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self, n, filename):

        with open(filename) as openFile:
            if n > 0:
                self.n = n
                self.dists = [[0]*self.n for i in range(self.n)]
                for line in openFile:
                    edge = [int(k) for k in line.split()]
                    j = edge[1]
                    i = edge[0]
                    self.dists[i][j] = edge[2]
                    self.dists[j][i] = edge[2]
                openFile.close()
            elif n == -1:
                self.n = 0
                self.dists = []
                for line0 in openFile:
                    edge0 = [int(k) for k in line0.split()]
                    with open(filename) as file:
                        distance = []
                        self.n += 1
                        for line1 in file:
                            edge1 = [int(k) for k in line1.split()]
                            euclidean = euclid(edge0, edge1)
                            distance.append(euclidean)
                            self.dists.append(distance)
            self.perm = list(range(self.n))

            # def makingNodes(node):
            # return [int(n) for n in node]

            # self.n = 0
            # self.dist = []
            # with open(filename) as openFile:

            #  if n < 0:
            #      for line_i in openFile:
            #         node_i = makingNodes(line_i.split())
            #        self.n += 1
            #       rows = []
            #      for line_j in openFile:
            #         node_j = makingNodes(line_j.split())
            #        rows.append(node_i, node_j)
            #       self.dists.append(rows)

            # else:

            #   self.n = n
            #  self.dists = [[0]*self.n for i in range(self.n)]
            # for line in openFile:
            #    edges = makingNodes(line.split())
            #   self.dists[edges[0]][edges[1]] = edges[2]
            #  self.dists[edges[1]][edges[0]] = edges[2]
            # self.perm = (i for i in range(self.n))

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).

    def tourValue(self):
        for i in range(self.n):
            return 0 + sum([self.dists[self.perm[i-1]]][self.perm[i]])

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.

    def trySwap(self, i):
        prevCost = self.tourValue()
        self.perm[i], self.perm[(i + 1) % self.n] = self.perm[(i + 1) % self.n], self.perm[i]
        currCost = self.tourValue()
        if currCost < prevCost:
            return True
        else:
            self.perm[i], self.perm[(i + 1) % self.n] = self.perm[(i + 1) % self.n], self.perm[i]
            return False

    # Consider the effect of reversing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.

    def tryReverse(self, i, j):
        prevCost = self.tourValue()
        self.perm[i:j + 1] = list(reversed(self.perm[i:j + 1]))
        currCost = self.tourValue()
        if prevCost > currCost:
            return True
        else:
            self.perm[i:j + 1] = list(reversed(self.perm[i:j + 1]))
            return False

    def swapHeuristic(self, k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self, k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n - 1):
                for i in range(j):
                    if self.tryReverse(i, j):
                        better = True

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.

    def Greedy(self):

        unused = set(range(1, self.n))
        self.perm[0] = 0

        for i in range(0, self.n - 1):
            minimum = math.inf
            next = 0
            for node in unused:
                distances = self.dists[self.perm[i], node]
                if distances < minimum:
                    minimum = distances
                    next = node
            self.perm[i + 1] = next
            unused.remove(next)






