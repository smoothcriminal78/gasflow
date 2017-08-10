from Node import Node

class DualBoundNode(Node):
    def __init__(self, elem1, elem2):
        Node.__init__(self)
        self.elem1 = elem1
        self.elem2 = elem2
