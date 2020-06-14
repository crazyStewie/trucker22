from .node_2d import Node2D

class VisualNode(Node2D):
    def __init__(self, name:str):
        super().__init__(name)
    
    def _pos_update(self, delta: float):
        super()._pos_update(delta)
        self.draw()
    
    def draw(self):
        pass