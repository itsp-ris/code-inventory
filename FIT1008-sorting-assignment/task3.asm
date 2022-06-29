	.data
prompt1:.asciiz "Enter size: "
prompt2:.asciiz "Enter temperature: "
prompt3:.asciiz "Enter target temperature: "
size:	.word 0
the_list:.word 0
target:	.word 0
i:	.word 0
j:	.word 0
count:	.word 0

	.text
	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt1	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	sw $v0, size	# store input value in variable size
	
	# Initialize list
	lw $t0, size	# load value in variable size to $t0
	li $t1, 4	# load 4 to $t1
	mult $t0, $t1	# $t0*$t1
	mflo $t2	# move value from lo register to $t2
	add $a0, $t1, $t2	# store the value $t1+$t2 in $a0
	li $v0, 9	# set $v0: 9 to allocate memory
	syscall
	
	sw $v0, the_list	# store the address of the first position of the array: $v0 in variable the_list
	sw $t0, ($v0)	# store length of array in the address in $v0: address of the first position
	
inputList:
	# Check
	lw $t0, i	# load value of variable i to $t0
	lw $t1, size	# load value of variable size to $t1
	bge $t0, $t1, userInput	# while $t0 < $t1: while i < size:
	
	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt2	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	lw $t0, i	# load value in variable i to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first position of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 in $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 in $t3: address of the i position of the array
	sw $v0, ($t3)	# store input value in the address in $t3: address of the i position of the array
	
	lw $t0, i	# load value in variable i to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: i += 1
	sw $t0, i	# store the value in $t0 in variable i
	
	j inputList	# jump to inputList
	
userInput:	
	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt3	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	sw $v0, target	# store input value in variable target
	
search:	# Check
	lw $t0, j	# load value in variable j to $t0
	lw $t1, size	# load value in variable size to $t1
	bge $t0, $t1, end	# while $t0 < $t1: while j < size:
	
	# Get the_list[j] value and compare
	lw $t0, j	# load value in variable j to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 in $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 in $t3
	lw $t4, ($t3)	# load value in the address in $t3: address of j position of the array to $t4
	lw $t5, target	# load value in variable target to $t5
	bgt $t4, $t5, counter	# if $t4 < $t5: # if the_list[j] < target:
	
	lw $t0, j	# load value in variable j to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: j += 1
	sw $t0, j	# store the value in $t0 in variable j
	
	j search	# jump to search
	
counter:
	lw $t6, count	# load value in variable count to $t6
	addi $t6, $t6, 1	# store the value $t6+1 in $t6: count += 1
	sw $t6, count	# store the value in $t6 in variable count
	
	lw $t0, j	# load value in variable j to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: j += 1
	sw $t0, j	# store the value in $t0 in variable j
	
	j search	# jump to search
	
end:	# Print
	li $v0, 1	# set $v0: 1 to print integer
	lw $a0, count	# load value in variable count to $a0
	syscall
	
	# End program
	li $v0, 10	# set $v0: 10 to end program
	syscall
