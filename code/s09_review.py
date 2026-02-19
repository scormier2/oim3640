def mystery_function(n):
    if n == 0:
        return 1
    else:
        return n * mystery_function(n-1)

def mystery_function(n):
    if n > 0:
        return "positive"
    else:
        return "non-positive"
        print("done")

#result = mystery(5)
#print(result)

x = 15
y = x > 10 and x < 200
print(type(y))
print(true)

x = 15
y = x > 10 or x < 2
print(type(y))
print(y)



def check(n):
    if n % 2 == 0:
        if n % 3 == 0:
            print("A")
        else:
            print("B")
    else:
        print("C")

check(8)
check(6)