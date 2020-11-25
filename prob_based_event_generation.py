import random

def random_event(data):

    r = random.uniform(0, 1)

    s = 0

    for event, prob in data.items():

        s += prob

        if s >= r:

            return event


d = {}

d[0] = 0.1
d[1] = 0.4
d[2] = 0.5

for i in range(10):

    print (random_event(d))
