# 📝 Notes — Weighted GPA Calculator

## Problem Breakdown

Read N courses. Each course has a letter grade (A/B/C/D) and a tier (1 or 2).
Compute: `(total_points / N) + total_tier_bonus`

## Parsing the Input

Each grade is given as a 2-character string like `"A1"` or `"B2"`.
The code unpacks it directly:
```python
letter, tier = list(input().strip())
```
This gives `letter = "A"` and `tier = "1"` (as a string), then `tier = int(tier)`.

## Tier Bonus Logic

Tier bonuses **only apply** for grades A, B, or C. Grade D courses carry no bonus regardless of tier.
This models a system where poor performance doesn't get rewarded by course difficulty.

## Output

The output is a raw Python float (e.g. `3.125`). No special formatting is applied — this is exactly what `print(float)` gives.

## Sample Trace

Input: 3 courses → A1, B2, C1

- A → 4 points, Tier 1 → +0.05
- B → 3 points, Tier 2 → +0.025
- C → 2 points, Tier 1 → +0.05

Total points = 9, N = 3 → unweighted = 3.0
Total bonus = 0.125
Final GPA = 3.0 + 0.125 = **3.125** ✓
