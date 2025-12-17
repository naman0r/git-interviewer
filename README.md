# Git Interviewer 🎤  
A pre-commit hook that *interviews you* about your code before letting you commit.

Git Interviewer transforms everyday commits into lightweight technical interviews.  
Before each commit, it analyzes your staged changes, generates interview-style questions, and requires a meaningful answer.  

This forces deeper understanding, intentional commits, and better engineering discipline — but in a fun way.

View here: https://pypi.org/project/git-interviewer/1.0.0/
---

## Why Git Interviewer?

Most developers commit code too quickly:

- without thinking about design decisions  
- without explaining intent  
- without validating risks  
- without reflecting on tradeoffs  

**Git Interviewer slows you down — in a good way.**  
It makes you articulate *why* you wrote the code, not just *what* you wrote.

Think of it as having a senior engineer inside your terminal.

---

# Features I want to build

### Interview Modes (Personas)
Choose the personality you want challenging your commit:

| Mode      | Description |
|-----------|-------------|
| `nice`    | Supportive engineer who wants clarity and understanding. |
| `grumpy`  | Tired senior dev who has seen too much. Very picky. |
| `systems` | Asks about architecture, scaling, risk, tradeoffs. |
| `founder` | Focuses on product impact and iteration speed. |



If you build this, your repo will be **dramatically** higher quality, and everyone who installs it will become a better engineer.

Feel free to open issues, request new personas, or contribute new interview logic!



## See Git-Interviewer in action! 

<img  height="200" alt="image" src="https://github.com/user-attachments/assets/c6d53265-4c43-4507-bcd6-7077164b085e" />
Graceful commit allowed, no friction
<br/>
<img height="200" alt="image" src="https://github.com/user-attachments/assets/0b9eaf2b-2199-41d2-9b36-907af9d633a6" />

Asks a question ^
<br/>
<img  height="200" alt="image" src="https://github.com/user-attachments/assets/267fc263-39fa-4e8b-86c2-19f932af2ae5" />
Answer too short -> graceful termination, commit not allowed.

<img width="1906" height="1254" alt="image" src="https://github.com/user-attachments/assets/496e9491-e087-4bad-a2f7-2e1d1dedec16" />








