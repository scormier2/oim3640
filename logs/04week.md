# Week 4 - Return Values, Conditionals, Boolean Logic

## What I learned this week

This week focused on deeper function design and decision-making logic.

### 1. Return Values (Deeper Understanding)

Return values allow functions to produce usable results that can:
- Be stored in variables
- Be passed into other functions
- Be used inside expressions

Example:

```python
import math

def area(radius):
    return math.pi * radius ** 2

total = area(5) + area(3)
```

Key shift: functions are not just actions — they are value-producing building blocks.

---

### 2. Incremental Development

Instead of writing a full function at once, we build it step by step.

Example: distance between two points.

Start simple (placeholder):

```python
def distance(x1, y1, x2, y2):
    return 0.0
```

Add intermediate logic:

```python
dx = x2 - x1
dy = y2 - y1
```

Complete:

```python
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2) ** 0.5
```

This approach reduces overwhelm and makes debugging easier.

---

### 3. Composition of Functions

Functions can call other functions.

```python
def circle_area(radius):
    import math
    return math.pi * radius ** 2

def ring_area(outer, inner):
    return circle_area(outer) - circle_area(inner)
```

This builds layered logic instead of duplicating code.

Abstraction on top of abstraction.

---

### 4. Boolean Functions

Functions that return True or False.

```python
def is_even(n):
    return n % 2 == 0
```

Naming convention:
- Start with `is_` or `has_`

Boolean functions improve readability and modular logic.

---

### 5. Conditionals

Decision-making in code using:

- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators (`and`, `or`, `not`)
- if / elif / else structure

Important insights:
- Order matters (first true condition runs)
- Indentation defines logic blocks
- Conditions evaluate to Boolean expressions

---

### 6. Recursion (Intro)

A function that calls itself:

```python
def countdown(n):
    if n <= 0:
        print("Go!")
    else:
        print(n)
        countdown(n - 1)
```

Key rule: must have a base case.

Recursion feels powerful but requires careful stopping conditions.

---

### Python Trivia Fact

The name "Python" comes from Guido van Rossum’s favorite comedy TV show:  
Monty Python’s Flying Circus.

It was not named after the snake.

---

## Code I'm proud of

```python
def is_adult(age):
    return age >= 18 and age < 65
```

Why I like it:
- Combines Boolean logic and comparison operators
- Clean, readable interface
- Can be reused in larger systems

It feels like real decision logic instead of math exercises.

---

## Challenges I faced

- Understanding how return values flow through multiple function calls.
- Writing conditionals in the correct order (small logic mistakes change everything).
- Thinking step-by-step with incremental development instead of trying to “solve it all” at once.
- Recursion was conceptually difficult — especially visualizing the call stack.

I worked through this by testing small inputs and printing intermediate values.

---

## AI usage (if any)

- Asked AI to explain recursive flow step-by-step.
- Used AI to check logic in Boolean expressions.
- Modified output manually to ensure I understood each line.
- Did not copy blindly — used it as a debugging assistant.
- ADD finally I use AI to organize my thoughts for learning logs

---

## Questions going forward

- When should recursion be preferred over loops?
- How do large programs manage many interacting Boolean conditions?
- How do professionals test conditional-heavy logic at scale?

I want to get better at writing decision logic without trial-and-error guessing and heavy AI use.