from marching_squares import draw_curve
import math
import os

#
# Please install pytest with the command: pip install pytest
# And run the command: pytest -q test_marching_squares.py
#

# Precision
D = 0.1

def test_draw_circle():
    R = 100
    output = "circle.eps"
    def f(x, y):
        return pow(x,2) + pow(y, 2) - pow(R, 2)

    draw_curve(f, output, -R, -R, R, R, D)
    assert os.path.exists(output)

def test_draw_tan():
    R = 5
    output = "tan.eps"
    def f(x, y):
        return math.tan(x) - y

    draw_curve(f, output, -R, -R, R, R, D)
    assert os.path.exists(output)

def test_draw_sin():
    R = 5
    output = "sin.eps"
    def f(x, y):
        return math.sin(x) - y

    draw_curve(f, output, -R, -R, R, R, D)
    assert os.path.exists(output)