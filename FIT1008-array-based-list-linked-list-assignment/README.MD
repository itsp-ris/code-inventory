**Requirements**
1. Provide documentation and testing for each piece of functionality in your code. 
<br />Documentation needs to include pre and post conditions, and information on any parameters used.
2. Create a new file/module for each task or subtask.
3. Write a function to test each function or method you implement, and at least two test cases per function. 
<br />There is no need to test menu functions, but all ADT operations should be tested separately.

<br />

**Task 1: Array-Based List**
<br /><br />Limitations: 
1. Use 50 as the maximum number of elements.
2. Include implementations for 
	1) __ str __ (self)
	2) __ len __ (self)
	3) __ contains __ (self, item)
	4) __ getitem __ (self, index)
	5) __ setitem __ (self, index, item): Sets the value at index in the list to be item.
	6) __ eq __ (self, other):  Returns True if this list is equivalent to other.
	7) __ append __ (self, item)
	8) __ insert __ (self, index, item)
	9) __ remove __ (self, item): Deletes the first instance of item from the list.
	10) __ delete __ (self, index)
	11) __ sort __ (self, reverse)
3. Make the class iterable

<br />

**Task 2: Modify list so that size is dynamic**
<br /><br />Limitations:
1. The base size of the array is 20 and should never be less than 20. 
<br />However, if the list becomes full, it is resized to be 2 times larger than the current size. 
<br />Likewise, the underlying size should decrease by half if the underlying array is larger than the base size 
but the content occupies less than 1/8 of the available space.

<br />

**Task 3: Redo Task 1 with a Linked Structure.**

<br />

**Task 4: Implement a function that takes a filename as input and reads it into an instance of the class 
implemented on Task 2 and 3.**
<br /><br />Limitations:
1. For each line in the file, store it as a single item in the list.

<br />

**Task 5: Text editor as Python Program.**
<br /><br />Limitations:
1. Allows a user to perform the 6 commands shown below using a menu.
<br />The list should be the type implemented on Task 2.
	1) insert num: which inserts a line of text (given by the user) in the list before position num, 
	and raises an exception if no num is given
	2) read filename
	3) write filename: which creates or opens a file, filename, writes every item in the list into the file, 
	and then closes the file
	4) delete num: which deletes the line of text in the list at position num, 
	and deletes all the lines if no num is given
	5) search word: which takes a word and prints the line numbers in which the target word appears. 
	<br />Search should be case insensitive. 
	<br />Search should work as expected in a standard text editor, for example ignoring punctuation. 
	<br />This function must be accessible through the menu via commands search
	6) quit

<br />

**Task 6: Re-implement your editor using a Linked List instead of an Array-based list.**

<br />

**Application Development Tools**
1. PyCharm






