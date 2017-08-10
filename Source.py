from SingleBoundNode import SingleBoundNode

class Source(SingleBoundNode):

    """
    Args:
        p - out pressure
    """
    def __init__(self, p, e):
        SingleBoundNode.__init__(self, e)
        self.out_pressure = p

    def __str__(self):
        return 'Source: Pressure {} Elem {}\n'.format(self.out_pressure, self.elem)
