from abc import ABC, abstractmethod
import classes.signal as sg
import classes.blocks as bl


class SignalInteractBlock(ABC):
    @abstractmethod
    def on_signal(self, signal: sg.Signal):
        pass