import sys
from checkDateValidity import checkDateValidity, daysInMonth


class invalidDateException(Exception):
    pass


def compareDates(dateA: list, dateB: list) -> int:
    """
    Compares dateA and dateB\n
    returns: 1 if dateA > dateB,\n
    -1 if dateA <dateB,
    0 if dateA == dateB \n
    raise Exception if dates are invalid
    """
    if not checkDateValidity(dateA, dateB):
        raise invalidDateException('Invalid Dates')
    i = 2
    while i >= 0:
        if dateA[i] < dateB[i]:
            return -1
        elif dateA[i] > dateB[i]:
            return 1
        else:
            if i == 0:
                return 0
            i -= 1


def countMonths(lastUpdated: list, billingDay: int, currentDate: list) -> int:
    """
    date format:[DD,MM,YYYY] \n
    returns No. of billing days between current date and last updated date \n
    Errors: invalidDateException
    """
    print(lastUpdated, billingDay, currentDate)
    if billingDay > 31 or billingDay < 1:
        raise invalidDateException('Invalid Billing Day')
    if compareDates(currentDate, lastUpdated) == -1:
        raise invalidDateException(
            'Current Date is less than Last Updated Date')
    elif compareDates(currentDate, lastUpdated) == 0:
        return 0

    count = 0
    diffYears = currentDate[2]-lastUpdated[2]
    count += 12*(diffYears-1 if diffYears > 1 else 0)

    if diffYears == 0:
        diffMonths = currentDate[1]-lastUpdated[1]
        count += (diffMonths-1 if diffMonths > 1 else 0)
        if diffMonths == 0:
            if billingDay >= daysInMonth(lastUpdated[1], lastUpdated[2]) and currentDate[0] >= daysInMonth(lastUpdated[1], lastUpdated[2]):
                count += 1
            elif billingDay <= lastUpdated[0]:
                count += 0
            elif currentDate[0] >= billingDay:
                count += 1
            else:
                count += 0
        else:
            count += countMonths(lastUpdated, billingDay, [daysInMonth(lastUpdated[1], lastUpdated[2]), lastUpdated[1], lastUpdated[2]]) + \
                countMonths([1, currentDate[1], currentDate[2]],
                            billingDay, currentDate)
    else:
        count += countMonths(lastUpdated, billingDay,
                             [31, 12, lastUpdated[2]]) + countMonths([1, 1, currentDate[2]], billingDay, currentDate)
    return count


# print(countMonths([15, 2, 2011], 18, [29, 2, 2012]))

# print(countMonths([int(x) for x in sys.argv[1].split('/')], int(sys.argv[2]), [int(x)
    #    for x in sys.argv[3].split('/')]))
