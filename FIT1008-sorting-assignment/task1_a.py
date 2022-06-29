def is_leap_year(year):
    '''
    function determines whether a year is a leap year or not a leap year
    author: 28390121 Priscilla Tham
    Date: 22.03.2018
    precondition: year input must be more than or equal to 1582
    :param: decimal number: integer (positive)
    postcondition:
    :return: returns a boolean expression: 'True' or 'False'
    complexity: O(1)
    '''
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True

    else:
        return False


year = 0

while year < 1582:
    year = int(input('Enter year: '))

if is_leap_year(year) == True:
    print('Is a leap year')

else:
    print('Is not a leap year')
