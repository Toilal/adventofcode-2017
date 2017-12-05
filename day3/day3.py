x = 0
y = 0
i = 1

input = 361527
r = 0
direction = 'RIGHT'
while i < input:
    if direction == 'TOP':
        y += 1
        if y >= r:
            direction = 'LEFT'
    elif direction == 'LEFT':
        x -= 1
        if x <= -r:
            direction = 'BOTTOM'
    elif direction == 'BOTTOM':
        y -= 1
        if y <= -r:
            direction = 'RIGHT'
    elif direction == 'RIGHT':
        x += 1
        if x >= r:
            if x == -y:
                direction = 'RIGHT'
            else:
                r += 1
                direction = 'TOP'
    i += 1

print("i: %s, x: %s, y: %s, distance: %s" % (i, x, y, abs(x) + abs(y)))
