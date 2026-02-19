# a = input("Enter an integer: ") # how to make sure input is integer
# a = int(a)
# print(type(a))


# # check odd or even
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# a = 2
# 1 + a  # an expression, which evaluates to 3, but does not do anything with it

# print(1 + a) # a statement, which prints the result

for i in range(4, 1, -1):
    print(i)
# for i in range(4, 1, -1):
#     print(i)

x = 10

def f():
    message = "Hello"
    x = 5
    print(message)
    print(x)
    return x + 1
y = f()
print(x)        
print(y)
print(message)  # this will cause an error because message is not defined in this scope

def f():
    message = "Hello"
    x = 5
    print(message)

    #Draw a triangle
    """
    
    
"""
def draw_square(size):
    for _ in range(size):
        print("Turn right 90 degrees")
        for _ in range(size):
            print("Move forward 1 unit")
draw_square(4)
draw_square(10)
def draw_triangle(size):
    for _ in range(3):
        print("Turn right 120 degrees")
        for _ in range(size):
            print("Move forward 1 unit")
draw_triangle(4)
draw_triangle(10)               
def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        print(f"Turn right {angle} degrees")
        for _ in range(size):
            print("Move forward 1 unit")
draw_polygon(4, 4)
draw_polygon(3, 4)
draw_polygon(10, 4)

def draw_star(size):

import turtle

screen = turtle.Screen()
screen.addshape(🧱)
                

t = turtle.Turtle()
t.shape
t.penup()

create a function to draw a draw_triangle
*
**
***
****


draw a draw_triangle like this (size = 5)
    for _ in range(5):
        print("Turn right 144 degrees")
        for _ in range(size):
            print("Move forward 1 unit")


def draw_triangle(size):
    for i in range(size):
 print(" " * (size - i - 1) + "*" * (2 * i + 1))

draw_triangle(5)
                

# create a function to draw a draw_pyramiad 


🧱🧱🧱🧱
def draw_pyramid(levels):
    for i in range(levels):
        print(" " * (levels - i - 1) + "🧱" * (2 * i + 1)
              
              )













