with open('input.txt', 'r') as f:
    current_date = f.readline().strip()
    rental_date = []
    f.readline()

    for line in f:
        cell_number, date = line.split()
        day, month = map(int, date.split('.'))
        rental_date.append((int(cell_number), day, month))

with open('output.txt', 'w') as f:
    for cell, day, month in rental_date:
        rental_day = int(current_date.split('.')[0])
        rental_month = int(current_date.split('.')[1])
        if (rental_month == month and rental_day - day > 3) or (rental_month != month and (30 - day + rental_day) > 3):
            f.write(f"{cell}\n")