from __future__ import annotations
import grailLogicModule.signal as sg
import pygame as pg
import math
import abstraction as abst


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
            return Pos(math.pow(self.x, power), math.pow(self.y, power))
        elif isinstance(power, int):
            return Pos(math.pow(self.x, power), math.pow(self.y, power))

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

    def __eq__(self, other):
        if isinstance(other, Pos):
            return other.x == self.x and other.y == self.y


class Cell:
    def __init__(self, pos: Pos, blocks: dict[int, Block] = {}, signals: dict[int, sg.Signal] = {}):
        self._pos = pos
        self._blocks = blocks
        self.signals = signals
        for i in self._blocks.keys():
            self._blocks[i].cell = self
        for i in self.signals.keys():
            self.signals[i].cell = self

    def __str__(self):
        return f'{self._pos}'

    def place_block(self, obj, layer: int = 0) -> None:
        self._blocks[layer] = obj

    def remove_block(self, layer: int = 0) -> None:
        self._blocks.pop(layer)

    @property
    def blocks(self) -> dict[int, Block]:
        return self._blocks

    @property
    def pos(self) -> Pos:
        return self._pos


class Grid:
    def __init__(self, cells: list[Cell] = []):
        self.cells = cells

    def get_cell(self, pos: Pos):
        for i in self.cells:
            if i.pos == pos:
                return i
        return Cell(pos)

    def set_cell(self, cell: Cell):
        for i in range(len(self.cells)):
            if self.cells[i].pos == cell.pos:
                self.cells[i] = cell
                return
        self.cells.append(cell)


class Block:
    def __init__(self, cell: Cell = None, layer: int = 0):
        self.cell = cell
        self.layer = layer


class ArrowBlock(Block, abst.SignalInteractBlock):
    def __init__(self, cell: Cell = None, layer: int = 0, direct: int = 0):
        super().__init__(cell, layer)
        if direct < 0 or direct > 3:
            raise ValueError('ArrowBlock.direct have to be in range from 0 to 3')
        self._direct = direct

    def on_signal(self, signal: sg.Signal):
        match self._direct:
            case 0:
                signal.vector = Pos(0, 1)
            case 1:
                signal.vector = Pos(1, 0)
            case 2:
                signal.vector = Pos(0, -1)
            case 3:
                signal.vector = Pos(-1, 0)
            case _:
                raise ValueError('ArrowBlock.direct have to be in range from 0 to 3')

    @property
    def direct(self):
        return self._direct

    @direct.setter
    def direct(self, value):
        if value < 0 or value > 3:
            raise ValueError('ArrowBlock.direct have to be in range from 0 to 3')
        self._direct = value
