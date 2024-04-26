with open('input.txt', 'r') as f:
    a = f.read()
c = a.upper()
with open('output.txt', 'w') as f:
    f.write(c)