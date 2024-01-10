def reverseString(str):
    # Use slicing to reverse the string
    reversed_string = str[::-1]
    return reversed_string

#taking input from user
inputStr = input("Enter any string : ")

# Call the function
result = reverseString(inputStr)

# print the result
print("Reversed string : ", result)
