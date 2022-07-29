**Requirements**
1. Add comments and documentation to the code.
2. Briefly describe the solution and its space and time complexity to the problem in a PDF file 
named Analysis.pdf
<br />The PDF file must give an outline of the solution (e.g., a high level idea of how did you solve it) 
and the worst-case space and time complexity of the solution.

<br />

**Limitations:**
1. The input file consists of the variable number of words not sorted in alphabetical order.
<br />Each word consists of only lowercase English characters, i.e., there is no uppercase letter.
2. Sentences of the input are separated by newline.
3. Let n be the total number of words in the writing and m be the maximum number of characters in 
a word. <br />The upper bound of the input size is O(nm).
4. The program must be able to:
    1) Preprocess: Remove the auxiliary verbs, articles and punctuation marks 
    (only comma(,), period(.), question(?), exclamation(!), colon(:), semicolon(;), and quotation(")); 
    <br /> worst case time and space complexity allowed: O(nm).
    2) Sort in alphabetical order: worst time and space complexity allowed: O(nm).
    3) Show the number of total words including frequency of each word: List of words should remain sorted; 
    <br />worst time & space complexity allowed: O(nm).
    4) Show the k top-most words appears in the file: If the count of two words are the same, 
    the word comes earlier in the sorted list will have higher priority over another; 
    <br />worst time and space complexity allowed: O(n log k) and O(km) respectively.
5. Do not use hashing and python dictionary.

<br />

**Application Development Tools**
1. PyCharm
