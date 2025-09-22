def add_time(start, duration, day=None):

    # take duration on hour and minute
    hour, minute = duration.split(':')
    duration_h = int(hour)
    duration_m = int(minute)

    # day list
    days = ['saturday', 'sunday', 
            'monday', 'tuesday', 
            'wednesday', 'thursday', 
            'friday']

    if day:
        day_index = days.index(day.lower())

    # convert time into 24 hour
    if 'PM' in start:
        start = start.replace("PM", "")
        start = start.strip()
        hour, minute = start.split(':')
        start_h = int(hour) + 12
        start_m = int(minute)

    else:
        start = start.replace("AM", "")
        start = start.strip()
        hour, minute = start.split(':')
        start_h = int(hour)
        start_m = int(minute)

    # whole calculation
    const = (start_m + duration_m) // 60
    new_m = (start_m + duration_m) % 60
    const2 = (start_h + duration_h + const) // 24
    new_h = (start_h + duration_h + const) % 24

    if day:
        day_index += const2 % 7
        day_index = day_index % 7

    # formatting
    if new_m // 10 < 1:
        new_m = '0' + str(new_m)

    if new_h >= 12 or new_h == 0:
        if new_h == 0:
            new_h = 12
            new_date = str(new_h) + ':' + str(new_m) + ' AM'

        elif new_h == 12:
            new_date = str(new_h) + ':' + str(new_m) + ' PM'

        else:
            new_h -= 12
            new_date = str(new_h) + ':' + str(new_m) + ' PM'

    else:
        new_date = str(new_h) + ':' + str(new_m) + ' AM'

    # day
    if day:
        new_day = days[day_index]
        new_day = new_day[0].upper() + new_day[1:]

    if const2 == 1:
        news = ' (next day)'

    elif const2 > 1:
        news = f' ({const2} days later)'

    elif const2 == 0:
        news = ''


    if day:
        new_time = new_date + ', ' + new_day + news

    else:
        new_time = new_date + news


    return new_time

print(add_time('8:16 PM', '466:02', 'tuesday'))
