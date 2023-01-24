def fibonacci():
    numbers = [0, 1]
    index = 0

    while True:
        numbers.append(numbers[-1] + numbers[-2])
        yield numbers[index]
        index += 1


generator = fibonacci()
for i in range(5):
    print(next(generator))
