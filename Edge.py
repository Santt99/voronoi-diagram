class Edge(object):
    def __init__(self, from_point, to_point):
        self.from_point = from_point
        self.to_point = to_point

    def __repr__(self):
        return "From: {}, To: {}".format(self.from_point, self.to_point)
