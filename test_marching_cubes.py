from marching_cubes import draw_curve
import math
import os

#
# Please install pytest with the command: pip install pytest
# And run the command: pytest -q test_marching_cubes.py
#


def test_draw_sphere():
    d = 1 # Precision
    limits = [-10, -10, -10, 10, 10, 10] # Limites
    r = 5 # Radio
    output = "sphere.off"
    def f(x, y, z):
        return pow(x,2) + pow(y, 2) + pow(z, 2) - pow(r, 2)

    draw_curve(f, output, limits[0], limits[1], limits[2], limits[3], limits[4], limits[5], d) 
    assert os.path.exists(output)

def test_draw_torus():
    d = 5
    limits = [-100, -100, -100, 100, 100, 100]
    r = 40
    a = 15
    output = "torus.off"
    def f(x, y, z):
        return pow(pow(x,2) + pow(y, 2) + pow(z, 2) + pow(r, 2) - pow(a,2), 2) - 4*pow(r,2)*(pow(x, 2) + pow(y, 2))

    draw_curve(f, output, limits[0], limits[1], limits[2], limits[3], limits[4], limits[5], d) 
    assert os.path.exists(output)

def test_draw_with_heart():
    d = 0.125
    output = "heart.off"
    def f(x, y, z):
        return pow(pow(x,2)+(9/4)*pow(y,2) + pow(z,2)-1,3)-pow(x,2)*pow(z,3)-(9/200)*pow(y,2)*(pow(z,3))

    limits = [-10, -10, -10, 10, 10, 10]
    draw_curve(f, output, limits[0], limits[1], limits[2], limits[3], limits[4], limits[5], d) 
    assert os.path.exists(output)