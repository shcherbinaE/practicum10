import os
directory = 'simple'
if not os.path.exists(directory):
    os.makedirs(directory)

with open('input.txt', 'r') as f:
    lines = f.readlines()

with open(os.path.join(directory, 'output.txt'), 'w') as f:
    for i in range(1, len(lines), 2):
        f.write(lines[i])