from pico2d import *
import gfw
import gobj
import math
from zombie import Zombie
import plant

def collides_distance(a, b):  # 구충돌
    ax, ay = a.pos
    bx, by = b.pos
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    radius_sum = a.radius + b.radius
    return distance_sq < radius_sum ** 2

def Get_Distance(pos1, pos2):
    ax, ay = pos1
    bx, by = pos2
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)


def check_collision_bullet_zombie():
    for bullet in gfw.world.objects_at(gfw.layer.bullet):
        for zombie in gfw.world.objects_at(gfw.layer.zombie):
            if gobj.collides_box(bullet, zombie):
                gfw.world.remove(bullet)
                zombie.collision_event(10)


def check_collision_cherrybomb(pos):
    for zombie in gfw.world.objects_at(gfw.layer.zombie):
        if Get_Distance(pos, zombie.pos) < 100:
            zombie.collision_event(-1)

def check_collision_plant_zombie():
    for p in gfw.world.objects_at(gfw.layer.plant):
        if p.name == 'CherryBomb' or p.state != plant.STATE_MOUNT:
            continue
        for zombie in gfw.world.objects_at(gfw.layer.zombie):
            if gobj.collides_box(p, zombie):
                p.collision_event(zombie.Att)
                zombie.collision_event(0)




