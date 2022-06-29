	.data
prompt1:.asciiz "Enter size: "
prompt2:.asciiz "Enter temperature: "
str1:	.asciiz " appears "
str2:	.asciiz " times. "
size:	.word 0
the_list:.word 0
i:	.word 0

	.text
	j main	# jump to main
	
	# Function begins
insertionSort:	
	# Allocate and save fp and ra
	addi $sp, $sp, -8	# store the value $sp-8 in $sp
	sw $fp, 0($sp)	# store address of $fp in 0($sp)
	sw $ra, 4($sp)	# store address in $ra in 4($sp)
	move $fp, $sp	# copies $sp to $fp
	
	# Allocate for local variables
	addi $sp, $sp, -8	# store the value $sp-8 in $sp
	li $t0, 1	# load 1 to $t0
	sw $t0, -4($sp)	# store value in $t0 in -4($sp): j = 1

check1:	lw $t0, the_list	# load value in variable the_list to $t0: address of the first postion of the array
	lw $t1, ($t0)	# load the value in the address in $t0: address of the first postion of the array to $t1
	lw $t2, -4($fp)	# load value in -4($fp): j to $t2
	bge $t2, $t1, return1	# while $t2 < $t1: # while j < (len(list)):
	
	lw $t1, -4($fp)	# load value in -4($fp): j to $t1
	sw $t1, -8($fp)	# store value in $t1 in -8($sp): k = 1
	
check2:	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	ble $t0, $0, increment1	# while $t0 > 0: # while (k > 0):
	
	# Get the_list[k-1] value
	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: k - 1
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 to $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 to $t3
	lw $t4, ($t3)	# load value in the address in $t3: address of (k - 1) position of the array to $t4
	
	# Get the_list[k] value
	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t5	# move value from lo register to $t5
	add $t5, $t5, $t2	# store the value $t5+$t2 to $t5
	add $t5, $t5, $t1	# store the value $t5+$t1 to $t5
	lw $t6, ($t5)	# load value in the address in $t5: address of k position of the array to $t6
	
	ble $t4, $t6, increment1	# while (the_list[k - 1] > the_list[k]):
	
	# Get the_list[k-1] value
	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: k - 1
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 to $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 to $t3
	lw $t4, ($t3)	# load value in the address in $t3: address of (k - 1) position of the array to $t4
	
	# Get the_list[k] value
	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t5	# move value from lo register to $t5
	add $t5, $t5, $t2	# store the value $t5+$t2 to $t5
	add $t5, $t5, $t1	# store the value $t5+$t1 to $t5
	lw $t6, ($t5)	# load value in the address in $t5: address of k position of the array to $t6
	
	# Swap
	sw $t6, ($t3)	# store the value in $t6 in the address in $t3: address of (k - 1) position of the array
	sw $t4, ($t5)	# store the value in $t4 in the address in $t5: address of k position of the array
	
	lw $t0, -8($fp)	# load value in -8($fp): k to $t0
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: k -= 1
	sw $t0, -8($fp)	# store the value in $t0 in -8($fp)
	
	j check2	# jump to check2
	
increment1:
	lw $t0, -4($fp)	# load value in -4($fp): j to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: j += 1
	sw $t0, -4($fp)	# store the value in $t0 in -4($fp)
	
	j check1	# jump to check1
	
return1:addi $sp, $sp, 8	# store the value $sp+8 in $sp
	lw $fp, 0($sp)	# load value in 0($sp) to $fp
	lw $ra, 4($sp)	# load value in 4($sp) to $ra
	addi $sp, $sp, 8	# store the value $sp+8 in $sp
	jr $ra	# jump and return to $ra
	# Function ends
	
	# Function begins
counter:	
	# Allocate and save fp and ra
	addi $sp, $sp, -8	# store the value $sp-8 in $sp
	sw $fp, 0($sp)	# store address of $fp in 0($sp)
	sw $ra, 4($sp)	# store address in $ra in 4($sp)
	move $fp, $sp	# copies $sp to $fp
	
	# Allocate for local variables
	addi $sp, $sp, -8	# store the value $sp-8 in $sp
	li $t0, 1	# load 1 to $t0
	sw $t0, -4($fp)	# store value in $t0 in -4($sp): l = 1
	li $t0, 1	# load 1 to $t0
	sw $t0, -8($fp) # store value in $t0 in -8($sp): count = 1
	
