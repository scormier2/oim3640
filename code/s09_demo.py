for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1



    response = ""
while response != "quit":
    response = input("Enter command: ")
    print(f"You said: {response}")

# break - exit the loop immediately
for word in words:
    if word == "target":
        print("Found it!")
        break

# continue - skip to the next iteration
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)  # prints odd numbers only

for letter in 'Gadsby':
    print(letter, end=' ')

#break exit loop immediatly
words = ["hello", "world", "target", "python"]
for word in words:
    if word == "target":
        print("Found it!")
        break


words = ["hello", "world", "target", "python"]
for word in words:
    print('checking:', word)  # prints all words including "target"
    if word == "target":
        print("Found it!\n")
        continue
    print("not the target\n")  # prints all words except "target"

# continue - skip to the next iteration
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)  # prints odd numbers only

def f(n):
    for num in range(n):
        if num % 2 == 0:
            continue
        return(num)  # returns the first odd number less than n
    
result = f(10)
print(result)  # prints 1, which is the first odd number less than 10


