
def daysInMonth(month: int, year: int) -> int:
    """
    return number of days in the month
    """
    def leapYear(year) -> bool:
        """
        returns True if leap year 
        """
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    days = {
        1: 31,
        2: 29 if leapYear(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return days[month]


def checkDateValidity(*args) -> bool:
    """
    parameters: list(int(list)) \n
    date format [DD,MM,YYYY] \n
    Check valid dates according to Gregorian calendar
    returns True if all dates are valid
    else returns False
    """

    for date in args:
        i = 2
        while i >= 0:
            if date[i] <= 0:
                return False
            i -= 1
        if date[0] > daysInMonth(date[1], date[2]) or date[1] > 12 or date[2] > 9999:
            return False
    return True
