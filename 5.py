try:
    with open('input.txt', 'r') as file:
        numbers = file.readlines()

    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    result = num1 / num2 + num3

except (ValueError) as e:
    result = "data error"
except (ZeroDivisionError) as e:
    result = "division by 0"

with open('output.txt', 'w') as file:
    file.write(str(result))
