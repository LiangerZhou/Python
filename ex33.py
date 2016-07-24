def haha(x, y):
	i = 0
	numbers = []

	#while i < x:
	for i in range(i, x, y):
		print "At the top i is %d" % i
		numbers.append(i)
	
		#i = i + y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	
	print "The numbers: "

	for num in numbers:
		print num
		
haha(9, 2)