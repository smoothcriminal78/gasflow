class Node:

    """
    Args:
        q - consumption
        p - out pressure
    """
    def __init__(self, id, q, p):
        self.id = id
        self.q = q
        self.p = p

    def __str__(self):
        return 'Node: Volume {} Pressure {} Elem {}\n'.format(self.q, self.p, self.elem)

class Pipe:

    """
    Args:
        l: length
        d: diameter
        r: roughness
        e1: Node element1
        e2: Node element2
    """
    def __init__(self, l, d, r):
        self.length = l
        self.diameter = d
        self.roughness = r

    def __str__(self):
        return 'Pipe:\nLength {}\nDiameter {}\nElem1 {} Elem2 {}\n'.format(self.length, self.diameter, self.elem1, self.elem2)
