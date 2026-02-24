# Week 3 Learning Log

## What did I learn in class this week?

This week focused on functions, abstraction, interface design, and refactoring using the turtle module.

### Turtle Module

Used `turtle` to visualize logic:


import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)


Turtle made loops and geometry visible, which helped connect math + logic.

---

### From Repetition to Loops

Manual square (repetitive):


t.forward(100)
t.left(90)
# repeated 4 times


Cleaner version:


for i in range(4):
    t.forward(100)
    t.left(90)


Key idea: loops eliminate repetition and improve scalability.

---

### Encapsulation (Functions)


def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)


Encapsulation = packaging logic into reusable components.

---

### Generalization

From square → polygon:

def draw_polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)


Now works for triangles, pentagons, hexagons, etc.

Shift: design for *many* cases, not one.

---

### Refactoring & Reuse

Refactoring = improving structure without changing behavior.

Patterns practiced:
- Extract repeated logic into functions
- Add parameters for flexibility
- Rename for clarity

Reused `draw_polygon()` to approximate a circle instead of rewriting loop logic.

Reuse > Rewrite.

---

### Interface Design

A good interface is:
- Simple
- General
- Appropriate level of abstraction

Too specific:
```python
def draw_pentagon(t):
```

Better:
```python
def draw_polygon(t, n, length):
```

Function design affects usability and scalability.

---

### Development Process

1. Start simple
2. Encapsulate
3. Generalize
4. Refactor
5. Document (docstrings)

This reflects how real software is built — iterative and modular.

---

## What challenges did I bump into?

- Moving from concrete thinking (“draw a square”) to abstraction (“design for n sides”).
- Choosing meaningful parameters.
- Debugging visual/geometry logic instead of syntax errors.
- Balancing simplicity vs flexibility in function design.

---

## Reflection

This week shifted my mindset from writing code to designing reusable systems.

Functions aren’t just organization tools — they are the foundation of scalable programming.