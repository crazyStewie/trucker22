import pyglet
from typing import List
from enum import Enum

class RawInput:
    pass

class RawInputKey(RawInput):
    key : pyglet.window.key

class ActionState(Enum):
    JUST_PRESSED = 0
    JUST_RELEASED = 1
    PRESSED = 2
    RELEASED = 3


class Action:
    name : str
    activators : List[RawInput]
    state : ActionState
    def __init__(self, name : str):
        self.name = name
        self.activators = []
        self.state = ActionState.RELEASED

class Input:
    _instance = None
    window : pyglet.window.Window
    keys : pyglet.window.key.KeyStateHandler
    actions : List[Action]

    def __init__(self, window : pyglet.window.Window, keys : pyglet.window.key.KeyStateHandler):
        self.window = window
        self.keys = keys
        self.actions = []
    
    @classmethod
    def initialize(cls, window : pyglet.window.Window, keys : pyglet.window.key.KeyStateHandler):
        cls._instance = cls(window, keys)
    
    @classmethod
    def instance(cls) -> 'Input':
        if cls._instance is None:
            raise Exception("Input singleton not initialized, please initialize before using")
        return cls._instance


