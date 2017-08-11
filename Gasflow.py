import json
from pprint import pprint

class Node:
    """
    Args:
        q - consumption
        p - out pressure
    """
    def __init__(self, data):
        self._id = int(data['_id'])
        self.pressure = float(data['p']) if data['p'] else data['p']
        self.q = float(data['q']) if data['q'] else data['q']

    def __str__(self):
        return 'Node: Volume {} Pressure {}'.format(self.q, self.p, self.elem)

class Pipe:
    """
    Args:
        l: length
        d: diameter
        r: roughness
    """
    def __init__(self, data):
        self._id = int(data['_id'])
        self.length = float(data['length'])
        self.diameter = float(data['diameter'])
        self.roughness = float(data['roughness'])

    def __str__(self):
        return 'Pipe:\nLength {}\nDiameter {}'.format(self.length, self.diameter, self.elem1, self.elem2)


with open('D:\python\gasflow\\network.json') as data_file:
    data = json.load(data_file)

print(data)

pipes, nodes = [], []
for p in data['pipe']:
    pipes.append(Pipe(p))
for n in data['node']:
    nodes.append(Node(n))

pprint(pipes)
pprint(nodes)
