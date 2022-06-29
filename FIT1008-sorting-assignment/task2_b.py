size = int(input('Enter size of list: '))

the_list = [0] * size

i = 0

while i < size:
    item = int(input('Enter an integer: '))
    the_list[i] = item
    i += 1

j = 1

while j < size:
    k = j

    while (k > 0) and (the_list[k - 1] < the_list[k]):

        temp = the_list[k - 1]
        the_list[k - 1] = the_list[k]
        the_list[k] = temp

        k -= 1

    j += 1

print(str(the_list[0] - the_list[-1]))
