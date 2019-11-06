def get_clock(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

    single_second = get_seconds(seconds % 2)
    five_hours = get_five_hours(hours)
    single_hours = get_hours(hours % 5)
    five_minutes = get_five_minutes(minutes)
    single_minutes = get_minutes(minutes % 5)

    return [
		single_second,
		five_hours,
		single_hours,
		five_minutes,
		single_minutes]


def get_seconds(seconds):
    return ["Y","O"][seconds%2]


def get_hours(hours_mod_5):
    lights_on = hours_mod_5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)


def get_five_minutes(minutes):
    lights_on = minutes // 5
    lights_in_row = 11
    return lights_for_row("Y", lights_on, lights_in_row)


def get_minutes(minutes_mod_5):
    lights_on = minutes_mod_5
    lights_in_row = 4
    return lights_for_row("Y", lights_on, lights_in_row)


def get_five_hours(hours):
    lights_on = hours // 5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)


def lights_for_row(character, lights_on, lights_in_row):
    return character*lights_on + "O"*(lights_in_row - lights_on)


if __name__ == "__main__":
    time = input()
    result = get_clock(time)
    print ("\n".join(result))


