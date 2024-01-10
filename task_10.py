def split_and_display(str):
    # Split the string on hyphens
    substrings = str.split('-')

    # Display each substring
    for substring in substrings:
        print(substring)

inputString = input("Enter the string : ")

# Call the function
split_and_display(inputString)
