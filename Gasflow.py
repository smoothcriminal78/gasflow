from Pipe import Pipe
from Source import Source
from Consumer import Consumer

s = Source(5.5, None)
c = Consumer(100, None)
p = Pipe(100, 50, 0.1, None, None)

p.elem1 = s
p.elem2 = c

print(s)
print(c)
print(p)
