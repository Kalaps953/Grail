from __future__ import annotations
import pygame as pg
import math
import grailLogicModule as glm


sprites = {glm.signal.DigitalSignal: pg.image.load('random_image.png')}


class Camera:
    def __init__(self, pos: glm.Pos, size: glm.Pos):
        self.pos = pos
        self.size = size

    def draw(self, display: pg.Surface, obj: glm.Signal | glm.Block):
        sprite = sprites[type(obj)]
        sprite.get_size()

