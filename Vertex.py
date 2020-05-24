class Vertex(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "(x: {}, y: {})".format(self.x, self.y)

    def to_list(self):
        return [int(self.x), int(self.y)]
