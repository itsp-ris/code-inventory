	.data
prompt1:.asciiz "Enter size of list: "
prompt2:.asciiz "Enter an integer: "
i:	.word 0
j:	.word 1
k:	.word 0
size:	.word 0
the_list:.word 0

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
	sw $t0, ($v0)	# store length of array: $t0 in the address in $v0: address of the first position
	
inputList:
	# Check
	lw $t0, i	# load value of variable i to $t0
	lw $t1, size	# load value of variable size to $t1
	bge $t0, $t1, sort	# while $t0 < $t1: while i < size:
	
	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt2	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	lw $t0, i	# load value in variable i to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 to $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 to $t3: address of the i position of the array
	sw $v0, ($t3)	# store input value in the address in $t3: address of the i position of the array
	
	lw $t0, i	# load value in variable i to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: i += 1
	sw $t0, i	# store the value in $t0 in variable i
	
	j inputList	# jump to inputList
	
sort:	lw $t0, j	# load value in variable j to $t0
	lw $t1, size	# load value in variable size to $t1
	bge $t0, $t1, end	# while $t0 < $t1: # while j < size:
	
	sw $t0, k	# store the value in $t0 to variable k: k = j
	
check:	lw $t0, k	# load value in variable k to $t0	
	ble $t0, $0, increment	# while $t0 > 0: # while k > 0:	
	
	# Get the_list[k-1] value
	lw $t0, k	# load value in variable k to $t0
	subi $t1, $t0, 1	# store the value $t0-1 in $t1
	lw $t2, the_list	# load value in variable the_list to $t2: address of the first postion of the array
	li $t3, 4	# load 4 to $t3
	mult $t1, $t3	# $t1*$t3
	mflo $t4	# move value from lo register to $t4
	add $t4, $t4, $t3	# store the value $t4+$t3 to $t4
	add $t4, $t4, $t2	# store the value $t4+$t2 to $t4
	lw $t5, ($t4)	# load value in the address in $t4: address of (k - 1) position of the array to $t5
	
	# Get the_list[k] value
	lw $t0, k	# load value in variable k to $t0
	lw $t2, the_list	# load value in variable the_list to $t2: address of the first postion of the array
	li $t3, 4	# load 4 to $t3
	mult $t0, $t3	# $t0*$t3
	mflo $t6	# move value from lo register to $t6
	add $t6, $t6, $t3	# store the value $t6+$t3 to $t6
	add $t6, $t6, $t2	# store the value $t6+$t2 to $t6
	lw $t7, ($t6)	# load value in the address in $t6: address of k position of the array to $t7
	
	bge $t5, $t7, increment	# while $t5 < $t7: # while the_list[k-1] < the_list[k}:
	
	# Get the_list[k-1] value
	lw $t0, k	# load value in variable k to $t0
	subi $t1, $t0, 1	# store the value $t0-1 to $t1
	lw $t2, the_list	# load value in variable the_list to $t2: address of the first postion of the array
	li $t3, 4	# load 4 to $t3
	mult $t1, $t3	# $t1*$t3
	mflo $t4	# move value from lo register to $t4
	add $t4, $t4, $t3	# store the value $t4+$t3 to $t4
	add $t4, $t4, $t2	# store the value $t4+$t2 to $t4
	lw $t5, ($t4)	# load value in the address in $t4: address of (k - 1) position of the array to $t5
	
	# Get the_list[k] value
	lw $t0, k	# load value in variable k to $t0
	lw $t2, the_list	# load value in variable the_list to $t2: address of the first postion of the array
	li $t3, 4	# load 4 to $t3
	mult $t0, $t3	# $t0*$t3
	mflo $t6	# move value from lo register to $t6
	add $t6, $t6, $t3	# store the value $t6+$t3 to $t6
	add $t6, $t6, $t2	# store the value $t6+$t2 to $t6
	lw $t7, ($t6)	# load value in the address in $t6: address of k position of the array to $t7
	
	# Swap
	sw $t7, ($t4)	# store the value in $t7 in the address in $t4: address of (k - 1) position of the array
	sw $t5, ($t6)	# store the value in $t5 in the address in $t6: address of k position of the array
	
	lw $t0, k	# load value in variable k to $t0
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: k -= 1
	sw $t0, k	# store the value in $t0 in variable k
	
	j check	# jump to check
	
increment:
	lw $t0, j	# load value in variable j to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: j += 1
	sw $t0, j	# store the value in $t0 in variable j
	
	j sort	# jump to sort
	
end:	# Get max address
	lw $t0, size	# load value in size to $t0
	sub $t0, $t0, $t0	# store the value $t0-$t0 in $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 to $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 to $t3
	
	# Get min address
	lw $t0, size	# load value in size to $t0
	subi, $t0, $t0, 1	# store the value $t0-1 in $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t4	# move value from lo register to $t4
	add $t4, $t4, $t2	# store the value $t4+$t2 to $t4
	add $t4, $t4, $t1	# store the value $t4+$t1 to $t4
	
	# Computation and Print
	li $v0, 1	# set $v0: 1 to print integer
	lw $t0, ($t3)	# load value in address in $t3: max value address to $t0
	lw $t1, ($t4)	# load value in address in $t4: min value address to $t1
	sub $a0, $t0, $t1	# store the value $t0-t1 in $a0
	syscall
	
	# End program
	li $v0, 10	# set $v0: 10 to end program
	syscall
	
	
