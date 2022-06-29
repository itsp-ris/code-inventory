def insertionSort():
    '''
    function sorts a list
    author: 28390121 Priscilla Tham
    Date: 22.03.2018
    precondition: element of the list must be natural numbers
    :param:
    postcondition:
    :return:
    complexity: O(n**2)
    '''

    j = 1
    while j < (len(the_list)):
        k = j

        while (k > 0) and (the_list[k - 1] > the_list[k]):

            temp = the_list[k - 1]
            the_list[k - 1] = the_list[k]
            the_list[k] = temp

            # correction: a, b = b, a
            # the_list[k], the_list[k - 1] = the_list[k - 1], the_list[k]

            k -= 1

        j += 1

def counter():
    '''
    function counts the number of appearance of each element in the list
    author: 28390121 Priscilla Tham
    Date: 22.03.2018
    precondition: element of the list must be natural numbers
    :param:
    postcondition:
    :return:
    complexity: O(n)
    '''
    l = 1
    count = 1

    while l < (len(the_list)):
    
        if the_list[l - 1] == the_list[l]:
            count += 1

        else:
            print(str(the_list[l - 1]), 'appears', count, 'times.')
            count = 1

        if l == (len(the_list) - 1):
            print(str(the_list[l]), 'appears', count, 'times.')

        l += 1

size = int(input('Enter size: '))

the_list = [0] * size

i = 0
while i < size:
    item = int(input('Enter temperature: '))
    the_list[i] = item
    i += 1

insertionSort()
counter()


