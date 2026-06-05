# Prompting Techniques

## Zero Shot

Prompt:
Explain data structures in python 

Response:
Python's main built-in data structures are **lists** (ordered, mutable), **tuples** (ordered, immutable), **sets** (unordered, unique elements), and **dictionaries** (key-value pairs). These containers organize data differently based on whether you need mutability, order preservation, uniqueness, or fast key-based lookup.


## Few Shot

Prompt:

Example 1:
Input: Red
Output: Colour

Example 2:
Input: Earth
Output: Planet

Input: White
Output:

Response:
Colour

## Chain of Thought

Prompt:
"A student has 3 exams in 5 days. Math (2 hours prep/day), Physics (3 hours/day), Chemistry (2 hours/day). 
How many total hours needed? Think step by step."

Response:
Step 1: Math needs 2 hours × 5 days = 10 hours
Step 2: Physics needs 3 hours × 5 days = 15 hours
Step 3: Chemistry needs 2 hours × 5 days = 10 hours
Step 4: Total = 10 + 15 + 10 = 35 hours
Answer: The student needs 35 total study hours.
