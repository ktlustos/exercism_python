def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap
