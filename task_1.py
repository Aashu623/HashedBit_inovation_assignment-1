# Initialize the first number
prevNum = 0

for i in range(1, 11):
    # Calculate the sum of the current and previous number
    currNum = i
    sum = currNum + prevNum
    
    # Print the result
    print(f"Current: {currNum}, Previous: {prevNum}, Sum: {sum}")
    
    # Update the previous number
    prevNum = currNum
