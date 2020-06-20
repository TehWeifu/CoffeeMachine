class Point:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y

    def dist(self, other_point):
        d = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return d

