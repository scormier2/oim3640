import turtle

def draw_square(turtle_obj, size=100):
    """Draw a square using the given turtle object and size."""
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)


def draw_spiral(t)
    """
    draw a spiral turn a angle, then draw anoter square
    and so on
    """
    for i in range(36):
        draw_square(t, size=i*50)
        t.right(10)



def main():
    t = turtle.Turtle()
    t.speed(0)  # Set the turtle speed to the fastest
    # draw_square(t, size=50)
    draw_spiral(t)
    turtle.mainloop()  # Keep the turtle graphics window open


if __name__ == "__main__":
    main()