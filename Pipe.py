from DualBoundNode import DualBoundNode

class Pipe(DualBoundNode):

    """
    Args:
        l: length
        d: diameter
        r: roughness
        e1: Node element1
        e2: Node element2
    """
    def __init__(self, l, d, r, e1, e2):
        DualBoundNode.__init__(self, e1, e2)
        self.length = l
        self.diameter = d
        self.roughness = r

    def __str__(self):
        return 'Pipe:\nLength {}\nDiameter {}\nElem1 {} Elem2 {}\n'.format(self.length, self.diameter, self.elem1, self.elem2)
