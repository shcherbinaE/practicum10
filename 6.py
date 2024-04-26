try:
    with open('input.txt', 'r') as file:
        data = file.readlines()

    n = int(data[0])
    if n == len(data) - 1:
        result = "YES"
    else:
        result = "NO"

except (ValueError, IndexError):
    result = "ERROR"

with open('output.txt', 'w') as file:
    file.write(result)
