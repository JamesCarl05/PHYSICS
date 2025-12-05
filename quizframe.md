# 📋 QuizFrame — Usage & Integration Guide

> **Quick reference** to find, embed and style the `QuizFrame` from `quiz_frame.py` in the simulation.

---

## 📑 Contents
- [Quick identifiers](#quick-identifiers)
- [Quick search](#quick-search)
- [Minimal integration](#minimal-integration-paste-into-main-gui-file)
- [Code examples with output explanations](#code-examples-with-output-explanations)
- [Design & integration notes](#design--integration-notes)
- [Accessibility & UX tips](#accessibility--ux-tips)
- [Checklist](#checklist)

---

## 🎯 Quick identifiers

| Item | Value |
|------|-------|
| **Module** | `quiz_frame.py` |
| **Class** | `QuizFrame` |
| **Key methods** | `start_level()`, `ask_question()`, `select_choice()`, `finish_quiz()` |
| **Key attributes** | `update_score_label()`, `score_label`, `next_btn`, `level_var` |

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
# filepath: main_gui.py
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

✅ **Result:** QuizFrame appears as a horizontal panel in your GUI.

---

## 💡 Code Examples with Output Explanations

### Example 1: Starting a Quiz at a Specific Level

**What it does:** Initialize the quiz and load questions for a chosen difficulty.

```python
# filepath: integration_example.py
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)

# Set difficulty and start
quiz.level_var.set("Medium")  # Options: "Easy", "Medium", "Hard"
quiz.start_level()             # Load questions for this level
```

**📊 Expected Output:**
| Element | Change |
|---------|--------|
| Quiz frame | First question appears on screen |
| Score label | Resets to `Score: 0/5` |
| Choice buttons | 4 answer options displayed |
| Next button | Enabled (clickable) |

---

### Example 2: Responding to User Answer Selection

**What it does:** Process user's answer choice and update score.

```python
# filepath: integration_example.py
from tkinter import Tk, messagebox
from quiz_frame import QuizFrame

root = Tk()
quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)
quiz.start_level()

# Simulate user clicking the first choice button (index 0)
quiz.select_choice(0)
```

**📊 Expected Output:**

| Scenario | Feedback | Score Update |
|----------|----------|--------------|
| ✅ **Correct answer** | Messagebox: `"Correct!"` | Increments (e.g., `1/5` → `2/5`) |
| ❌ **Incorrect answer** | Messagebox: `"Incorrect. Answer: [X]"` | No change |
| ⏭️ **After feedback** | Messagebox closes | Next button becomes active |

---

### Example 3: Monitoring Score Changes Programmatically

**What it does:** Access score data and sync it with external logging or tracking.

```python
# filepath: integration_example.py
from tkinter import Tk
from quiz_frame import QuizFrame

root = Tk()
quiz = QuizFrame(root)
quiz.pack(fill="x", pady=8)
quiz.start_level()

# After user completes a question:
current_score_text = quiz.score_label.cget("text")  # Retrieve display
print(f"Quiz Status: {current_score_text}")  # Output: "Score: 2/5"

# Manually refresh (useful after programmatic updates)
quiz.update_score_label()
```

**📊 Expected Output:**

```
Console Output:
Quiz Status: Score: 2/5

UI Update:
- Score label on screen refreshes
- Ready for next question
```

> **💼 Use case:** Log quiz progress to a file or sync with simulation state tracking.

---

## 🎨 Design & integration notes

### Keep concerns separated
- ❌ **Don't:** Mix simulation physics logic into `quiz_frame.py`
- ✅ **Do:** Call `QuizFrame` methods from your main UI, keep responsibilities clean

### Minimal API usage
```python
# Three main operations:
quiz.start_level()                    # Begin quiz at current level
quiz.level_var.set("Easy")            # Change difficulty
quiz.update_score_label()             # Refresh score display
```

### Placement & styling
| Aspect | Recommendation |
|--------|-----------------|
| **Location** | Near simulation controls (sliders, buttons) for discoverability |
| **Fonts** | Match app theme (e.g., same font family/size as other panels) |
| **Padding** | Use `pady=8` or consistent spacing with surrounding widgets |
| **Colors** | Inherit from Tkinter theme or customize to match UI palette |

---

## ♿ Accessibility & UX tips

| Tip | Benefit |
|-----|---------|
| **Keep messages short** | Users focus on key info (e.g., "Correct!" vs. long explanations) |
| **Enable keyboard navigation** | Users can tab through buttons and select with Enter |
| **Label buttons clearly** | Avoid generic names like "Button 1"; use "Easy", "Medium", etc. |
| **For long explanations** | Open a small `Toplevel` window with formatted text instead of messagebox |
| **Test with screen readers** | Ensure labels and button text are meaningful |

---

## ✅ Checklist

Before deploying your quiz integration:

- [ ] ✅ `QuizFrame` import found in project (use Quick search section)
- [ ] ✅ `QuizFrame(...)` instantiated and added to layout
- [ ] ✅ Simulation event handlers call or update quiz appropriately
- [ ] ✅ No import/path errors when running
- [ ] ✅ Visual alignment and fonts consistent with app theme
- [ ] ✅ Score updates visible and responsive
- [ ] ✅ Keyboard navigation works (Tab, Enter)

---

## 📞 Need more help?

I can:
- 🔎 **Scan the repo** and list files that reference `QuizFrame`
- 🔧 **Modify `quiz_frame.py`** to accept callbacks/shared variables (confirm before changes)
- 📖 **Add more examples** for specific integration scenarios

---

**Last updated:** 2025 | **Status:** Ready for integration
