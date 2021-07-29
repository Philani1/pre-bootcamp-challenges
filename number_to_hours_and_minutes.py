def number_to_hours_and_min(num):
    hours = num / 60
    minutes = num % 60
    hour_unit = ""
    minute_unit = ""
    if int(hours) == 1:
        hour_unit = "hour"
    else:
        hour_unit = "hours"

    if minutes == 1:
        minute_unit = "minute"
    else:
        minute_unit = "minutes"

    return f"{int(hours)} {hour_unit}, {minutes} {minute_unit}"


if __name__ == "__main__":
    num = int(71)
    print(number_to_hours_and_min(num))
