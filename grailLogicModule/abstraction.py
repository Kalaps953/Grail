from abc import ABC, abstractmethod
import grailLogicModule.signal as sg
import grailLogicModule.blocks as bl


class SignalInteractBlock(ABC):
    @abstractmethod
    def on_signal(self, signal: sg.Signal):
        pass
