# Week 8 - Dictionaries, Tuples, Sets, and Choosing Data Structures

## What I learned this week

This week focused on choosing the right data structure for different problems and reviewing some important Python behaviors.

---

### 1. Copying vs Aliasing (Lists)

Two variables can reference the **same list** (aliasing):

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)       # [1, 2, 3, 4]
print(a is b)  # True
```

Both variables point to the **same object in memory**.

To create a copy instead:

```python
a = [1, 2, 3]
b = a[:]
b.append(4)

print(a)       # [1, 2, 3]
print(a is b)  # False
```

Key takeaway: copying vs referencing changes how mutations behave.

---

### 2. split() and strip() Review

Important string behavior:

```python
'a  b  c'.split()       # ['a', 'b', 'c']
'a  b  c'.split(' ')    # ['a', '', 'b', '', 'c']
```

- `split()` treats multiple spaces as **one separator**
- `split(' ')` splits on **each individual space**

Also important when reading files:

```python
word = line.strip()
```

`strip()` removes newline characters and whitespace so data is processed correctly.

---

### 3. Dictionaries (Key–Value Mapping)

A dictionary stores data as **key → value pairs**.

```python
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

eng2sp['two']   # 'dos'
'two' in eng2sp # True
len(eng2sp)     # 3
```

Keys must be **immutable** (strings, numbers, tuples).

---

### 4. Creating and Modifying Dictionaries

```python
prices = {}

prices['AAPL'] = 178.50
prices['GOOG'] = 141.80
prices['MSFT'] = 415.20

prices['AAPL'] = 182.30   # update
del prices['GOOG']        # delete
```

Dictionaries allow dynamic updates and fast lookup by key.

---

### 5. Looping Through Dictionaries

Different iteration patterns:

```python
for key in prices:
    print(key, prices[key])

for value in prices.values():
    print(value)

for key, value in prices.items():
    print(f"{key}: ${value}")
```

`items()` is especially useful because it supports **tuple unpacking**.

---

### 6. The Counting Pattern (Histogram)

Common pattern for counting frequency:

```python
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
```

Example:

```python
histogram("bookkeeper")
```

Counts how often each character appears.

This pattern applies to:
- word frequencies
- vote counting
- data analysis

---

### 7. Tuples

Tuples are **immutable sequences**.

```python
t = ('a', 'b', 'c')
t[0]      # 'a'
len(t)    # 3
```

Unlike lists, tuples **cannot be modified**.

Common uses:
- fixed data (coordinates)
- returning multiple values

Example:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3,1,4,1,5])
```

Tuple unpacking assigns both values at once.

---

### 8. zip() for Combining Sequences

```python
names = ['AAPL', 'GOOG', 'MSFT']
prices = [182.30, 141.80, 415.20]

for name, price in zip(names, prices):
    print(name, price)
```

Can also build dictionaries:

```python
stock_prices = dict(zip(names, prices))
```

---

### 9. Sets (Unique Collections)

Sets store **unique elements only**.

```python
fruits = {'apple', 'banana', 'apple'}
print(fruits)   # {'apple', 'banana'}
```

Good for removing duplicates:

```python
nums = [1,2,2,3,3]
unique = set(nums)
```

---

### 10. Set Operations

Sets support mathematical operations:

```python
a = {1,2,3,4}
b = {3,4,5,6}

a & b   # intersection
a | b   # union
a - b   # difference
```

Membership checks are very fast:

```python
3 in a
```

---

### 11. Choosing Data Structures

Each structure serves a different purpose:

- **list** → ordered collection with duplicates
- **tuple** → fixed data that shouldn't change
- **dict** → lookup by key
- **set** → unique items and fast membership testing

Choosing the right structure makes programs simpler and more efficient.

---

## Code I'm proud of

```python
def histogram(word):
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts
```

Why I like it:
- Uses the counting pattern
- Avoids KeyError using `get()`
- Compact but still readable

This feels like a useful real-world pattern.

---

## Challenges I faced

- Understanding when aliasing vs copying affects program behavior.
- Remembering that dictionary membership checks **keys**, not values.
- Keeping track of when to use lists vs tuples vs sets.

I worked through this by writing small test examples and printing outputs to confirm behavior.

---

## AI usage (if any)

- Used AI to clarify differences between lists, tuples, sets, and dictionaries.
- Asked for examples of when each structure is used in real programs.
- Compared AI explanations with lecture examples.

AI helped reinforce concepts but I rewrote examples myself.

---

## Questions going forward

- When does performance difference between lists, sets, and dicts really matter?
- How do large applications organize complex data structures?
- Are there common design patterns for combining dictionaries and lists?

I want to get better at selecting the right data structure before writing code.