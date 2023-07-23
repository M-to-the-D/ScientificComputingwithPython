def add_time(start, duration, day=None):
    # Convert start time to minutes since midnight
    start_time, meridiem = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_minutes = start_hour * 60 + start_minute
    if meridiem == "PM":
        start_minutes += 12 * 60

    # Convert duration time to minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    duration_minutes = duration_hour * 60 + duration_minute

    # Calculate the total minutes after adding the duration
    total_minutes = start_minutes + duration_minutes

    # Calculate the new time and meridiem
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    new_meridiem = "AM" if new_hour < 12 else "PM"
    if new_hour >= 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12

    # Calculate the number of days later
    days_later = total_minutes // (24 * 60)

    # Determine the new day if provided
    new_day = None
    if day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = days.index(day.lower().capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days[new_day_index]

    # Prepare the final output string
    new_time = f"{new_hour}:{str(new_minute).rjust(2, '0')} {new_meridiem}"
    if day:
        new_time += f", {new_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time