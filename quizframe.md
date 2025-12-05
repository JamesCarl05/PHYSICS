# 📋 QuizFrame — Usage & Integration Guide

> **Quick reference** to find, embed and style the `QuizFrame` from `quiz_frame.py` in the simulation.

---

## 📑 Contents
- [Quick identifiers](#quick-identifiers)
- [Quick search](#quick-search)
- [Minimal integration](#minimal-integration-paste-into-main-gui-file)
- [Real code examples with output](#real-code-examples-with-output)
- [QuizFrame class structure](#quizframe-class-structure)
- [Design & integration notes](#design--integration-notes)
- [Accessibility & UX tips](#accessibility--ux-tips)
- [Checklist](#checklist)

---

## 🎯 Quick identifiers

| Item | Value |
|------|-------|
| **Module** | `quiz_frame.py` |
| **Class** | `QuizFrame(ttk.Frame)` |
| **Constructor** | `QuizFrame(master)` |
| **Key methods** | `start_level()`, `ask_question()`, `select_choice()`, `finish_quiz()`, `update_score_label()` |
| **Key attributes** | `level_var` (StringVar), `score_label`, `next_btn`, `questions_by_level` |
| **Difficulty levels** | `"Easy"`, `"Medium"`, `"Hard"` |

---

## 🔍 Quick search

### PowerShell
```powershell
# Find QuizFrame class
Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "QuizFrame" -SimpleMatch

# Find quiz_frame module
Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" -Pattern "quiz_frame" -SimpleMatch
```

### Cross-platform (git bash / WSL / macOS / Linux)
```bash
# Find QuizFrame class
grep -R --line-number "QuizFrame" "c:/Users/user/Downloads/PHYSICS-main" || true

# Find quiz_frame module
grep -R --line-number "quiz_frame" "c:/Users/user/Downloads/PHYSICS-main" || true
```

---

## 🚀 Minimal integration (paste into main GUI file)

> **For the quickest setup**, copy this snippet into your main GUI file.

```python
# filepath: main.py (or your main GUI file)
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
root.title("Wave Simulation with Physics Quiz")

# ... existing simulation UI setup ...

quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)

root.mainloop()
```

✅ **Result:** QuizFrame appears as a control panel with:
- Level selector dropdown (`Easy`, `Medium`, `Hard`)
- "Start Level" button
- Score display label
- Question display area
- Multiple choice buttons
- "Next Question" button

---

## 💡 Real Code Examples with Output

### Example 1: Initialize and Start Easy Level

**What the code does:** Create QuizFrame and start the Easy difficulty level.

```python
# filepath: main.py
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)

# Option 1: User clicks "Start Level" button (default is "Easy")
# quiz.start_level()  # Starts "Easy" because level_var defaults to "Easy"

# Option 2: Explicitly set and start
quiz.level_var.set("Easy")
quiz.start_level()
```

**📊 What happens on screen:**

| Element | State |
|---------|-------|
| Question text box | Shows `"Q1: Which variable controls the height of the wave?"` |
| Choice buttons | Displays 2 shuffled choices: `"A. Frequency"` and `"B. Amplitude"` |
| Score label | Shows `"Score: 0/2"` (2 questions in Easy level) |
| Next button | **Disabled** (grayed out) until answer selected |

**Console / Debug Output:**
```
Level: Easy
Questions loaded: 2
Total score: 0/2
```

---

### Example 2: User Selects Answer (Correct)

**What the code does:** User clicks choice button. If correct, score increments and feedback displays.

```python
# filepath: quiz_frame.py - select_choice() method
def select_choice(self, choice):
    for child in self.choice_frame.winfo_children():
        child.config(state="disabled")  # Disable all buttons

    clicked = choice[1]  # e.g., "B" (the answer key)
    correct = self.current_q["correct"]  # e.g., "B"

    if clicked == correct:
        self.score += 1  # Score increases from 0 to 1
        messagebox.showinfo("Correct", "Correct!\n\n" + choice[2])
        # choice[2] is explanation: "Amplitude controls the height of the wave."
    else:
        # Show incorrect feedback with correct answer
        correct_text = next(c[0] for c in self.current_q["choices"] if c[1] == correct)
        correct_expl = next(c[2] for c in self.current_q["choices"] if c[1] == correct)
        messagebox.showinfo("Incorrect",
                            f"Incorrect.\n\nCorrect answer: {correct_text}\n\n{correct_expl}")

    self.q_index += 1  # Move to next question
    self.update_score_label()  # Update label: "Score: 1/2"
    self.next_btn.config(state="normal")  # Enable "Next" button
```

**📊 Output when user clicks "B. Amplitude" (correct):**

| UI Element | Before | After |
|-----------|--------|-------|
| Score label | `Score: 0/2` | `Score: 1/2` |
| Choice buttons | Clickable | Disabled (grayed out) |
| Next button | Disabled | **Enabled** (clickable) |
| Messagebox | — | Pops up: `"Correct!\nAmplitude controls the height of the wave."` |

**User action:** Click "OK" on messagebox, then click "Next Question" button.

---

### Example 3: User Selects Answer (Incorrect)

**What the code does:** User clicks wrong answer. Score stays same, correct answer shown.

```python
# filepath: quiz_frame.py - select_choice() method (incorrect branch)
if clicked == correct:
    self.score += 1
else:
    # User selected "A. Frequency" but correct is "B. Amplitude"
    correct_text = next(c[0] for c in self.current_q["choices"] if c[1] == correct)
    # correct_text = "Amplitude"
    correct_expl = next(c[2] for c in self.current_q["choices"] if c[1] == correct)
    # correct_expl = "Amplitude controls the height of the wave."
    messagebox.showinfo("Incorrect",
                        f"Incorrect.\n\nCorrect answer: {correct_text}\n\n{correct_expl}")
```

**📊 Output when user clicks "A. Frequency" (incorrect):**

| UI Element | Before | After |
|-----------|--------|-------|
| Score label | `Score: 0/2` | `Score: 0/2` (no change) |
| Choice buttons | Clickable | Disabled |
| Next button | Disabled | **Enabled** |
| Messagebox | — | Pops up: `"Incorrect.\nCorrect answer: Amplitude\nAmplitude controls the height of the wave."` |

---

### Example 4: Complete Quiz & Finish

**What the code does:** User answers all questions. Quiz finishes and shows performance feedback.

```python
# filepath: quiz_frame.py - finish_quiz() method
def finish_quiz(self):
    msg = f"You finished the level!\nScore: {self.score}/{self.total}"
    # msg = "You finished the level!\nScore: 2/2"

    if self.score == self.total:
        msg += "\nExcellent — perfect score!"
    elif self.score >= self.total * 0.7:
        msg += "\nGreat job!"
    elif self.score >= self.total * 0.4:
        msg += "\nGood effort!"
    else:
        msg += "\nTry again!"

    messagebox.showinfo("Level Complete", msg)
    # Resets quiz state
    self.score = 0
    self.total = 0
    self.q_index = 0
    self.update_score_label()
    self.clear_question_area()
    self.next_btn.config(state="disabled")
```

**📊 Output when user finishes with 2/2 score:**

**Messagebox displays:**
```
Level Complete

You finished the level!
Score: 2/2

Excellent — perfect score!
```

**After clicking OK:**

| UI Element | State |
|-----------|-------|
| Score label | Reset to `Score: 0/0` |
| Question text | Cleared (empty) |
| Choice buttons | All removed |
| Next button | Disabled |

---

### Example 5: Change Level & Clear Quiz

**What the code does:** User changes difficulty level. Previous progress clears automatically.

```python
# filepath: quiz_frame.py - change_level() method
def change_level(self, *_):
    self.score = 0  # Reset score
    self.total = 0
    self.q_index = 0
    self.update_score_label()  # Label: "Score: 0/0"
    self.clear_question_area()  # Remove all question/choice widgets
    self.next_btn.config(state="disabled")  # Disable Next button
```

**User action sequence:**
1. User selects `"Medium"` from dropdown
2. `change_level()` executes automatically (callback)

**📊 Output:**

| Element | After change_level() |
|---------|----------------------|
| Score label | `Score: 0/0` |
| Question text | Cleared |
| Choice buttons | All removed |
| Next button | Disabled |
| Status | Ready for user to click "Start Level" |

---

## 📦 QuizFrame Class Structure

### Constructor
```python
# filepath: quiz_frame.py
def __init__(self, master):
    super().__init__(master)
    self.master = master
    self.levels = ["Easy", "Medium", "Hard"]
    self.questions_by_level = self.build_questions()  # Load all Q&A
    self.level_var = tk.StringVar(value=self.levels[0])  # Default: "Easy"
    self.current_q = None  # Current question dict
    self.q_index = 0  # Current question index
    self.score = 0  # Current score
    self.total = 0  # Total questions in level
    self.create_widgets()  # Build UI
```

### Question Data Structure
```python
# filepath: quiz_frame.py - sample from build_questions()
{
    "Easy": [
        {
            "text": "Which variable controls the height of the wave?",
            "choices": [
                ("Frequency", "A", "Frequency changes how fast the wave oscillates."),
                ("Amplitude", "B", "Amplitude controls the height of the wave.")
            ],
            "correct": "B"
        },
        # ... more questions
    ],
    "Medium": [ ... ],
    "Hard": [ ... ]
}
```

### Main Methods

| Method | Purpose | Called by |
|--------|---------|-----------|
| `start_level()` | Load questions, reset score, show first Q | "Start Level" button |
| `ask_question()` | Display current question and choices | `start_level()`, `next_question()` |
| `select_choice(choice)` | Process answer, update score, show feedback | Choice buttons |
| `next_question()` | Move to next Q or finish quiz | "Next Question" button |
| `finish_quiz()` | Show final score, reset state | `next_question()` when all Q answered |
| `change_level(...)` | Reset quiz when level changes | Level dropdown |
| `update_score_label()` | Refresh score display | `select_choice()`, `change_level()` |
| `clear_question_area()` | Remove Q text and choice buttons | `ask_question()`, `change_level()` |

---

## 🎨 Design & integration notes

### Keep concerns separated
- ❌ **Don't:** Mix physics simulation logic into `quiz_frame.py`
- ✅ **Do:** Call `QuizFrame` methods from your main simulation UI

### Minimal API usage
```python
# Three essential operations:
quiz.start_level()                    # Begin quiz at current level
quiz.level_var.set("Hard")            # Change difficulty
quiz.update_score_label()             # Refresh score display (automatic in most cases)
```

### Placement & styling
| Aspect | Recommendation |
|--------|-----------------|
| **Location** | Place near simulation controls (sliders, buttons) for discoverability |
| **Fonts** | Uses `"Segoe UI", 11` for questions — match this or adjust theme-wide |
| **Padding** | Question box uses `pady=5`, control buttons use `pady=3` |
| **Colors** | Inherits from Tkinter ttk theme (no hardcoded colors) |
| **Height** | Frame height set to `180px` — adjust if content overflows |

---

## ♿ Accessibility & UX tips

| Tip | Benefit | Implementation |
|-----|---------|-----------------|
| **Short messagebox text** | Users focus on key info | Feedback is 1–2 lines max |
| **Clear button labels** | No confusion on next action | "Start Level", "Next Question" |
| **Keyboard navigation** | Tab through buttons, Enter to select | Tkinter ttk handles this by default |
| **Shuffle choices** | Prevents answer pattern recognition | `random.shuffle(choices)` in `ask_question()` |
| **Disable buttons after answer** | Prevents double-submission | `child.config(state="disabled")` in `select_choice()` |
| **Explanations in feedback** | Users learn from mistakes | Each choice includes `choice[2]` explanation |

---

## ✅ Checklist

Before deploying your quiz integration:

- [ ] ✅ Import `from quiz_frame import QuizFrame` works (no path errors)
- [ ] ✅ `quiz = QuizFrame(root)` instantiates without errors
- [ ] ✅ `quiz.pack()` displays the frame in your main window
- [ ] ✅ "Start Level" button loads first question
- [ ] ✅ Choice buttons work and show feedback
- [ ] ✅ Score updates correctly after each answer
- [ ] ✅ "Next Question" button proceeds to next Q
- [ ] ✅ Level dropdown changes clear previous progress
- [ ] ✅ Final messagebox shows correct performance message
- [ ] ✅ Visual styling matches your app theme

---

## 📞 Need more help?

I can:
- 🔧 **Modify `quiz_frame.py`** to add new questions or difficulty levels
- 📊 **Add score persistence** (save quiz results to file)
- 🎨 **Customize colors/fonts** to match your simulation UI
- 🔗 **Connect quiz events** to simulation (e.g., unlock features on perfect score)

---

**Last updated:** 2025 | **Status:** Ready for integration | **QuizFrame version:** 1.0
