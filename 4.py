with open('input.txt', 'r') as file:
    lines = file.readlines()
long_lines = [line for line in lines if len(line) > 20]
with open('output.txt', 'w') as file:
    for line in long_lines:
        file.write(line)
