def add_two_numbers() -> int:
    lines = input()
    strings = lines.split(",")
    sum = 0

    for s in strings:
        sum += int(s)

    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
