def counter(target):
    '''
    function totals the number of element in the list which is more than the target
    author: 28390121 Priscilla Tham
    Date: 22.03.2018
    precondition: element of the list must be natural numbers
    :param:
    postcondition:
    :return:
    complexity: O(n)
    '''
    count = 0

    for j in range(len(the_list)):

        if the_list[j] > target:
            count += 1

    return count


size = int(input('Enter size: '))

the_list = [0] * size

i = 0

while i < size:
    item = int(input('Enter temperature: '))
    the_list[i] = item
    i += 1

target = int(input('Enter target temperature: '))

print(counter(target))