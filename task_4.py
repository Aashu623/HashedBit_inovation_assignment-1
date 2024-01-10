def compareNumbers(numbers):
    if len(numbers) > 0:
        return numbers[0] == numbers[-1]
    else:
        return False


# Get the number of elements in the list from the user
N = int(input("Enter the number of elements: "))

# Initialize an empty list to store the numbers
numbers = []

for i in range(N):
    # Get input from the user
    num = int(input(f"Enter number {i + 1}: "))

    numbers.append(num)

result = compareNumbers(numbers)
print(result)
