# Week 2 Learning Log

## What did I learn in class this week?

This week shifted from course setup to actual programming foundations, focusing on *how to think* rather than just how to type code.

---

### Environment Setup & Debugging

We learned how to fix the Conda warning in VS Code (Windows). If red text like `conda activate base` appears before output, the code still runs correctly — but it’s an environment configuration issue.

Two fixes:

- Run `conda init powershell` in Anaconda Prompt, then restart VS Code (recommended).
- Change VS Code Terminal default profile to Command Prompt.

This reinforced that development environments matter. Not all “red text” means your code is broken — sometimes it’s configuration.

---

### Programming as a Way of Thinking (Chapter 1)

The key takeaway: programming = structured problem solving.

Core ideas:
- Break big problems into smaller steps.
- Python is an interpreter that executes instructions line by line.
- Errors (SyntaxError, NameError, TypeError) are part of the learning process.
- Experimentation is encouraged — test, observe, iterate.

Instead of fearing errors, we’re learning to treat them as feedback.

---

### Variables & Statements (Chapter 2)

We moved into foundational building blocks:

#### Values and Types
Understanding different kinds of data (strings, integers, floats, etc.) and how Python classifies them.

#### Variables
A variable stores a value using a name:

python
message = "Hello, World!"
n = 42
pi = 3.14159