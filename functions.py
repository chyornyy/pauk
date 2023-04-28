def format_time(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    time_components = []
    if hours > 0:
        time_components.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        time_components.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        time_components.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    return ", ".join(time_components)