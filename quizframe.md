# QuizFrame — Usage & Integration Guide

> Quick reference to find, embed and style the `QuizFrame` from `quiz_frame.py` in the simulation.

---

## Contents
- Quick identifiers
- Quick search
- Minimal integration (copy-paste)
- Design & integration notes
- Accessibility & UX tips
- Checklist

---

## Quick identifiers
- Module: `quiz_frame.py`  
- Class: `QuizFrame`  
- Common methods/attributes: `start_level`, `ask_question`, `select_choice`, `finish_quiz`, `update_score_label`, `score_label`, `next_btn`, `level_var`

---

## Quick search
PowerShell
- Find class:  
  `Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "QuizFrame" -SimpleMatch`
- Find module:  
  `Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "quiz_frame" -SimpleMatch`

Cross-platform (git bash / WSL / macOS / Linux)
- Find class:  
  `grep -R --line-number "QuizFrame" "c:/Users/user/Downloads/PHYSICS-main" || true`
- Find module:  
  `grep -R --line-number "quiz_frame" "c:/Users/user/Downloads/PHYSICS-main" || true`

---

## Minimal integration (paste into main GUI file)
```python
# Example (insert into your main GUI file)
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
root.title("Simulation with Quiz")

# ... existing simulation UI setup ...

quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)   # adjust to your layout style

# Optional: start default level
# quiz.start_level()

root.mainloop()
```

---

## Design & integration notes
- Keep concerns separated:
  - Do not mix simulation logic into `quiz_frame.py`. Call its methods from the simulation UI instead.
  - Prefer callbacks or shared Tk variables (IntVar/DoubleVar) to share state.
- Minimal API usage:
  - Start quiz: `quiz.start_level()`
  - Change level: `quiz.level_var.set("Easy")`
  - Refresh score display: `quiz.update_score_label()`
- Placement:
  - Place the QuizFrame near relevant simulation controls (sliders) for discoverability.
  - Match font sizes and padding with the app's theme.

---

## Accessibility & UX tips
- Keep messagebox messages short and actionable.
- Ensure buttons are keyboard-focusable and labeled clearly.
- If explanations are long, consider opening a small Toplevel with formatted text instead of a messagebox.

---

## Checklist
- [ ] `QuizFrame` import found in project (search).
- [ ] `QuizFrame(...)` is instantiated and added to the UI layout.
- [ ] Simulation event handlers call or update the quiz where appropriate.
- [ ] No import/path errors.
- [ ] Visual alignment and fonts are consistent.

---

If you want, I can:
- Scan the repo and list files that reference `QuizFrame` (requires reading other files), or
- Modify `quiz_frame.py` to accept callbacks/shared variables (confirm before changes).
