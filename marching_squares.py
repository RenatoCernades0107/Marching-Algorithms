import numpy as np
import matplotlib.pyplot as plt
import random as rd


N = 1000

class point:
    x: int = 0
    y: int = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def to_array(self):
        return np.array([self.x, self.y])


class square:
    p1: point
    p2: point
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def to_array(self):
        return np.array([self.p1.to_array(), self.p2.to_array()])

    def draw_segment(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y])

    def draw_square(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p1.y])
        plt.plot([self.p1.x, self.p1.x], [self.p1.y, self.p2.y])
        plt.plot([self.p2.x, self.p2.x], [self.p2.y, self.p1.y])
        plt.plot([self.p2.x, self.p1.x], [self.p2.y, self.p2.y])


def add_segments(func, box: square, segments: list[square]):
    upl = func(box.p1.x, box.p2.y) > 0
    upr = func(box.p2.x, box.p2.y) > 0
    dwnl = func(box.p1.x, box.p1.y) > 0
    dwnr = func(box.p2.x, box.p1.y) > 0

    xmin = box.p1.x
    xmax = box.p2.x
    ymin = box.p1.y
    ymax = box.p2.y

    mid_x_ymin = point((xmax+xmin)/2,ymin)
    mid_y_xmin = point(xmin, (ymax+ymin)/2)
    mid_y_xmax = point(xmax, (ymax+ymin)/2)
    mid_x_ymax = point((xmax+xmin)/2,ymax)


    # Caso 1 y 14
    if ((upr and upl and dwnr and not dwnl) or (not upr and not upl and not dwnr and dwnl)):
        segments.append( square(mid_x_ymin, mid_y_xmin) )
    
    # Caso 2 y 13
    if ((upr and upl and not dwnr and dwnl) or (not upr and not upl and dwnr and not dwnl)):
        segments.append( square(mid_x_ymin, mid_y_xmax) )
    
    # Caso 3 y 12
    if ((upr and upl and not dwnr and not dwnl) or (not upr and not upl and dwnr and dwnl)):
        segments.append( square(mid_y_xmin, mid_y_xmax) ) 

    # Caso 4 y 11
    if ((not upr and upl and dwnr and dwnl) or (upr and not upl and not dwnr and not dwnl)):
        segments.append( square(mid_x_ymax, mid_y_xmax) )
    
    # Caso 5
    if (not upr and upl and dwnr and not dwnl):
        segments.append( square(mid_y_xmin, mid_x_ymax) )
        segments.append( square(mid_x_ymin, mid_y_xmax) )

    # Caso 10
    if (upr and not upl and not dwnr and dwnl):
        segments.append( square(mid_x_ymax, mid_y_xmin) )
        segments.append( square(mid_y_xmax, mid_x_ymin) )

    # Caso 6 y 9
    if ((not upr and upl and not dwnr and dwnl) or (upr and not upl and dwnr and not dwnl)):
        segments.append( square(mid_x_ymin, mid_x_ymax) )
    
    # Caso 7 y 8
    if ((not upr and upl and not dwnr and not dwnl) or (upr and not upl and dwnr and dwnl)):
        segments.append( square(mid_y_xmin, mid_x_ymax) )
    


def divide_box(box: square) -> list:
    mid_point = point((box.p1.x + box.p2.x)/2, (box.p1.y + box.p2.y)/2)
    mid_top_point = point((box.p1.x + box.p2.x)/2, box.p2.y)
    mid_bot_point = point((box.p1.x + box.p2.x)/2, box.p1.y)
    mid_left_point = point(box.p1.x, (box.p1.y + box.p2.y)/2)
    mid_right_point = point(box.p2.x, (box.p1.y + box.p2.y)/2)

    # Top right
    s1 = square(mid_point, box.p2)
    # Top left
    s2 = square(mid_left_point, mid_top_point)
    # Bottom right
    s3 = square(mid_bot_point, mid_right_point)
    # Bottom left
    s4 = square(box.p1, mid_point)

    return [s1, s2, s3, s4]


def rand_point(box: square):
    randx = (rd.random()*(box.p2.x - box.p1.x) ) + box.p1.x
    randy = (rd.random()*(box.p2.y - box.p1.y) ) + box.p1.y
    return point(randx, randy)


def _marching_squares(func, box: square, max_depth: int, squares: list[square]):
    if (abs(box.p1.x - box.p2.x) <= max_depth):
        squares.append(box)
        return

    isExtern = True
    isIntern = True
    isBorder = False

    for _ in range(N):
        p: point = rand_point(box)
        value: float = func(p.x, p.y)
        if (value > 0):
            isIntern = False
        
        elif (value < 0):
            isExtern = False
        
    if (not isExtern and not isIntern):
        isBorder = True
    
    if (isBorder):
        boxes = divide_box(box)
        _marching_squares(func, boxes[0], max_depth, squares)
        _marching_squares(func, boxes[1], max_depth, squares)
        _marching_squares(func, boxes[2], max_depth, squares)
        _marching_squares(func, boxes[3], max_depth, squares)


def draw_curve(func, output_file: str, min_x:float, min_y:float, max_x: float, max_y: float, precision: float):
    squares = []
    box = square(point(min_x, min_y), point(max_x, max_y))

    _marching_squares(func, box, precision, squares)
    segments = []
    
    for sq in squares:
        add_segments(func, sq, segments)

    for seg in segments:
        plt.plot([seg.p1.x, seg.p2.x], [seg.p1.y, seg.p2.y])

    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.savefig(output_file, format='eps', dpi=1200)
    plt.clf()