check3:
	# Check
	lw $t0, the_list	# load value in variable the_list to $t0: address of the first postion of the array
	lw $t1, ($t0)	# load the value in the address in $t0: address of the first postion of the array to $t1
	lw $t2, -4($fp)		# load value in -4($fp): l to $t2
	bge $t2, $t1, return2	# while $t2 < $t1: # while l < (len(list)):
	
	# Get the_list[l - 1] value
	lw $t0, -4($fp)	# load value in -4($fp): l to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: l - 1
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 in $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 in $t3
	lw $t4, ($t3)	# load value in the address in $t3: address of (l - 1) position of the array to $t4
	
	# Get the_list[l] value
	lw $t0, -4($fp)	# load value in -4($fp): l to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t5	# move value from lo register to $t5
	add $t5, $t5, $t2	# store the value $t5+$t2 in $t5
	add $t5, $t5, $t1	# store the value $t5+$t1 in $t5
	lw $t6, ($t5)	# load value in the address in $t5: address of l position of the array to $t4
	
	bne $t4, $t6, print	# if the_list[l - 1] == the_list[l]:
	
	# Increase count
	lw $t0, -8($fp)	# load value in -8($fp): count to $t0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: count += 1
	sw $t0, -8($fp)	# store the value in $t0 in -8($fp)
	
	j check3	# jump to check3
	
print:	li $v0, 1	# set $v0: 1 to print integer
	lw $t0, -4($fp)	# load value in -8($fp): l to $t0
	subi $t0, $t0, 1	# store the value $t0-1 in $t0: l - 1
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t3	# move value from lo register to $t3
	add $t3, $t3, $t2	# store the value $t3+$t2 in $t3
	add $t3, $t3, $t1	# store the value $t3+$t1 in $t3
	lw $a0, ($t3)	# load value in the address in $t3: address of (l - 1) position of the array to $a0
	syscall
	
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str1	# set $a0 to address of the first character of the string
	syscall
	
	li $v0, 1	# set $v0: 1 to print integer
	lw $a0, -8($fp)	# load value in -8($fp): count to $a0
	syscall
	
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str2	# set $a0 to address of the first character of the string
	syscall
	
	li $t0, 1	# load 1 to $t0
	sw $t0, -8($fp)	# store the value in $t0 in -8($fp)
	
check3:	lw $t0, -4($fp)	# load value in -4($fp): l to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	lw $t2, ($t1)	# load value in the address in $t1: address of the first postion of the array to $t2
	subi $t2, $t2, 1	# store the value $t2-1 in $t2	
	bne $t0, $t2, increment2	# if $t0 == $t1: # if l == (size - 1):

	li $v0, 1	# set $v0: 1 to print integer
	lw $t0, -4($fp)	# load value in -4($fp): l to $t0
	lw $t1, the_list	# load value in variable the_list to $t1: address of the first postion of the array
	li $t2, 4	# load 4 to $t2
	mult $t0, $t2	# $t0*$t2
	mflo $t5	# move value from lo register to $t5
	add $t5, $t5, $t2	# store the value $t5+$t2 in $t5	
	add $t5, $t5, $t1	# store the value $t5+$t1 in $t5
	lw $a0, ($t5)	# load value in the address in $t5: address of l position of the array to $a0
	syscall
	
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str1	# set $a0 to address of the first character of the string
	syscall
	
	li $v0, 1	# set $v0: 1 to print integer
	lw $a0, -8($fp)	# load value in -8($fp): count to $a0
	syscall
	
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str2	# set $a0 to address of the first character of the string
	syscall
	
increment2:
	lw $t0, -4($fp)	# load value in -4($fp): l to $a0
	addi $t0, $t0, 1	# store the value $t0+1 in $t0: l += 1
	sw $t0, -4($fp)	# store the value in $t0 in -4($fp)
	
	j computation	# jump to computation
	
return2:addi $sp, $sp, 8	# store the value $sp+8 in $sp
	lw $fp, 0($sp)	# load value in 0($sp) to $fp
	lw $ra, 4($sp)	# load value in 4($sp) to $ra
	addi $sp, $sp, 8	# store the value $sp+8 in $sp
	jr $ra	# jump and return to $ra
	# Function ends
	
main:	# Prompt user
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
	blt $t0, $t1, input	# while $t0 < $t1:  while i < size:
	jal insertionSort	# jump and link to insertionSort
	jal counter	# jump and link to counter
	j end	# jump to end
	
input:	# Prompt user
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
	
end:	# End program
	li $v0, 10	# set $v0: 10 to end program
	syscall
