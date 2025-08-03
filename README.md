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
