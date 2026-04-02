num =100
try:
    a = float(input('Enter a number to divide 100 by:'))
    print(num/a)
except ZeroDivisionError:
    print("error: Divison by zero is not allowed.")
except ValueError:
    print("error: please enter a valid number.")
finally:
    print("we still will want to be print this.")
        



print("let's move on to the next part of the code.")

names = ['Alice', 'Bob', '123', 'Charlie']
for name in names:
    try:
        print(name.upper())
    except AttributeError:
        print(f"error: '{name}' is not a string and cannot be converted to uppercase.")

print("uppercase names:", uppercase_names)
print("let's move on to the next part of the code.")
