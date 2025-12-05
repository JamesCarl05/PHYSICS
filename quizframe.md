# QuizFrame — Usage & Integration Guide

## Purpose
- Quick reference for where and how to use the `QuizFrame` (from `quiz_frame.py`) in the simulation.
- Fast search tips, a minimal integration snippet, and design notes to keep integration clean and maintainable.

## Table of Contents
- Purpose
- Quick identifiers to search for
- Search commands
- Minimal integration example
- Design & readability guidelines
- Checklist

## Quick identifiers to search
- Module: `quiz_frame.py`
- Class: `QuizFrame`
- Key methods and attributes: `start_level`, `ask_question`, `select_choice`, `finish_quiz`, `update_score_label`, `score_label`, `next_btn`, `level_var`

## Search commands
- Windows PowerShell:
  - Search for the class:  
    `Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "QuizFrame" -SimpleMatch`
  - Search for the file name:  
    `Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "quiz_frame" -SimpleMatch`

- Cross-platform (Git Bash / WSL / macOS / Linux):
  - grep for the class:  
    `grep -R --line-number "QuizFrame" "c:/Users/user/Downloads/PHYSICS-main" || true`
  - grep for the module:  
    `grep -R --line-number "quiz_frame" "c:/Users/user/Downloads/PHYSICS-main" || true`

## Minimal integration example
- Paste into your main GUI file (e.g., `main.py` or `app.py`). This shows the minimal required steps to embed the quiz into an existing Tkinter app.

```python
# Example (insert into your main GUI file)
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
root.title("Simulation with Quiz")

# ... existing simulation UI setup ...

quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)   # Use pack/grid/place consistent with your layout

# Optionally start a default level automatically:
# quiz.start_level()

root.mainloop()
```

## Design & readability guidelines
- Keep QuizFrame decoupled:
  - Avoid embedding simulation logic directly in `quiz_frame.py`. Instead, call QuizFrame methods from the simulation UI.
  - Use shared Tkinter variables (e.g., IntVar/DoubleVar) or pass callbacks if the quiz needs simulation state.
- Small API suggestions (no file changes here, just integration tips):
  - Use `quiz.start_level()` to begin.
  - Use `quiz.level_var.set("Easy")` to change the level programmatically.
  - Use `quiz.update_score_label()` after external score changes.
- UI layout:
  - Place QuizFrame near controls it references (e.g., sliders) to improve discoverability.
  - Keep margins and font sizes consistent with the rest of the app.
- Accessibility:
  - Ensure messagebox text is concise; use short sentences.
  - Make sure buttons are keyboard-focusable and have clear labels.

## Checklist for integration
- [ ] Found files that import `QuizFrame` (search results).
- [ ] `QuizFrame(...)` is instantiated and added to the window layout.
- [ ] Simulation event handlers call or update QuizFrame where needed.
- [ ] No import errors and correct module paths.
- [ ] Visual alignment and font sizes consistent with the app.

If you want:
- I can scan the repository and return a list of exact files that reference `QuizFrame` (requires reading other files).
- Or I can update `quiz_frame.py` to accept shared variables or callbacks (confirm before I change code).
