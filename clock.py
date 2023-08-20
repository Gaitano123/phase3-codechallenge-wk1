def clock_converter(hour, minute, period):
    if period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12
    return f"{hour:02d}{minute:02d}"  