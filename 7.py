with open('input.txt', 'r') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if '100' not in line]

with open('input.txt', 'w') as file:
    for line in filtered_lines:
        file.write(line)
