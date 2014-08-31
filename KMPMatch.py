class KMP:
    """docstring for KMP"""
    def getNext(self, s):
        n = len(s)
        a, i, j = n * [0], 0, -1
        a[0] = -1
        while i < n - 1:
            if j == -1 or s[i] == s[j]:
                i, j = i + 1, j + 1
                if s[i] != s[j]:
                    a[i] = j
                else:
                    a[i] = a[j]
            else:
                j = a[j]
        return a
    def match(self, s, p):
        a, i, j = self.getNext(p), 0, 0
        print(a)
        while i < len(s):
            if j == -1 or s[i] == p[j]:
                i, j = i + 1, j + 1
            else:
                j = a[j]
            if j == len(p):
                return i - len(p)
        return -1
