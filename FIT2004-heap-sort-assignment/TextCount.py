'''
ID: 28390121
author: Priscilla Tham
Date: 12.03.2019
'''

# task 1
def preprocess(filename):
    '''
    function opens a file and removes punctuations, auxiliary verbs and articles from the content
    precondition:
    :param: filename: the name of the file the user wants to open
    postcondition: the file is not modified
    :return: the list of words in the file after removing punctuations, auxiliary verbs and articles
    complexity: time: best: O(n) where n is the total number of words in the file and n = 1 is possible
                      worst: O(nm) where n is the total number of words in the file and m is the maximum number
                      of characters in a word
                space: O(nm)
    '''
    with open(filename, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    if len(content) == 0:
        return []
    punctuation = '",.?!;:'
    verbs_articles = ['am', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'may', 'can',
                      'would', 'should', 'might', 'could', 'a', 'an', 'the']
    text = ''
    wordsList = []

    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs p times
    # where p is the total number of characters
    for i in range(len(content)):
        # if loop traverses the list in constant time
        if content[i] not in punctuation:
            text += content[i]
    # when number of characters == 1, system look for whitespace(s) once
    # when number of characters > 1, system look for whitespace(s) n times
    text = text.split()

    # when number of words == 1, loop runs 1 time
    # when number of words > 1, loop runs n times
    for j in range(len(text)):
        # if loop traverse the list in constant time
        if text[j] not in verbs_articles:
            wordsList += [text[j]]
    return wordsList

# task 2
def wordSort(wordsList):
    '''
    function sorts items in the list
    precondition: list is not empty and does not contain punctuation, auxiliary verbs and articles
    :param: wordsList: the list to be sorted
    postcondition:
    :return: sorted list
    complexity: time: best and worst: O(nm) where n is the total number of words in the file and m is the maximum number
                    of characters in a word
                space: O(nm)
    '''
    n = len(wordsList)
    if n == 0:
        raise IndexError
    tmp = [[] for _ in range(27)]
    maxLen = len(wordsList[0])

    # when number of words == 1, loop runs 1 time
    # when number of words > 1, loop runs (n-1) times
    for i in range(1, n):
        if len(wordsList[i]) > maxLen:
            maxLen = len(wordsList[i])

    # when list is sorted, first loop runs m times and second loop runs n times
    for j in range(maxLen, 0, -1):
        for k in range(n):
            if len(wordsList[k]) >= j:
                index = ord(wordsList[k][j-1]) - 96
                tmp[index] += [wordsList[k]]
            else:
                tmp[0] += [wordsList[k]]
        wordsList[:] = []
        # loop runs constant time
        for m in range(len(tmp)):
            if tmp[m]:
                wordsList += tmp[m]
        tmp[:] = [[] for _ in range(27)]
    return wordsList

# task 3
def wordCount(wordsList):
    '''
    function counts the total number of words including the frequency of each word in the file
    precondition: words in the list are sorted alphabetically
    :param: wordsList: the sorted list of words in the file
    postcondition:
    :return: sorted list with total number of words and their count
    complexity: time: best: O(n) where n is the total number of words and n = 1 is possible
                      worst: O(nm) where n is the total number of words and m is the maximum number of characters in a
                      word
                space: O(nm)
    '''
    n = len(wordsList)
    if n == 0:
        raise IndexError
    count = 1
    len_freq = [n]

    # when number of words == 1, loop runs 1 time
    # when number of words > 1, loop runs n times
    for i in range(1, n):
        # when number of characters == 1, if loop runs 1 time
        # when number of characters > 1, if loop runs m times
        if wordsList[i-1] != wordsList[i]:
            len_freq += [[wordsList[i-1], count]]
            count = 1
        else:
            count += 1
        if i == n-1:
            len_freq += [[wordsList[i], count]]
    return len_freq

# task 4
def heapify(heapList, index):
    '''
    function sorts items in the heap by sub-heap tree
    precondition:
    :param: heapList: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best: O(log k) where k is the size of the heap
                      worst: O(log k) where k is the size of the heap
    '''
    root = 1
    # loop runs log k time(s)
    while 2*root <= index:
        smallest = root
        left = 2*root
        right = 2*root+1

        if left < index and (heapList[left][1] < heapList[smallest][1] or
                    (heapList[left][1] == heapList[smallest][1] and heapList[left][2] > heapList[smallest][2])):
            smallest = left

        if right < index and (heapList[right][1] < heapList[smallest][1] or
                    (heapList[right][1] == heapList[smallest][1] and heapList[right][2] > heapList[smallest][2])):
            smallest = right

        if smallest == root:
            return
        heapList[smallest], heapList[root] = heapList[root], heapList[smallest]
        root = smallest

def heapSort(heapList):
    '''
    function sorts items in the heap
    precondition:
    :param: heapList: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best: O(k log k) where k is the number of items in the heap and k is the size of the heap
                      worst: O(k log k) where k is the number of items in the heap and k is the size of the heap
    '''
    n = len(heapList)-1
    # when number of items == 1, loop runs 1 time, loop in heapify runs 1 time
    # when number of items > 1, loop runs n times, loop in heapify function runs log k times
    for n in range(n, 0, -1):
        heapList[1], heapList[n] = heapList[n], heapList[1]
        heapify(heapList, n)

def sink(heapList):
    '''
    function moves item down the heap accordingly
    precondition:
    :param: heapList: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best: O(log k) where k is the size of the heap
                      worst: O(log k) where k is the size of the heap
    '''
    root = 1
    # loop runs log k time(s)
    while 2*root <= len(heapList)-1:
        child = 2*root

        if child+1 < len(heapList) and (heapList[child+1][1] < heapList[child][1] or
                (heapList[child][1] == heapList[child+1][1] and
                 heapList[child][2] < heapList[child+1][2])):
            child += 1

        if heapList[root][1] > heapList[child][1] or \
                (heapList[child][1] == heapList[root][1] and heapList[child][2] > heapList[root][2]):
            heapList[root], heapList[child] = heapList[child], heapList[root]
        else:
            return
        root = child

def rise(heapList):
    '''
    function moves item up the heap accordingly
    precondition:
    :param: heapList: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best: O(log k) where k is the size of the heap
                      worst: O(log k) where k is the size of the heap
    '''
    n = len(heapList)-1
    # loop runs log k time(s)
    while n > 1 and heapList[n//2][1] > heapList[n][1]:
        heapList[n//2], heapList[n] = heapList[n], heapList[n//2]
        n //= 2

def kTopWords(k, sortedList):
    '''
    function retrieves k top most frequent words in the file
    precondition: words in the list are sorted alphabetically
    :param: k: value of type integer in the range of 1 to number of words in the file
           sortedList: the sorted list of words in the file to retrieve
    postcondition:
    :return: the list of k top most frequent words sorted by occurrences and then alphabets
    complexity: time: best: O(n log k) where n is the total number of words in the file and k is the size of the heap
                      worst: O(n log k) where n is the total number of words in the file and k is the size of the heap
                space: O(km); m is the maximum number of characters in a word
    '''
    n = len(sortedList)-1
    if k > n+1:
        k = n+1
    elif k <= 0:
        raise AssertionError('Please enter and integer ranging from 1 onwards.')
    heap = [None, sortedList[n]]
    heap[1] += [n]

    # loop runs k time(s), loop in rise function runs log k time(s)
    for i in range(n-1, n-k, -1):
        heap += [sortedList[i]]
        index = n+1-i
        heap[index] += [i]
        rise(heap)

    # loop runs (n-k) time(s), loop in sink function runs log k time(s)
    for j in range(n-k, -1, -1):
        if sortedList[j][1] > heap[1][1] or sortedList[j][1] == heap[1][1]:
            heap[1] = sortedList[j]
            heap[1] += [j]
            sink(heap)
    # heapsort worst complexity is added into the function complexity
    heapSort(heap)
    # loop runs k time(s)
    # so, k log k + (n-k) log k + k log k + k = n log k + k log k + k
    # considering that k <= n, the total complexity in big O notation is O(n log k)
    for m in range(1, k):
        heap[m].pop()
    return heap[1:]

# print function
def printing(aList):
    string = ''
    for i in range(len(aList)):
        string += aList[i][0]+' : '+str(aList[i][1])+'\n'
    return string

def anotherPrinting(aList):
    string = ''
    for i in range(len(aList)):
        string += aList[i]+'\n'
    return string

if __name__ == '__main__':
    while True:
        try:
            fileInput = 'Writing.txt'
            processedWords = preprocess(fileInput)
            sortedWords = wordSort(processedWords)
            print('Words are preprocessed..')
            displayQuery = str(input('Do I need to display the remaining words: '))
            if displayQuery.upper().strip() == 'Y':
                print(anotherPrinting(processedWords))
            elif displayQuery.upper().strip() == 'N':
                    print('\n')
            else:
                raise AssertionError("Please enter 'Y' or 'N'.")

            print('The remaining words are sorted in alphabetical order')
            displayQuery = input('Do you want to see: ')
            if displayQuery.upper().strip() == 'Y':
                print(anotherPrinting(sortedWords))
            elif displayQuery.upper().strip() == 'N':
                print('\n')

            else:
                raise AssertionError("Please enter 'Y' or 'N'.")

            countedWords = wordCount(sortedWords)
            print('The total number of words in the writing:', countedWords[0])
            print('The frequencies of each word: ')
            print(printing(countedWords[1:]))

            displayQuery = int(input('How many top-most frequent words do I display: '))
            kList = kTopWords(displayQuery, countedWords[1:])
            print(str(displayQuery), 'top most words appear in the writing are: ')
            print(printing(kList))
        except AssertionError as e:
            print(e)
        except ValueError:
            print('Please enter integers only.')
        except IndexError:
            print('Unable to continue: \n 1.', fileInput, 'is empty or \n 2. There is no word remaining after '
                'preprocessing.')
