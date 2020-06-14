from .node import Node
from ..utils.math_utils import Vector2

class Node2D(Node):
    position : Vector2
    _global_position : Vector2
    rotation : float
    _global_rotation : float
    def __init__(self, name:str):
        super().__init__(name)
        self.position : Vector2 = Vector2(0, 0)
        self._global_position : Vector2 = Vector2(0, 0)
        self.rotation : float = 0.0
        self._global_rotation : float = 0.0
    
    def _update_global(self):
        if self.parent is not None and isinstance(self.parent, Node2D):
            self._global_position = self.parent._global_position + self.position
            self._global_rotation = self.parent._global_rotation + self.rotation
        else:
            self._global_position = self.position
            self._global_rotation = self.rotation
        
    def _pos_update(self, delta:float):
        super()._pos_update(delta)
        self._update_global()