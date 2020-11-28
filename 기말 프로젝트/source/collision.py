from pico2d import *
import gfw

def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    radius_sum = a.radius + b.radius
    return distance_sq < radius_sum ** 2

