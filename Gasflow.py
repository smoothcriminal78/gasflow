import json
from math import *
gas_viscosity = 14.3 * 10 ** -6 # standard conditions
gas_density = 0.73 # standard conditions
gas_temp = 273.5
roughness = 0.1
air_temp = 293.15

class Node(object):

    def __init__(self, id, incidents, q, p):
        self._id = id
        self.incidents = incidents
        self.q = q
        self.p = p

    def __str__(self):
        return 'Node'

class Consumer(Node):
    """
    Args:
        q - consumption
        p - in pressure
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'], data['q'], data['p'])

    def __str__(self):
        return 'Consumer: Id {} Volume {} Pressure {}'.format(self._id, self.q, self.p)

class Source(Node):
    """
    Args:
        q - distrib volume
        p - out pressure
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'], data['q'], data['p'])

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
        Node.__init__(self, data['_id'], data['incidents'], 0, 0)
        self.length = data['length']
        self.diameter = data['diameter']
        self.roughness = data['roughness']

    def __str__(self):
        return 'Pipe:\nId {}\nLength {}\nDiameter {}'.format(self._id, self.length, self.diameter)

    """ Re number """
    def getFrictionCoef():
        re_num = (0.0354 * self.q) / (self.diameter * gas_viscosity)
        coef = 0
        if re_num <= 2000: # laminar mode
            coef = 64 / re_nu
        elif re_num > 2000 and re_num <= 4000: # critical mode
            coef = 0.0025 * (re_num * 0.333)
        else:
            if re_num * (roughness / self.diameter): # pipe wall smoothness
                if re_num > 4000 and re_num <= 100000:
                    coef = 0.3164 / (re_num * 0.25)
                else:
                    coef = 1 / ((1.82 * log10(re_num) - 1.64) ** 2)
            else:
                coef = 0.11 * ((roughness / self.diameter + 68 / re_num) ** 0.25)

    """ Avg compressibility of gas """
    def getCompressibilityCoef():
        a1 = -0.39 +
        1 +

    def getPressureDrop():
        fc = getFrictionCoef()
        4.324 * 10 ** -7 * fc * self.q * abs(self.q) * gas_density * self.length * gas_temp / d ** 5

class Valve(Node):
    """
    Args:
        closed: 1 closed, 0 opened
    """
    def __init__(self, data):
        Node.__init__(self, data['_id'], data['incidents'], 0, 0)
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
        q = prev.q
        while prev != None:
            path.append(prev)
            prev.q += q
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

# def calcPressureDrop():

flows = findDistribution()
for f in flows:
    print([(i._id, i.q) for i in f])
