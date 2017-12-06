input="""
10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6
"""

data = [int(x.strip()) for x in input.split()]

states = set()
state = data


def find_entry_index():
    max_value = None
    i = None
    for x in range(len(data)):
        if max_value is None or data[x] > max_value:
            i = x
            max_value = data[x]
    return i


while True:
    print(state)
    state_key = ';'.join(map(str, state))
    if state_key in states:
        break
    states.add(state_key)

    i = find_entry_index()

    x = data[i]
    data[i] = 0
    while x > 0:
        i += 1
        data[i % len(data)] += 1
        x -= 1


print(len(states))
