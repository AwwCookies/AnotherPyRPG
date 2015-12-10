from collections import defaultdict


class Manager():
    def __init__(self, level=1, max_level=100):
        self.next_level = None
        self.cur_level = level
        self.max_level = max_level
        self.table = self.gen_table(level, max_level)
        self.exp = self.table[level]

    def gen_table(self, level, max_level):
        table = defaultdict(int)
        for x in xrange(level, max_level+1):
            table[x] = [y * 8 for y in xrange(level, max_level+1)][x-1]
        return table

    def level_up(self):
        for x in xrange(self.max_level):  #TODO do this someother way
            if self.cur_level != self.max_level:
                if self.exp >= self.table[self.cur_level + 1]:
                    self.cur_level += 1

    def add_exp(self, amount):
        self.exp += amount

    def needed_exp(self):
        return int(self.table[self.cur_level + 1])

########### Tests #############
