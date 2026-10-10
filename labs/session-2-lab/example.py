try:
    a = int(input())
    b = int(input())
    ans = a/b
    file = open("output.txt", "r")
    print(ans)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.",e)
except ValueError as e:
    print("Error: Invalid input. Please enter numeric values.",e)
except Exception as e:
    print("An unexpected error occurred.",e)
finally:
    print("Program Executed")
