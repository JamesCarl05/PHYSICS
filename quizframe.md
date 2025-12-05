# 📋 QuizFrame — Usage & Integration Guide

> **Quick reference** to find, embed and style the `QuizFrame` from `quiz_frame.py` in the simulation.

---

## 📑 Quick Navigation
| Section | Purpose |
|---------|---------|
| [🎯 Quick identifiers](#-quick-identifiers) | Find what you need at a glance |
| [🚀 Minimal integration](#-minimal-integration) | Copy-paste to get started (30 seconds) |
| [💡 Real code examples](#-real-code-examples-with-output) | See actual output for each scenario |
| [📦 Class structure](#-quizframe-class-structure) | Understand the internals |
| [🎨 Design notes](#-design--integration-notes) | Best practices |
| [♿ Accessibility tips](#-accessibility--ux-tips) | User-friendly design |
| [✅ Checklist](#-checklist) | Deployment checklist |

---

## 🎯 Quick identifiers

```
Module:              quiz_frame.py
Class:               QuizFrame(ttk.Frame)
Constructor:         QuizFrame(master)
Difficulty Levels:   Easy  |  Medium  |  Hard
```

### Core Methods at a Glance
```
start_level()         → Begin quiz at current level
ask_question()        → Display Q + choices
select_choice()       → Process answer
finish_quiz()         → Show final score
update_score_label()  → Refresh score display
```

### Key Attributes
```
level_var        StringVar  → Current difficulty ("Easy", "Medium", "Hard")
score_label      ttk.Label  → Displays "Score: X/Y"
next_btn         ttk.Button → "Next Question" button
current_q        dict       → Current question data
```

---

## 🔍 Quick Search Commands

<details>
<summary><strong>PowerShell (Windows)</strong></summary>

```powershell
# Find QuizFrame references
Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" `
  -Pattern "QuizFrame" -SimpleMatch

# Find quiz_frame.py imports
Select-String -Path "c:\Users\user\Downloads\PHYSICS-main\**\*" `
  -Pattern "quiz_frame" -SimpleMatch
```
</details>

<details>
<summary><strong>Git Bash / WSL / macOS / Linux</strong></summary>

```bash
# Find QuizFrame references
grep -R --line-number "QuizFrame" "c:/Users/user/Downloads/PHYSICS-main"

# Find quiz_frame.py imports
grep -R --line-number "quiz_frame" "c:/Users/user/Downloads/PHYSICS-main"
```
</details>

---

## 🚀 Minimal Integration

### ⏱️ 30-Second Setup

```python
# filepath: main.py
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
root.title("Wave Simulation with Physics Quiz")

# Your existing simulation code...

quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)

root.mainloop()
```

### ✅ You now have:
- ✓ Level selector dropdown (`Easy`, `Medium`, `Hard`)
- ✓ "Start Level" button  
- ✓ Live score display (`Score: 0/0`)
- ✓ Question display area  
- ✓ Multiple choice buttons
- ✓ "Next Question" button

---

## 💡 Real Code Examples with Output

### Example 1️⃣: Start Easy Level

**What happens:**
1. User clicks "Start Level" button
2. First question loads
3. Score resets
4. Choice buttons appear

```python
# Initialize and start
quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)

# Default is "Easy" — user clicks "Start Level" button
quiz.start_level()
```

### 📺 Screen Output:

```
┌──────────────────────────────────────────────────────┐
│ Quiz Level: [Easy ▼]  [Start Level]  Score: 0/2      │
├──────────────────────────────────────────────────────┤
│ Q1: Which variable controls the height of the wave?  │
├──────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────┐  │
│ │ A. Frequency                                    │  │
│ └─────────────────────────────────────────────────┘  │
│ ┌─────────────────────────────────────────────────┐  │
│ │ B. Amplitude                                    │  │
│ └─────────────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────┤
│ [Next Question] (disabled)                           │
└──────────────────────────────────────────────────────┘
```

| Component | Value |
|-----------|-------|
| **Question** | `Q1: Which variable controls the height of the wave?` |
| **Choices** | 2 shuffled buttons (A. Frequency, B. Amplitude) |
| **Score** | `Score: 0/2` |
| **Next button** | 🔴 Disabled (wait for answer) |

---

### Example 2️⃣: User Clicks Correct Answer

**User clicks:** `B. Amplitude`

```python
# QuizFrame internally calls:
def select_choice(self, choice):
    # choice = ("Amplitude", "B", "Amplitude controls the height...")
    
    if choice[1] == self.current_q["correct"]:  # "B" == "B" ✓
        self.score += 1  # 0 → 1
        messagebox.showinfo("Correct", "Correct!\n\nAmplitude controls...")
    
    self.update_score_label()  # "Score: 1/2"
    self.next_btn.config(state="normal")  # Enable Next button
```

### 📺 Screen Output:

**Before click:**
```
Score: 0/2  |  Choice buttons: 🟢 Clickable  |  Next button: 🔴 Disabled
```

**After click:**
```
Score: 1/2  |  Choice buttons: 🔴 Disabled   |  Next button: 🟢 Enabled
```

**Messagebox:**
```
┌─────────────────────────────────┐
│  Correct                        │
├─────────────────────────────────┤
│  Correct!                       │
│                                 │
│  Amplitude controls the height  │
│  of the wave.                   │
├─────────────────────────────────┤
│              [ OK ]             │
└─────────────────────────────────┘
```

| State | Before | After |
|-------|--------|-------|
| **Score label** | `0/2` | `1/2` ✓ |
| **Choice buttons** | Clickable | Disabled |
| **Next button** | Disabled | **Enabled** ✓ |

---

### Example 3️⃣: User Clicks Wrong Answer

**User clicks:** `A. Frequency` (incorrect)

```python
def select_choice(self, choice):
    # choice = ("Frequency", "A", "Frequency changes...")
    
    if choice[1] == self.current_q["correct"]:  # "A" != "B" ✗
        # Score DOES NOT increment
        correct_answer = "Amplitude"
        correct_explanation = "Amplitude controls the height..."
        messagebox.showinfo("Incorrect", 
            f"Incorrect.\n\nCorrect answer: {correct_answer}\n\n{correct_explanation}")
    
    self.next_btn.config(state="normal")  # Enable Next button
```

### 📺 Screen Output:

**Messagebox:**
```
┌─────────────────────────────────────────────┐
│  Incorrect                                  │
├─────────────────────────────────────────────┤
│  Incorrect.                                 │
│                                             │
│  Correct answer: Amplitude                  │
│                                             │
│  Amplitude controls the height of the wave. │
├─────────────────────────────────────────────┤
│                  [ OK ]                     │
└─────────────────────────────────────────────┘
```

| State | Before | After |
|-------|--------|-------|
| **Score label** | `0/2` | `0/2` (no change) |
| **Choice buttons** | Clickable | Disabled |
| **Next button** | Disabled | **Enabled** ✓ |

---

### Example 4️⃣: Quiz Complete (Perfect Score)

**User finishes with 2/2 answers correct**

```python
def finish_quiz(self):
    if self.score == self.total:  # 2 == 2 ✓
        msg = "You finished the level!\nScore: 2/2\nExcellent — perfect score!"
    
    messagebox.showinfo("Level Complete", msg)
    self.score = 0
    self.total = 0
    self.update_score_label()
    self.clear_question_area()
```

### 📺 Screen Output:

**Messagebox:**
```
┌──────────────────────────────────┐
│  Level Complete                  │
├──────────────────────────────────┤
│  You finished the level!         │
│  Score: 2/2                      │
│                                  │
│  ⭐ Excellent — perfect score!   │
├──────────────────────────────────┤
│              [ OK ]              │
└──────────────────────────────────┘
```

**After clicking OK:**
```
┌──────────────────────────────────┐
│ Score: 0/0                       │
│ (Question area cleared)          │
│ [Next Question] (disabled)       │
└──────────────────────────────────┘
```

| Performance | Feedback |
|-------------|----------|
| **2/2 (100%)** | ⭐ Excellent — perfect score! |
| **1.4/2 (70%)** | 👍 Great job! |
| **0.8/2 (40%)** | 👌 Good effort! |
| **<0.8/2 (<40%)** | Try again! |

---

### Example 5️⃣: Change Difficulty Level

**User selects "Hard" from dropdown**

```python
# Automatically called when dropdown changes
def change_level(self, *_):
    self.score = 0
    self.total = 0
    self.q_index = 0
    self.update_score_label()  # "Score: 0/0"
    self.clear_question_area()  # Remove all widgets
    self.next_btn.config(state="disabled")
```

### 📺 Screen Output:

**Before change:**
```
Level: Easy   |   Score: 1/2   |   Q displayed   |   Choices visible
```

**After change:**
```
Level: Hard   |   Score: 0/0   |   Q cleared     |   Choices cleared
```

---

## 📦 QuizFrame Class Structure

### Initialization
```python
# filepath: quiz_frame.py - __init__ method

QuizFrame(master)
├── Load all questions from build_questions()
├── Set default level to "Easy"
├── Initialize score = 0
├── Initialize q_index = 0
└── Build UI widgets
    ├── Level dropdown
    ├── Start Level button
    ├── Score label
    ├── Question text box
    ├── Choice buttons frame
    └── Next Question button
```

### Question Data Format
```python
# Each question dictionary:
{
    "text": "Which variable controls the height of the wave?",

    "choices": [
        ("Frequency", "A", "Frequency changes how fast..."),
        ("Amplitude", "B", "Amplitude controls the height...")
    ],

    "correct": "B"  # Answer key
}

# Structure: (display_text, answer_key, explanation)
```

### Method Call Flow
```
User clicks "Start Level"
    ↓
start_level()
├── Reset: score=0, q_index=0
├── Load questions for level
├── Shuffle questions
└── Call ask_question()
    ↓
ask_question()
├── Display question text
├── Create choice buttons
└── Shuffle and display choices
    ↓
User clicks choice
    ↓
select_choice()
├── Compare with correct answer
├── Update score if correct
├── Show messagebox feedback
├── Enable "Next" button
└── If more questions → user clicks "Next"
    ↓
next_question()
├── Call ask_question() again
    OR
└── If no more questions → finish_quiz()
    ↓
finish_quiz()
├── Show final score & feedback
├── Reset all state
└── Clear question area
```

---

## 🎨 Design & integration notes

### ✅ Best Practices

```
DO:
✓ Keep quiz logic separate from simulation code
✓ Call quiz.start_level() from UI events only
✓ Let messagebox handle all user feedback
✓ Use level_var to read/set difficulty
✓ Match fonts with rest of app

DON'T:
✗ Mix physics calculations into quiz_frame.py
✗ Modify quiz questions at runtime without rebuilding
✗ Access internal _question attributes
✗ Hide the quiz from controls
```

### Common Customizations

**Change font size:**
```python
# In quiz_frame.py, find create_widgets() method
self.q_text = tk.Text(self, height=4, wrap="word",
                      font=("Segoe UI", 14))  # ← Change 11 to 14
```

**Adjust padding:**
```python
quiz.pack(fill="x", pady=12)  # Default is 8, increase for more space
```

**Add to existing frame:**
```python
# Instead of pack(), use grid() if your layout uses grid
quiz.grid(row=0, column=0, sticky="ew", pady=8)
```

### Layout Placement
```
┌─ Your Main Window ──────────────────┐
│                                     │
│  [ Other simulation controls ]      │
│                                     │
│  ┌─ QuizFrame ────────────────────┐ │
│  │ Quiz Level: [Easy ▼]  [Start]  │ │
│  │ Score: 0/0                     │ │
│  │                                │ │
│  │ Question text display area...  │ │
│  │                                │ │
│  │ [ Choice A ] [ Choice B ]      │ │
│  │                                │ │
│  │ [ Next Question ]              │ │
│  └────────────────────────────────┘ │
│                                     │
│  [ More simulation controls ]       │
│                                     │
└─────────────────────────────────────┘
```

---

## ♿ Accessibility & UX Tips

### Keyboard Navigation
```
Tab      → Move between buttons
Enter    → Click focused button
Shift+Tab → Move backwards
```

### Screen Reader Friendly
```
✓ All buttons have clear labels
✓ Score updates are reflected in text
✓ Messagebox titles are descriptive
✓ Questions are plain English (no abbreviations)
```

### Mobile / Touch Friendly
```
✓ Button padding allows easy tapping
✓ Choice buttons are full width
✓ Font is readable at any size
```

| Feature | Benefit | How |
|---------|---------|-----|
| **Shuffled choices** | Prevents pattern memorization | `random.shuffle(choices)` |
| **Instant feedback** | User knows if answer is right | Messagebox appears immediately |
| **Disabled buttons** | Prevents double-clicking | Buttons disabled until "Next" |
| **Clear labels** | No confusion on actions | "Correct!", "Incorrect." |
| **Explanations** | Learn from mistakes | Each choice has explanation text |

---

## ✅ Pre-Deployment Checklist

Run through before going live:

```
Code Integration:
☐ Import statement works: from quiz_frame import QuizFrame
☐ QuizFrame(root) instantiates without errors
☐ quiz.pack() displays in main window
☐ No file path errors

Functionality:
☐ "Start Level" button loads first question
☐ Choice buttons respond to clicks
☐ Score updates correctly after each answer
☐ "Next Question" button advances to next Q
☐ Level dropdown changes level correctly
☐ Final messagebox shows correct feedback

Visual:
☐ Fonts match app theme
☐ Padding looks consistent
☐ Colors look acceptable (or themed)
☐ Text is readable
☐ No widgets overlap

Bugs:
☐ No crash when starting level
☐ No crash when selecting answer
☐ No crash when changing level
☐ All messagebox buttons work
☐ Can complete full quiz without errors
```

---

## 🎓 Learning Path

**Beginner:** Just integrate the minimal example above  
**Intermediate:** Customize fonts and layout to match your UI  
**Advanced:** Add score persistence or connect to simulation events  

---

## 📞 Quick Help

| Need | Solution |
|------|----------|
| Add more questions | Edit `build_questions()` in `quiz_frame.py` |
| Change difficulty | Modify `self.levels` list in `__init__()` |
| Custom colors | Add `style.configure()` calls after `QuizFrame(root)` |
| Save scores | Call `quiz.score` and log to file after `finish_quiz()` |
| Disable level change | Hide the dropdown or disable `OptionMenu` widget |

---

**Last updated:** 2025  
**Status:** ✅ Ready for production  
**Version:** 1.0  

---
