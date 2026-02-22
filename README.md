# 🎓 ICPC — Weighted GPA Calculator

> Compute a student's weighted GPA from letter grades and course tiers.

**Contest:** SoCal ICPC  
**Difficulty:** Easy  
**Status:** ✅ Solution provided

---

## 📋 Table of Contents

- [Problem Summary](#-problem-summary)
- [Input / Output](#-input--output)
- [How the Solution Works](#-how-the-solution-works)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)

---

## 📖 Problem Summary

Given N courses, each with a **letter grade** (A–D) and a **course tier** (1 or 2), calculate the student's final weighted GPA.

**Grade point values:**

| Letter | Points |
|--------|--------|
| A | 4 |
| B | 3 |
| C | 2 |
| D | 1 |

**Tier bonus** (only applies for grades A, B, or C):

| Tier | Bonus |
|------|-------|
| 1 | +0.05 |
| 2 | +0.025 |

**Final GPA = (sum of grade points / N) + sum of tier bonuses**

---

## 📥 Input / Output

**Input:**
```
N
grade_tier   (e.g. "A1", "B2", "C1", "D2")
...
```
Each grade is a 2-character string — no space between letter and tier.

**Output:** A single float — the final weighted GPA.

### Example

```
Input:          Output:
3               3.125
A1
B2
C1
```
*GPA = (4+3+2)/3 + (0.05+0.025+0.05) = 3.0 + 0.125 = 3.125*

---

## 💡 How the Solution Works

The solution reads each grade, maps the letter to its 4-point value, and adds the appropriate tier bonus if the grade is A, B, or C. It divides the total grade points by N and adds the accumulated tier bonuses at the end.

Input parsing relies on Python's ability to unpack a 2-character string directly into `letter, tier = list("A1")`.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+

### Running the Solution

```bash
python src/solution.py < tests/sample.txt
```

---

## 📂 Project Structure

```
src/
  solution.py     - Completed solution
docs/
  notes.md        - Walkthrough of the approach
tests/
  sample.txt      - Sample inputs
  expected.txt    - Expected outputs
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Think there's a bug or edge case? Open an issue!

## 📄 License

MIT — see [LICENSE](LICENSE).
