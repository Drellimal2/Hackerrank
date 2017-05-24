n = int(input())
steps = list(input())
sea_level = True
level = 0
valleys = 0
mountains = 0
for step in steps:
    if step == 'U':
        level += 1
        if level == 0:
            valleys += 1
    elif step == 'D':
        level -= 1
        if level == 0:
            mountains += 1
print(valleys)