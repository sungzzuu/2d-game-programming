from pico2d import *
import gfw
import gobj
from zombie import Zombie

def collides_distance(a, b):  # 구충돌
    ax, ay = a.pos
    bx, by = b.pos
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    radius_sum = a.radius + b.radius
    return distance_sq < radius_sum ** 2

def check_collision():
    for bullet in gfw.world.objects_at(gfw.layer.bullet):
        for zombie in gfw.world.objects_at(gfw.layer.zombie):
            if gobj.collides_box(bullet, zombie):
                gfw.world.remove(bullet)
                zombie.collision_event(10)

