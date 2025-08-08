# Time Calculator Project - By: David Kachroo

This public repository contains my solution for the **"Build a Time Calculator"** project from the **freeCodeCamp Scientific Computing with Python** certification.

## Project Overview
The `add_time` function calculates the new time after adding a specified duration to a given start time, with optional handling for the day of the week. The function returns the result in 12-hour format, including day transitions and proper formatting.

### Features:
- Accepts a **start time** in 12-hour AM/PM format (e.g., `"3:00 PM"`).
- Accepts a **duration** in `"hours:minutes"` format (e.g., `"2:45"`).
- Supports an **optional weekday** argument, case-insensitive (e.g., `"Monday"`).
- Calculates and returns the new time in correct 12-hour format.
- Handles time overflow across days:
  - Displays `(next day)` if it rolls over by one day.
  - Displays `(<n> days later)` if it rolls over by multiple days.
- Returns the new **weekday**, if provided in the input.
- Ensures consistent output formatting based on input scenarios.

### Example Usage:
```python
from time_calculator import add_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
