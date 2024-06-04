import classes.blocks as bl


class Signal:
    def __init__(self,
                 cell: bl.Cell = None,
                 id: int = 0,
                 layer: int = 0,
                 vector: bl.Pos = bl.Pos(0, 1)):
        self.cell = cell
        self.id = id
        self.layer = layer
        self.vector = vector

    def update(self, grid: bl.Grid):
        self.cell.signals.pop(self.layer)
        self.cell = grid.get_cell(self.cell.pos + self.vector)
        self.cell.signals[self.layer] = self


class DigitalSignal(Signal):
    def __init__(self, cell: bl.Cell = None, power: int = 0, id: int = 0, layer: int = 0, vector: bl.Pos = bl.Pos(0, 1)):
        super().__init__(cell, id, layer, vector)
        self.power = power

    def update(self, grid: bl.Grid):
        self.cell.signals.pop(self.layer)
        self.cell = grid.get_cell(self.cell.pos + self.vector)
        self.cell.signals[self.layer] = self

    # TODO: __add__, __sub__, comparing and something else


class BooleanSignal(Signal):
    def __init__(self, cell: bl.Cell = None, state: bool = False, id: int = 0, layer: int = 0, vector: bl.Pos = bl.Pos(0, 1)):
        super().__init__(cell, id, layer, vector)
        self.state = state

    def update(self, grid: bl.Grid):
        self.cell.signals.pop(self.layer)
        self.cell = grid.get_cell(self.cell.pos + self.vector)
        self.cell.signals[self.layer] = self


class StringSignal(Signal):
    def __init__(self, cell: bl.Cell = None, text: str = '', id: int = 0, layer: int = 0, vector: bl.Pos = bl.Pos(0, 1)):
        super().__init__(cell, id, layer, vector)
        self.text = text

    def update(self, grid: bl.Grid):
        self.cell.signals.pop(self.layer)
        self.cell = grid.get_cell(self.cell.pos + self.vector)
        self.cell.signals[self.layer] = self

    def __add__(self, other):
        if isinstance(other, str):
            return self.text + other
        if isinstance(other, StringSignal):
            return self.text + other.text
        raise AttributeError(f'adding \'{type(other)}\' to \'StringSignal\'')

    def __lt__(self, other):
        if isinstance(other, str):
            return self.text < other
        if isinstance(other, StringSignal):
            return self.text < other.text
        raise TypeError(f'comparing \'{type(other)}\' to \'StringSignal\'')

    def __gt__(self, other):
        if isinstance(other, str):
            return self.text > other
        if isinstance(other, StringSignal):
            return self.text > other.text
        raise TypeError(f'comparing \'{type(other)}\' to \'StringSignal\'')

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.text
        if isinstance(other, StringSignal):
            return other.text == self.text
        return False

    def __ge__(self, other):
        if isinstance(other, str):
            return self.text >= other
        if isinstance(other, StringSignal):
            return self.text >= other.text
        raise TypeError(f'comparing \'{type(other)}\' to \'StringSignal\'')

    def __le__(self, other):
        if isinstance(other, str):
            return self.text <= other
        if isinstance(other, StringSignal):
            return self.text <= other.text
        raise TypeError(f'comparing \'{type(other)}\' to \'StringSignal\'')

    def __len__(self):
        return len(self.text)
