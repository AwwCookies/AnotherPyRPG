from anotherpyrpg import PyRPGObject, settings

class Pool(PyRPGObject):
    def __init__(self, _min=0, _max=100, current=None, settings={}):
        PyRPGObject.__init__(self)
        self.min = _min
        self.max = _max
        # If `current` wasn't set, set it to max
        self.current = current if current != None else self.max

    def display(self):
        print("Min: %i Max: %i Current: %i" % (self.min, self.max, self.current))

    def add(self, amount):
        if amount > 0:
            if (self.current + amount) < self.max:
                self.current += amount
            else:
                self.current = self.max
        else:
            if settings.get("debug"):
                self.log.warn("pool.py (add): converting value to positive number")
            self.add(abs(amount))

    def sub(self, amount):
        if amount > 0:
            if (self.current - amount) > self.min:
                self.current -= amount
            else:
                self.current = self.min
        else:
            if settings.get("debug"):
                self.log.warn("pool.py (add): converting value to positive number")
            self.sub(abs(amount))

    def __add__(self, amount):
        self.add(amount)

    def __sub__(self, amount):
        self.sub(amount)

########### Tests #############
def test_add():
    health = Pool(_min=0, _max=100, current=0)
    health.add(20)
    assert(health.current == 20)
    health.add(-20)
    assert(health.current == 40)
    health.add(600)
    assert(health.current == health.max)

def test___add__():
    health = Pool(_min=0, _max=100, current=0)
    health + 20
    assert(health.current == 20)
    health + -20
    assert(health.current == 40)
    health + 600
    assert(health.current == health.max)

def test_sub():
    health = Pool()
    health.sub(20)
    assert(health.current == 80)
    health.sub(-20)
    assert(health.current == 60)
    health.sub(600)
    assert(health.current == health.min)

def test_sub():
    health = Pool()
    health - 20
    assert(health.current == 80)
    health - -20
    assert(health.current == 60)
    health - 600
    assert(health.current == health.min)

def test_display():
    health = Pool()
    health.display()
