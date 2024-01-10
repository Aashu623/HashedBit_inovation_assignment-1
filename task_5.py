def createNewList(list1, list2):
    # Filter odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]

    # Filter even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]

    # Combine the odd and even numbers into a new list
    newList = odd_numbers + even_numbers

    return newList


# Get input from the user for List 1
N_1 = int(input("Enter the number of elements for list 1: "))
list1 = []
for i in range(N_1):
    num = int(input(f"Enter number {i + 1}: "))

    list1.append(num)

# Get input from the user for List 2
N_2 = int(input("Enter the number of elements for list 2: "))
list2 = []
for i in range(N_2):
    num = int(input(f"Enter number {i + 1}: "))

    list2.append(num)

# Call the function and print the result
resultList = createNewList(list1, list2)
print(resultList)
