def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

    return [
        seconds_row_lights(seconds % 2)
        , five_hours_row_lights(hours)
        , single_hours_row_lights(hours % 5)
        , five_minutes_row_lights(minutes)
        , single_minutes_row_lights(minutes % 5)
    ]


def seconds_row_lights(seconds):
    return ["Y","O"][seconds%2]


def five_hours_row_lights(hours):
    lights_on = hours // 5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)


def single_hours_row_lights(hours_mod_5):
    lights_on = hours_mod_5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)


def five_minutes_row_lights(minutes):
    lights_on = minutes // 5
    lights_in_row = 11
    return lights_for_row("Y", lights_on, lights_in_row)


def single_minutes_row_lights(minutes_mod_5):
    lights_on = minutes_mod_5
    lights_in_row = 4
    return lights_for_row("Y", lights_on, lights_in_row)


def lights_for_row(character, lights_on, lights_in_row):
    return character*lights_on + "O"*(lights_in_row - lights_on)


if __name__ == "__main__":
    time = input()
    result = berlin_clock_time(time)
    print ("\n".join(result))


