from SingleBoundNode import SingleBoundNode

class Consumer(SingleBoundNode):

    """
    Args:
        q - consumption
    """
    def __init__(self, q, e):
        SingleBoundNode.__init__(self, e)
        self.q = q

    def __str__(self):
        return 'Consumer: Volume {} Elem {}\n'.format(self.q, self.elem)
