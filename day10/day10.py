r = list(range(0, 256))
input=[129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]
print(r)
skip_size = 0

current_index = 0

offset = 0

for length in input:
    print(r)
    section = r[:length]
    section.reverse()
    r = section + r[length:]

    for k in range(0, length + skip_size):
        r.append(r.pop(0))

    offset = (offset + length + skip_size) % (len(r))
    skip_size += 1

for k in range(0, len(r) - offset):
    r.append(r.pop(0))

print(r)
print (r[0] * r[1])