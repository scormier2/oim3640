# Week 6 - GitHub Copilot Workflow, Project Tracks, AI as a Tool

## What I learned this week

This week focused on working effectively with GitHub Copilot in VS Code and treating AI as part of a structured development workflow — not just a code generator.

---

### 1. Copilot Chat Modes

Copilot has three distinct modes:

- **Ask** → Explains code, answers questions (does NOT edit files)
- **Plan** → Designs implementation steps (blueprint phase)
- **Agent** → Executes tasks (creates/edits files, iterates on errors)

Workflow:
Ask → Plan → Agent

Analogy:
- Ask = Tutor  
- Plan = Architect  
- Agent = Contractor  

Key insight: Don’t skip straight to Agent. Understanding comes first.

---

### 2. Choosing a Development Track

We learned to choose a strategy based on our project state:

**Track A** – Have PROPOSAL.md, no code  
→ Critique → Plan → Agent  

**Track B** – Already have code  
→ Plan → Agent  
→ Compare AI-generated structure with your own  

Important addition:
"Do not overwrite any existing files."

Comparison becomes a learning tool:
- Did AI modularize better?
- Did it use more functions?
- Is its structure cleaner?

---

### 3. Improving Code with Agent Mode

We practiced using targeted prompts:

- Modularize large files
- Add input validation
- Simplify functions
- Write edge-case tests
- Expand features

Example validation thinking:
What happens if the user types nothing?
What happens if they type the wrong type?

This introduced defensive programming.

---

### 4. Track C – From Rough Idea to Proposal

If starting from scratch:

Use Ask mode:
"Ask me 5 questions to clarify my app idea."

Then:
Generate a draft `PROPOSAL.md`
Edit in your own words.
Commit.
Move to planning.

AI can structure thinking — but ownership comes from editing and refining.

---

### 5. Spelling Bee Project (Alternative Path)

We revisited search patterns and Boolean logic:

- `uses_only(word, letters)`
- `is_bee_valid(word, letters, center)`
- Iterate through a word list file
- Add scoring rules

This combined:
- Loops
- Conditionals
- Search pattern
- File iteration
- Modular function design

Extension thinking:
Build the solver OR reverse-engineer the full game.

---

### 6. for vs while (Reinforcement)

Use `for` when:
- Iteration count is known
- Looping over sequences

Use `while` when:
- Iteration depends on a condition
- Implementing retry/input validation
- Waiting for break condition

Understanding control flow is critical for interactive apps.

---

### 7. Critiquing and Planning with AI

We practiced prompts like:

"Read #file:PROPOSAL.md and critique it. Is anything vague? Is it feasible?"

Then:

"Create an implementation plan. Ask clarifying questions first."

This showed that AI is strongest when used as:
- Reviewer
- Planner
- Refactoring assistant

Not just a code writer.

---

## Code I'm proud of

```python
def is_bee_valid(word, letters, center):
    return (
        len(word) >= 4
        and center in word
        and uses_only(word, letters)
    )
```

Why:
- Clean composition of Boolean checks
- Combines multiple functions into readable logic
- Feels like real application-level validation

---

## Challenges I faced

- Resisting the urge to immediately use Agent mode.
- Knowing how detailed my prompts should be.
- Evaluating AI output instead of assuming it’s correct.
- Comparing my code to AI’s without defaulting to “AI must be better.”

I worked through this by reading every generated line and asking for simplifications when needed.

---

## AI usage (if any)

- Used Ask mode to clarify implementation decisions.
- Used Plan mode to structure file layout.
- Used Agent mode selectively for refactoring and validation.
- Compared AI-generated solutions with my own for learning purposes.
- Explicitly prompted AI not to overwrite files.

AI was used as a collaborator, not a replacement.

---

## Questions going forward

- How do professional developers structure prompts for large systems?
- When does AI speed up development vs create hidden complexity?
- How do I maintain originality while leveraging AI effectively?
- What does “clean architecture” look like at a larger scale?

This week felt less about syntax and more about workflow, tooling, and engineering judgment.