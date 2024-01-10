def createNewString(str):
    # Check if the input string has at least three characters
    if len(str) >= 3:
        # Calculate the middle index
        middle_index = len(str) // 2

        # Extract the first, middle, and last characters
        newString = str[0] + str[middle_index] + str[-1]

        return newString
    else:
        # If the input string has fewer than three characters, return the original string
        return str


inputStr = input("Enter any string : ")

# Call the function and print the result
resultStr = createNewString(inputStr)
print(resultStr)
