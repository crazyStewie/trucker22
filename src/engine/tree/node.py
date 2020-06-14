from typing import List

class Node:
    _children : List['Node']
    parent : 'Node'
    name : str
    in_tree : bool
    def __init__(self, name : str):
        self._children = []
        self.parent = None
        self.name = name
        self.in_tree = False

    def add_child(self, child : 'Node'):
        if child.parent is not None:
            raise Exception("Node {} already has a parent {}", child.name, child.parent.name)
        elif self.get_child_by_name(child.name):
            raise Exception("Node {} already has a child with the name {}", self.name, child.name)
        else:
            child.parent = self
            self._children.append(child)
        if self.in_tree:
            if not child.in_tree:
                child.add_to_tree()
        elif child.in_tree:
            child.remove_from_tree()
    
    def get_child_by_name(self, name : str) -> 'Node':
        for child in self._children:
            if child.name == name:
                return child
        return None

    def get_child_by_id(self, id : int) -> 'Node':
        if id > len(self._children) - 1:
            return None
        else:
            return self._children[id]

    def _update(self, delta : float):
        self._pre_update(delta)
        self.update(delta)
        self._pos_update(delta)
        for child in self._children:
            child._update(delta)
        pass

    def update(self, delta: float):
        pass

    def _pre_update(self, delta: float):
        pass

    def _pos_update(self, delta: float):
        pass

    def add_to_tree(self):
        pass

    def remove_from_tree(self):
        pass