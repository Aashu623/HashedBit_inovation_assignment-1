def countChars(str):
    # Initialize an empty dictionary
    occurrencesOfChar = {}

    # Iterate through each character
    for char in str:
        # Update the count for the current character
        occurrencesOfChar[char] = occurrencesOfChar.get(char, 0) + 1

    return occurrencesOfChar


inputStr = input("Enter any string : ")

# Call the function
result = countChars(inputStr)

print("Character occurrences : ")
for char, count in result.items():
    print(f"{char}: {count}")
