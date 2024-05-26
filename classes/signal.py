class Signal:
    def __init__(self, id: int = 0, layer: int = 0):
        self.id = id
        self.layer = layer


class DigitalSignal(Signal):
    def __init__(self, power: int = 0, id: int = 0, layer: int = 0):
        super().__init__(id, layer)
        self.power = power

    # TODO: __add__, __sub__, comparing and something else


class BooleanSignal(Signal):
    def __init__(self, state: bool = False, id: int = 0, layer: int = 0):
        self.state = state
        super().__init__(id, layer)


class StringSignal(Signal):
    def __init__(self, text: str = '', id: int = 0, layer: int = 0):
        self.text = text
        super().__init__(id, layer)

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
