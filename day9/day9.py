with open('input.txt', 'r') as f:
    input = f.read()

groups_stack_size = 0
score = 0
escaping = False
garbage = False

for c in input:
    if escaping:
        escaping = False
    elif c == '!':
        escaping = True
    elif c == '{' and not garbage:
        groups_stack_size += 1
    elif c== '}' and not garbage:
        score += groups_stack_size
        groups_stack_size -= 1
    elif c == '<':
        garbage = True
    elif c == '>':
        garbage = False

print(score)




