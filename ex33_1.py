# python 2.7
def list_number(number):
	i = 0
	numbers = []

	while  i < number:
		print "At the top i is %d. " %i
		numbers.append(i)

		i  = i + 1
		print "Numbers now: ",numbers
		print "At the bottom i is %d. " %i

	print "The numbers: "

	for num in numbers:
		print num
list_number(10)
