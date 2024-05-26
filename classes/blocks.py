from .signal import Signal
import pygame as pg
import math


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos_to_arr(self):
        return [int(self.x), int(self.y)]

    def draw(self, display: pg.Surface, color):
        pg.draw.circle(display, color, self.pos_to_arr(), 2)

    @staticmethod
    def arr_to_pos(arr):
        return Pos(arr[0], arr[1])

    def __str__(self):
        return f'x={self.x}; y={self.y}'

    # +
    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
        elif isinstance(other, float):
            return Pos(self.x + other, self.y + other)
        elif isinstance(other, int):
            return Pos(self.x + other, self.y + other)

    # -
    def __sub__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x - other.x, self.y - other.y)
        elif isinstance(other, float):
            return Pos(self.x - other, self.y - other)
        elif isinstance(other, int):
            return Pos(self.x - other, self.y - other)

    # /
    def __truediv__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x / other.x, self.y / other.y)
        elif isinstance(other, float):
            return Pos(self.x / other, self.y / other)
        elif isinstance(other, int):
            return Pos(self.x / other, self.y / other)

    # *
    def __mul__(self, other):
        if isinstance(other, Pos):
            return Pos(self.x * other.x, self.y * other.y)
        elif isinstance(other, float):
            return Pos(self.x * other, self.y * other)
        elif isinstance(other, int):
            return Pos(self.x * other, self.y * other)

    # **
    def __pow__(self, power, modulo=None):
        if isinstance(power, Pos):
            return Pos(math.pow(self.x, power.x), math.pow(self.y, power.y))
        elif isinstance(power, float):
            return Pos(math.pow(self.x,  power), math.pow(self.y, power))
        elif isinstance(power, int):
            return Pos(math.pow(self.x,  power), math.pow(self.y, power))

    # <
    def __lt__(self, other):
        if isinstance(other, Pos):
            return self.x <= other.x or self.y <= other.y
        elif isinstance(other, float):
            return self.x <= other or self.y <= other
        elif isinstance(other, int):
            return self.x <= other or self.y <= other

    # >
    def __gt__(self, other):
        if isinstance(other, Pos):
            return self.x >= other.x or self.y >= other.y
        elif isinstance(other, float):
            return self.x >= other or self.y >= other
        elif isinstance(other, int):
            return self.x >= other or self.y >= other

    # <=
    def __le__(self, other):
        if isinstance(other, Pos):
            return self.x <= other.x and self.y <= other.y
        elif isinstance(other, float):
            return self.x <= other and self.y <= other
        elif isinstance(other, int):
            return self.x <= other and self.y <= other

    # >=
    def __ge__(self, other):
        if isinstance(other, Pos):
            return self.x >= other.x and self.y >= other.y
        elif isinstance(other, float):
            return self.x >= other and self.y >= other
        elif isinstance(other, int):
            return self.x >= other and self.y >= other


class Cell:
    def __init__(self, pos: Pos, blocks: dict[int, "Block"] = {}, signals: dict[int, Signal] = {}):
        self.pos = pos
        self._blocks = blocks
        self.signals = signals

    def place_block(self, obj, layer: int = 0) -> None:
        self._blocks[layer] = obj

    def remove_block(self, layer: int = 0) -> None:
        self._blocks.pop(layer)

    @property
    def blocks(self) -> dict[int, "Block"]:
        return self._blocks


class Grid:
    def __init__(self, cells: list[Cell]):
        self.cells = cells

    def get_cell(self, pos: Pos):
        for i in self.cells:
            if i.pos == pos:
                return i
        return Cell(pos)

    def set_cell(self, pos: Pos, cell: Cell):
        for i in range(len(self.cells)):
            if self.cells[i].pos == pos:
                self.cells[i] = cell
                return
        self.cells.append(cell)


class Block:
    def __init__(self, cell: Cell, layer: int = 0):
        self.cell = cell
        self.layer = layer

