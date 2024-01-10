for i in range(5, 11):  # Iterate from 5 to 10 
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):  # Multiply by numbers 1 through 10
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Add a blank line between tables
