def insertionSort():
    '''
    function sorts a list
    author: 28390121 Priscilla Tham
    Date: 22.03.2018
    precondition: element of the list must be decimal numbers: integers
    :param:
    postcondition:
    :return:
    complexity: O(n**2)
    '''
    for j in range(1, len(the_list)):
        k = j

        while (k > 0) and (the_list[k - 1] < the_list[k]):

            temp = the_list[k - 1]
            the_list[k - 1] = the_list[k]
            the_list[k] = temp

            # correction: a, b = b, a
            # the_list[k], the_list[k - 1] = the_list[k - 1], the_list[k]

            k = k - 1


size = int(input('Enter size of list: '))

the_list = [0] * size

for i in range(size):
    item = int(input('Enter an integer: '))
    the_list[i] = item

insertionSort()

print(str(the_list[0] - the_list[-1]))

