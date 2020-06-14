from .visual_node import VisualNode
from pyglet.sprite import Sprite
from pyglet.image import AbstractImage

class SpriteNode(VisualNode):
    __slots__ = "sprite"
    def __init__(self, name : str, image : AbstractImage):
        super().__init__(name)
        self.sprite : Sprite = Sprite(image)

    def _pos_update(self, delta: float):
        self.sprite.x = self._global_position.x
        self.sprite.y = self._global_position.y
        self.sprite.rotation = self._global_rotation
        super()._pos_update(delta)

    def draw(self):
        self.sprite.draw()
        
