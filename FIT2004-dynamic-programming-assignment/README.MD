**Requirements**
1. Briefly describe the solution and its space and time complexity to the problem in 
a PDF file named Report_2.pdf
2. The PDF file must give an outline of the solution (e.g., a high level idea of how did you 
solve it) and the worst-case space and time complexity of the solution.

<br />

**Limitations:**
1. There are two input files required to complete this text decipher problem.
<br />One named encrypted.txt consists of two variable sized encrypted texts.
<br />Each text contains of only English alphabets (a,b,c,....z), in both lower and uppercase format.
<br />There is no punctuation or whitespace character in each text.
2. In the input file, two texts will be in two consecutive lines, not in same line. 
3. Let consider n and m be the size of first text and second text respectively.
<br />Therefore, the input size of first file is O(n + m)
4. Another input file will contain all possible set of words named dictionary.txt.
<br />Each word is the combination of only upper and (or) lower case alphabets, 
no punctuation or whitespace character.
5. Let's assume that N be the number of words and M be the maximal size of the words in the file.
<br />Therefore, the input size of second file is O(NM).
6. The program must be able to:
    1) Find the longest subsequence of common alphabets: worst time and space complexity allowed: O(nm)
    3) Words separating: Break the deciphered message of (1) into multiple words using the 
    vocabulary, input from dictionary.txt; 
    <br /> worst time and space complexity allowed: O(kM · NM), 
    where k is the size of input string, and O(kM + NM) respectively.
        <br />_Cases:_
        1) Normal condition: Break the message into available words
        2) : If the combine of two or more words is also another large word in the dictionary 
        and the message, use the large word. For an example, in the dictionary there are eight 
        words: 'am', 'i', 'ice', 'cream', 'icecream', 'is', 'old', 'cold' and the message is 
        'icecreamiscold', Use 'icecream is cold' instead of other patterns.
        3) Empty dictionary: Whole message will be treated as a single word.
        4) No matching words: Whole message will be treated as a single word.
        5) Dictionary may not contain all possible words. In this case, not matched segment 
        of the message will be treated as separate words. It can appear in the beginning or 
        in the middle or at the end of the message. For an example, in the dictionary 
        there are five words: 'am', 'i', 'ice', 'cream', `icecream' and the message is 
        'icecreamiscold', the task will predict 'icecream i scold'. Let consider another example, 
        in the dictionary there are six words: 'am', 'i', 'ice', 'cream', 'icecream', 'old' 
        and the message is 'icecreamiscold', the task will predict 'icecream i sc old'.
7. Design the solution of assignment using the concept of Object Oriented Programming.
8. Do not use hashing and python dictionary.

<br />

**Application Development Tools**
1. PyCharm
