def add_time(start, duration, starting_day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start to 24-hour format
    if period == 'PM':
        start_hour += 12 if start_hour != 12 else 0
    else:
        start_hour = 0 if start_hour == 12 else start_hour

    # Add duration
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

    # Build result string
    new_time = f"{final_hour}:{final_minute:02d} {final_period}"

    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time