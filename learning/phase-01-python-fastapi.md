# Phase 1 — Python Fundamentals with FastAPI

## Learning Objectives

By the end of this phase you will be able to:

- Set up a Python project with a virtual environment
- Write and run Python scripts confidently
- Use Python's core data types and collections correctly
- Write functions, control flow, and comprehensions
- Build a small FastAPI application with CRUD-style routes
- Validate data with Pydantic models
- Choose correct HTTP methods and status codes

## Lesson Sequence

| # | Lesson | Status |
|---|--------|--------|
| 0 | Project setup, virtual environments, pip | ✅ |
| 1 | Variables, data types, print, f-strings | ✅ |
| 2 | Type conversion, input/output, operators | ✅ |
| 3 | Conditionals (if / elif / else) | ✅ |
| 4 | Loops (for / while), break, continue | ✅ |
| 5 | Collections I — lists & tuples | ✅ |
| 6 | Collections II — dicts & sets | ✅ |
| 7 | String manipulation | ✅ |
| 8 | Functions, parameters, return, defaults | ✅ |
| 9 | Scope — local vs global | ✅ |
| 10 | Comprehensions & lambdas | ✅ |
| 11 | Modules & imports | ✅ |
| 12 | First FastAPI app — routes & HTTP methods | ✅ |
| 13 | Path & query parameters | ✅ |
| 14 | Request bodies & Pydantic models | ✅ |
| 15 | HTTP verbs, status codes & HTTPException | ✅ |
| 16 | Phase 1 capstone — in-memory product API | ✅ |

## Notes

- FastAPI is introduced early, but only after the Python concept
  underneath it has been explained.
- All Phase 1 data lives in memory (lists/dicts). No database yet.
- Every lesson ends with an assessment before moving on.

## Common Mistakes to Watch For

- Running code outside the virtual environment (`ModuleNotFoundError`)
- Forgetting to activate the venv in a new terminal
- Confusing `=` (assignment) with `==` (comparison)
- Off-by-one errors in loops (`range` end is exclusive)
- Mutating a list while iterating over it
- Forgetting `self` is not a thing yet — plain functions first
- Returning data vs printing data inside API functions

## Phase 1 Completion Checklist

- [ ] Can create/activate a venv and install packages
- [ ] Can explain mutable vs immutable types
- [ ] Can write CRUD functions over a list of dicts
- [ ] Can explain what `@app.get` does and what a decorator is (informally)
- [ ] Can define a Pydantic model and explain why validation matters
- [ ] Can choose between GET/POST/PUT/PATCH/DELETE correctly
- [ ] Capstone API runs under uvicorn and passes manual tests in /docs
