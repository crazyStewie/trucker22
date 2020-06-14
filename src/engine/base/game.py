from ..tree.node import Node
import pyglet

class Game(Node) :
    __slots__ = "root", "window"

    def __init__(self, name : str):
        super().__init__(name)
        self.root : None | Node = None
        self.window : pyglet.window.Window = pyglet.window.Window()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.update(pyglet.clock.tick())
    
    def update(self, delta : float):
        if (self.root):
            self.root._update(delta)