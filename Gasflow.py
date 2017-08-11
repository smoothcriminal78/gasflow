import json

class Node(object):

    def __init__(self, id, incidents):
        self._id = id
        self.incidents = incidents

    def __str__(self):
        return 'Node'

class Consumer(Node):
    """
    Args:
        q - consumption
        p - in pressure
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'])
        self.p = data['p'] if data['p'] else data['p']
        self.q = data['q'] if data['q'] else data['q']

    def __str__(self):
        return 'Consumer: Id {} Volume {} Pressure {}'.format(self._id, self.q, self.p)

class Source(Node):
    """
    Args:
        q - distrib volume
        p - out pressure
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'])
        self.p = data['p'] if data['p'] else data['p']
        self.q = data['q'] if data['q'] else data['q']

    def __str__(self):
        return 'Source: Id {} Volume {} Pressure {}'.format(self._id, self.q, self.p)

class Pipe(Node):
    """
    Args:
        l: length
        d: diameter
        r: roughness
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'])
        self.length = data['length']
        self.diameter = data['diameter']
        self.roughness = data['roughness']

    def __str__(self):
        return 'Pipe:\nId {}\nLength {}\nDiameter {}'.format(self._id, self.length, self.diameter)

class Valve(Node):
    """
    Args:
        closed: 1 closed, 0 opened
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'])
        self.closed = bool(data['closed'])

    def __str__(self):
        return 'Valve: Id {} closed {}'.format(self._id, self.closed)

with open('D:\python\gasflow\\network.json') as data_file:
    data = json.load(data_file)

consumers = [Consumer(c) for c in data['consumer']]
sources = [Source(s) for s in data['source']]
pipes = [Pipe(p) for p in data['pipe']]
valves = [Valve(v) for v in data['valve']]
nodes = consumers + sources + pipes + valves

def getNodeById(id):
    return next((n for n in nodes if n._id == id), None)

def getNodes(ids):
    return [getNodeById(id) for id in ids]

def buildGraph():
    graph = {}
    for n in nodes:
        graph[n] = getNodes(n.incidents)
    return graph

def findPath(_from, to):
    def constructPath(prev):
        path = []
        while prev != None:
            path.append(prev)
            prev = backtrace[prev]
        return path[::-1]
    toVisit = [_from]
    backtrace = {_from: None}
    cnt = 0
    while len(toVisit) > 0 and cnt < 50:
        candidate = toVisit.pop()
        if type(candidate) == Valve and candidate.closed:
            continue
        if candidate == to:
            return constructPath(candidate)
        for adjNode in getNodes(candidate.incidents):
            if adjNode not in backtrace:
                toVisit.append(adjNode)
                backtrace[adjNode] = candidate
        previous = candidate
        cnt+=1
    return []

g = buildGraph()

def findDistribution():
    return [findPath(s, c) for s in sources for c in consumers]

flows = findDistribution()
for f in flows:
    print([i._id for i in f])
