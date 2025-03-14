class Counter:
    def __init__(self, value = 0):
        self.value = value
        self.initvalue = value

    def inc(self):
        self.value = self.value + 1

    def dec(self):
        self.value = self.value - 1

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.initvalue


c1 = Counter()
c1.inc()
c1.reset()
print(c1.getvalue())

c2 = Counter(100)
c2.dec()
print(c2.getvalue())


