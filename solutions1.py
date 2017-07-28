############################################
# Programming Challenge 1
# Python: Variables, Conditionals, & Loops
############################################

# 1
# print "Welcome to my world!"
print("Welcome to my world!")


# 2
# print "hey!" 7 times using a for loop
for i in range(7):
	print("hey!")



# 3
# print the numbers 1-10 using a for loop 
for i in range(10):
	print(i+1)


# 4
# print the odd numbers between 20 and 30 using a while loop
i = 20
while i < 30:
	if i%2 == 0:
		print(i+1)
	i += 1


# 5
# write a function that subtracts two numbers (and call the function to test it) 
def subtract(a, b):
	return a-b

ans = subtract(8,3)
print(ans)


# 6
# print all the multiples of 3 between 2 and 34 using a loop
i = 2
while i<=34:
	if i%3 == 0:
		print(i)
	i += 1


# 7
# print the numbers 2-8 in order, ten times using two for loops
for i in range(10):
	for j in range(7):
		print(j+2)


# 8
# write a function that takes in parameters 
def my_function(a, b):
	return (a*a)-(b*b) # difference of squares

ans = my_function(5, 4)
print(ans)


# 9
# print a list of all the numbers that are divisible by 7 that are between 22 and 62
i = 22
while i<62:
	if i%7 == 0:
		print(i)
	i += 1

# 10
# print "yo" 14 times, each time adding one more "o" to "yo" (ex. "yo", "yoo", "yooo"...)
for i in range(14):
	my_str = "yo"
	for j in range(i):
		my_str = my_str + "o"
	print(my_str)


