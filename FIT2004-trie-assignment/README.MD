**Requirements**
1. Briefly describe the solution and its space and time complexity to the problem in 
a PDF file named Report_A3.pdf
2. The PDF file must give an outline of the solution (e.g., a high level idea of how did you 
solve it) and the worst-case space and time complexity of the solution.

<br />

**Task 1: Database Query**
<br /><br />Limitations:
1. Input is a text file, named database.txt, containing N records: record index, identification
number, first name, last name, phone number, and email address.
<br />Every line is an entry that represents the details of one person only.
<br />No two lines are identical, though some fields may be the same (e.g. same first name).
2. The indices start at 0 and increase by 1 each line, so they are unique. 
The identification numbers are also all unique.
3. Each piece of information of a person is space-separated.
<br />Format of each line in the input: 
Record_index Identification_no First_name Last_name Phone_number Email_address
4. Record indices, identification numbers and phone numbers are only integer.
<br />Identification numbers can have different length.
<br />First name and last name contains only English alphabets in both cases.
<br />Email address is the combination of alpha-numeric values with 4 special characters: 
at(@), dot(.), hyphen(-) and underscore(_)
5. Each line contains only one person's information, therefore, the number of lines in the input 
file is N. <br />The maximum length of a single record is M characters, so the size of the input file 
database.txt will be O(NM).
6. The program must be able to: 
    1) Given a file of records and a query which consists of two parameters, id_prefix and 
    last_name_prefix, find the indices of all records which have an identification number (id) 
    whose prefix is id_prefix and a last name whose prefix is last_name_prefix.
    <br />This list can be empty. This list does not have to be sorted, it can be in any order.
    2) Construct appropriate TRIEs inside this function: worst time and space complexity allowed: 
    O(T) where T is the number of characters in all identification numbers and all last names, 
    and O(T + NM) respectively.
    3) Implement your own Trie and are NOT ALLOWED to use publicly available implementations. 
    <br />Also, you are NOT ALLOWED to use Python dictionary (i.e., hash tables) or 
    linked lists for implementing Trie. 
    <br />You must use arrays (called lists in Python) to implement the nodes of the Trie.

<br />

**Task 2: Reverse substrings search**
<br /><br />Limitations:
1. Write a function reverseSubstrings(filename) which takes as input a filename.
<br />The file contains a single line containing only lowercase a-z characters.
2. The function returns a lists of lists, where each inner list will contain two values.
<br /> The first value will be a substring with length >1 whose reverse exists in the string, 
and the second value will be the index of that substring in the input text.
3. The function should run in O(K^2 + P), where K is the total number of characters in the input
string and P is the total length of all substrings whose reverse appears in the string. 
<br />The space complexity should be O(K^2 + P).

<br />

**Application Development Tools**
1. PyCharm
