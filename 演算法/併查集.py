
class DSU:
    def _init_(self, n):
        self.root = [i for i in range(n)]
        self.depth = [1 for i in range(n)]

    def find(self, k):
        if self.root == k:
            return k
        else:
            return self.find(self.root[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        xh = self.depth[x]
        yh = self.depth[y]
        if x == y:
            return
        if xh > yh:
            self.root[y] = x
            self.depth[x] = max(self.depth[x], self.depth[y] + 1)
        else:
            self.root[x] = y


class DSU:
    def _init_(self, n):
        self.root = [i for i in range(n)]

    def find(self, k):
        if self.root[k] == k:
            return k
        else:
            self.root[k] = self.find(self.root[k])
            return self.root[k]


def union(self, a, b):
    x = self.find(a)
    y = self.find(b)
    if x == y:
        return
    self.root[x] = y
