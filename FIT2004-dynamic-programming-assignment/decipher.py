'''
ID: 28390121
author: Priscilla Tham
Date: 08.04.2019
'''


class Decipher:
    message = ''

    def __init__(self):
        self.fstSequence = ''
        self.sndSequence = ''

    def createDP(self, column_size, row_size, value=0):
        '''
        function creates a dynamic table array of size row_size * column_size to implement dynamic programming
        precondition:
        :param: column_size: number of columns
                row_size: number of rows
                value: initialisation value; set to default 0
        postcondition:
        :return: dynamic table array created
        complexity: time: best and worst: O(nm) where n is the number of rows and m is the number of columns
                        or vice versa
                    space: O(nm)
        error handling:
        '''
        return [[value for _ in range(column_size + 1)] for _ in range(row_size + 1)]

    def messageFind(self, filename='encrypted_1.txt'):
        '''
        function will find out the initial deciphered message (longest subsequence of common alphabets) from two
        encrypted text
        precondition: the file is not empty and each text is in each line
        :param: filename: the name of the file which contains the two encrypted text
        postcondition: the file is not modified
        :return:
        complexity: time: best and worst: O(nm) where n is the size of the first text and m is the size of the second text
                        or vice versa
                    space: O(nm)
        error handling: return current content of the message class variable if file does not exist
        '''
        try:
            with open(filename, 'r', encoding='utf-8-sig') as file:
                content = file.read()

            content_len = len(content)
            # when number of characters == 1, for loop runs 1 time
            # when number of characters > 1, for loop runs n times
            for i in range(content_len):
                if content[i] == '\n':
                    break
                self.fstSequence += content[i]

            # when number of characters == 1, for loop runs 1 time
            # when number of characters > 1, for loop runs m times
            for j in range(i + 1, content_len):
                if content[j] == '\n':
                    break
                self.sndSequence += content[j]

            fstSeq_len = len(self.fstSequence) + 1
            sndSeq_len = len(self.sndSequence) + 1
            dp = self.createDP(sndSeq_len, fstSeq_len)
            # loop runs n times
            for k in range(1, fstSeq_len):
                # loop runs m times
                for m in range(1, sndSeq_len):
                    if self.fstSequence[k - 1] != self.sndSequence[m - 1]:
                        dp[k][m] = max(dp[k - 1][m], dp[k][m - 1])
                    else:
                        dp[k][m] = 1 + dp[k - 1][m - 1]

            # loop depends on whether k (n) and m (m) is greater
            while k > 0 and m > 0:
                if self.fstSequence[k - 1] == self.sndSequence[m - 1]:
                    self.message += self.fstSequence[k - 1]
                    k -= 1
                    m -= 1
                elif dp[k - 1][m] >= dp[k][m - 1]:
                    k -= 1
                else:
                    m -= 1
            self.message = self.message[::-1]
            return
        except FileNotFoundError:
            return

    def retrieveMsg(self, dp_table, wordList, length):
        '''
        function extracts the stored index in the dynamic table array to fetch matching word(s) from a list, from
        initial deciphered message
        precondition: there are matching words and its index is stored in the dynamic table array
        :param: dp_table: dynamic table array to extract the indexes from
                wordList: list of words
                length: length of the initial deciphered message
        postcondition:
        :return: extracted message
        complexity: time: best and worst: O(n) where n is the number of columns
                    space: O(p) where p is the total number of characters in the message
        error handling:
        '''
        msg = ''
        prediction = ''
        p = 1
        # loop runs n times
        while p < length + 1:
            if dp_table[1][p] > -1:
                if prediction != '':
                    msg += prediction + ' ' + wordList[dp_table[1][p]]
                    prediction = ''
                else:
                    msg += wordList[dp_table[1][p]]
                p += len(wordList[dp_table[1][p]])
                if p < length:
                    msg += ' '
            else:
                prediction += self.message[p - 1]
                p += 1
        if prediction != '':
            msg += prediction
        return msg

    def findMax(self, wordList, length):
        '''
        function finds the maximum length of characters among words in a list
        precondition: list is not empty
        :param: wordList: list of words
                length: size of the list
        postcondition:
        :return: maximum length of characters
        complexity: time: best and worst: O(n) where n is the number of words in the list
        error handling:
        '''
        max = len(wordList[0])
        # loop runs n times
        for i in range(1, length):
            n = len(wordList[i])
            if n > max:
                max = n
        return max

    def wordBreak(self, filename='dictionary_1.txt'):
        '''
        function will break the deciphered message stored in the message class variable into multiple words using the
        vocabulary from a list of words
        precondition: there must an initial deciphered message stored in the message class variable
        :param: filename: the file which contains the vocabulary
        postcondition: the file is not modified
        :return:
        complexity: time: best: O(m) where m is the maximum number of characters in a word
                        worst: O(m*km) where k is the size of the initial deciphered message and m is the maximum
                        number of characters in a word
                    space: O(km+nm)
        error handling: return current content of the message class variable if file does not exist
        '''
        try:
            with open(filename, 'r', encoding='utf-8-sig') as dictFile:
                dictWords = dictFile.read()

            dictWords = dictWords.split()
            dict_len = len(dictWords)
            if dict_len != 0:
                max = self.findMax(dictWords, dict_len)

                msg_len = len(self.message)
                dp = self.createDP(msg_len, max, -1)

                if msg_len < max:
                    max = msg_len
                j = 0
                start = 0
                end = max
                # loop runs m times
                # best case when there is not matching words
                while max > 0:
                    if self.message[start:end] != dictWords[j]:
                        j += 1
                        if j == dict_len:
                            start += 1
                            end += 1
                            j = 0
                    else:
                        # loop runs m times
                        for k in range(start + 1, end + 1):
                            if dp[max][end] >= 0:
                                break
                            if dp[max][k] < 0:
                                dp[max][k] = j
                            elif dp[max][k] >= j:
                                dp[max][end-k] = -1
                                dp[max][k] = j
                            else:
                                break
                        start += 1
                        end += 1
                        # start = end
                        # end += max
                        j = 0
                    if end > msg_len:
                        dp[max - 1] = dp[max][:]
                        max -= 1
                        start = 0
                        end = max
                # loop runs km times
                for m in range(msg_len + 1):
                    if dp[1][m] > -1:
                        self.message = self.retrieveMsg(dp, dictWords, msg_len)
                        break
            return
        except FileNotFoundError:
            return

    def getMessage(self):
        '''
        function returns the current content of the class instance variable message as string
        precondition:
        :param:
        postcondition:
        :return: current content of the message class variable as string
        complexity: time: best and worst: O(n) where n = 1 is possible
        error handling:
        '''
        return self.message


if __name__ == '__main__':
    someMsg = Decipher()
    someMsg.messageFind('test.txt')
    someMsg.wordBreak('dict.txt')
    print(someMsg.getMessage())

    someMsg = Decipher()
    someMsg.messageFind('encrypted_10.txt')
    someMsg.wordBreak('dictionary_10.txt')
    print(someMsg.getMessage())
