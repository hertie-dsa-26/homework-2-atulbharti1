# test_circle.py

from circle import Circle
import math


def test_perimeter():
    c = Circle(1)
    assert c.perimeter() == 2 * math.pi


def test_area():
    c = Circle(1)
    assert c.area() == math.pi


def test_zero_radius():
    c = Circle(0)
    assert c.perimeter() == 0
    assert c.area() == 0


def test_negative_radius():
    c = Circle(-2)
    assert c.perimeter() == -4 * math.pi
    assert c.area() == math.pi * 4 