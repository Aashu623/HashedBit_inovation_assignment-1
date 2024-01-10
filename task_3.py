def remove_characters(str, n):
    if n >= 0 and n < len(str):
        result = str[n:]
        return result
    else:
        return str

# Accept a string and an integer 'n' from the user
inputStr = input("Enter a string: ")
n = int(input("Enter the value of 'n': "))

# Remove characters and display the result
result = remove_characters(inputStr, n)
print(f"Resulting string: {result}")
