def calculate_minutes(time_string):
    total_minutes = 0
    for time_value in time_string.split(','):
        time_value = time_value.strip()
        for part in time_value.split(' '):
            if 'h' in part:
                total_minutes += int(part.replace('h', '')) * 60
            elif 'm' in part:
                total_minutes += int(part.replace('m', ''))
            elif 's' in part:
                total_minutes += int(part.replace('s', '')) // 60
    return total_minutes


result = calculate_minutes('1h 45m,360s,25m,30m 120s,2h 60s')
print(result)