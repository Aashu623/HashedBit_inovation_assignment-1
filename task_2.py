# input from the user
inputStr = input("Enter a string: ")

# store characters at even index numbers
result = ""
for index in range(0, len(inputStr), 2):
    result += inputStr[index] + " "

print(f"Characters at even index numbers: {result}")
