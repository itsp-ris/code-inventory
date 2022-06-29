size = int(input('Enter size: '))

the_list = [0] * size

i = 0

while i < size:
    item = int(input('Enter temperature: '))
    the_list[i] = item
    i += 1

target = int(input('Enter target temperature: '))

j = 0
count = 0

while j < size:
    
    if the_list[j] > target:
        count += 1

    j += 1

print(count)
