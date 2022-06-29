	.data
prompt:	.asciiz "Enter year: "
year:	.word 0
str1:	.asciiz "Is a leap year."
str2:	.asciiz "Is not a leap year."

	.text
	j main # jump to main
	
	# Function begins
is_leap_year:
	# Allocate and save fp and ra
	addi $sp, $sp, -8	# store the value $sp-8 in $sp
	sw $fp, 0($sp)	# store address of $fp in 0($sp)
	sw $ra, 4($sp)	# store address in $ra in 4($sp)
	move $fp, $sp	# copies $sp to $fp
	
	lw $t0, 8($fp)	# load value in 8($fp): year to $t0
	li $t1, 4	# load 4 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t2	# move value from hi register to $t2
	bne $0, $t2, check3	# if $t2 == 0:
	
check2:	lw $t0, 8($fp)	# load value in 8($fp): year to $t0
	li $t1, 100	# load 100 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t2	# move value from hi register to $t2
	beq $0, $t2, check3	# if $t2 != 0:
	li $v0, 0	# load return value 0 to $v0
	lw $fp, 0($sp)	# load value in 0($sp) to $fp
	lw $ra, 4($sp)	# load value in 4($sp) to $ra
	addi $sp, $sp, 8	# store the value $sp+8 in $sp
	jr $ra	# jump and return to $ra
	
check3:	lw $t0, 8($fp)	# load value in 8($fp): year to $t0
	li $t1, 400	# load 400 to $t1
	div $t0, $t1	# $t0/$t1
	mfhi $t2	# move value from hi register to $t2
	bne $0, $t2, false	# if $t2 == 0:
	li $v0, 0	# load return value 0 to $v0
	lw $fp, 0($sp)	# load value in 0($sp) to $fp
	lw $ra, 4($sp)	# load value in 4($sp) to $ra
	addi $sp, $sp, 8	# store the value $sp+8 in $sp
	jr $ra	# jump and return to $ra
	
false:	li $v0, 1	# load return value 1 to $v0
	lw $fp, 0($sp)	# load value in 0($sp) to $fp
	lw $ra, 4($sp)	# load value in 4($sp) to $ra
	addi $sp, $sp, 8	# store the value $sp+8 in $sp
	jr $ra	# jump and return to $ra
	# Function ends
	
main:	# Prompt user
	li $v0, 4	# set $v0: 4 to print string
	la $a0, prompt	# set $a0 to address of the first character of the string
	syscall
	
	# Get user input
	li $v0, 5	# set $v0: 5 to input integer
	syscall
	
	# Store input
	sw $v0, year	# store input value in variable year
	
	# Call function and print
	lw $t0, year	# load value in variable year to $t0
	li $t1, 1582	# load 1582 to $t1
	blt $t0, $t1, main	# if $t0 >= $t1: # if year >= 1582:
	addi $sp, $sp, -4	# store the value $sp-4 to $sp
	lw $t0, year	# load value in variable year to $t0
	sw $t0, 0($sp)	# store the value in $t0 in 0($sp)
	jal is_leap_year	# jump and link to is_leap_year
	
	
	
	move $t0, $v0	# move value $v0 to $t0
	bne $0, $t0, else # if $t0 == 0:
	li $v0, 4	# set $v0: 4 to print string
	la $a0, str1	# set $a0 to address of the first character of the string
	syscall
	
	j end	# jump to end
	
else:	li $v0, 4	# set $v0: 4 to print string
	la $a0, str2	# set $a0 to address of the first character of the string
	syscall
	
end:	li $v0, 10	# set $v0: 10 to end program
	syscall
