class KMP:
    """docstring for KMP"""
    def getNext(self, s):
        n = len(s)
        a, pos, cnd = n * [0], 0, -1
        a[0] = -1
        while pos < n - 1:
            if cnd == -1 or s[pos] == s[cnd]:
                cnd, pos = cnd + 1, pos + 1
                if s[pos] != s[cnd]:
                    a[pos] = cnd
                else:
                    a[pos] = a[cnd]
            else:
                cnd = a[cnd]
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