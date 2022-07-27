**Requirements**
1. Provide documentation and testing for each piece of functionality in your code. 
<br />Documentation needs to include pre and post conditions, and information on any parameters used.
2. Create a new file/module for each task or subtask.
3. Not allowed to use the Python built-in dict methods.
4. Write a function to test each function or method you implement, and at least two test cases per function. 
<br />There is no need to test menu functions, but The cases need to show that your functions can handle both valid 
and invalid inputs.

<br />

**Task 1: Hash Table using Linear Probing**
<br /><br />Limitations: 
1. Linear Probing to resolve collisions.
2. Include implementations for 
	3) __ contains __ (self, key)
	4) __ getitem __ (self, key)
	5) __ setitem __ (self, key, value):  Sets the value corresponding to key in the hash table to be value.
	6) __ hash __ (self, key):  Calculates the hash value for the given key. (Hash function is given)

<br />

**Task 2**
<br /><br />Limitations:
1. Download from Moodle the dictionary files english_small.txt, english_large.txt and french.txt
<br />For each of these dictionaries, time how long it takes to read all words in it into the hash table.
<br />Do this for each of the following table_size values: 210000, 209987, 400000 and 399989 and 202361.
<br /> Present the wall times recorded in a table.
<br />Write a short analysis reporting what values work best and which work poorly. 
<br />Explain why these might be the case.

<br />

**Task 3: Modify hash table implementation to now track the number of collisions, the load, 
as well as the average probe length**
<br /><br />Limitations:
1. Using collisions, probe length and wall time, choose appropriate values of a (in hash function) and table_size.
<br /> Find values that perform well across all three files. For this task use a maximum table size of 400000.
<br />Explain your choice by presenting all data behind your reasoning recorded in a table.

<br />

**Task 4: Hash Table using Quadratic Probing.**
<br /><br />Limitations:
1. Quadratic Probing to resolve collisions.
2. Implement dynamic hashing, by doubling the size of the underlying array (and rehashing) every time 
the load exceeds 2/3.
3. Compare the number of collisions, probe length and running time found when loading each dictionary against 
the best combination found using the Linear Probing hash table.

<br />

**Task 5: Hash Table using Separate Chaining.**
<br /><br />Limitations:
1. Compare the performance of Separate Chaining against the linear probe above.

<br />

**Task 6**
<br /><br />Limitations:
1. Download some ebooks as text files from https://www.gutenberg.org/ and use these files as a collection of English.
<br />Read these into your Quadratic Probing hash table to count the number of each word in the texts.
<br />Considering the data you collected in Task 2, select an appropriate table size for the text files.
<br />Use these occurrence counts to construct a table which can be used to look up whether a given word is
common, uncommon or rare within written English.

<br />

**Task 7**
<br /><br />Limitations:
1. Implement the program in Task 3 using Python’s dict class.
<br />How does the performance of your own implementations compare to Python’s in terms of the wall time?
<br />What factors may drive the differences?
<br />How close can you get to the reference implementation?

**Application Development Tools**
1. PyCharm

<i>A little backstory:
A lot of the students had other assignments piling in along with this one. 
Most of us did not complete this assignment on time.</i>
