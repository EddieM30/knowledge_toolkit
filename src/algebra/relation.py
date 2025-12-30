class Relation:
    def __init__(self, pairs=None):
        self.pairs = set(pairs) if pairs else set()

    @property
    def domain(self):
        return {pair[0] for pair in self.pairs}

    @property
    def range(self):
        return {pair[1] for pair in self.pairs}
