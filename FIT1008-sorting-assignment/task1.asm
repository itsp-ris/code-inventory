	.data
prompt:	.asciiz "Enter year: "
str1:	.asciiz "Is a leap year"
str2:	.asciiz "Is not a leap year"
year:	.word 0

	.text
userInput:	
	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	sw $v0, year	# store input value in variable year
	
check1:	# Check
	lw $t0, year	# load value in variable year to $t0
	li $t1, 1582 	# load 1582 to $t1
	blt $t0, $t1, userInput	# if $t0 >= $t1: # if year >= 1582:
	
	lw $t0, year	# load value in variable year to $t0
	li $t1, 4	# load 4 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t1	# move value from hi register to $t1
	bne $0, $t1, check3	# if $t1 == 0:
	
check2:	# Check
	lw $t0, year	# load value in variable year to $t0
	li $t1, 100	# load 100 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t1	# move from hi register to $t1
	bne $0, $t1, true	# if $t1 == 0:
	
check3: # Check
	lw $t0, year	# load value in variable year to $t0
	li $t1, 400	# load 400 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t1	# move from hi register to $t1
	bne $0, $t1, false	# if $t1 != 0:

true:	# Print
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str1	# set $a0 to address of the first character of the string
	syscall
	
	j end	# jump to End
	
false:	# Print
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str2	# set $a0 to address of the first character of the string
	syscall
	
end:	# End program
	li $v0, 10	# set $v0: 10 to end program
	syscall