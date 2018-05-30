##test code


f = open('test_in_csv.csv','r')
lines=f.readlines()
a = ''
#define string and a list to help in character assignment
myArray = "\0" * 200
listify = list(myArray)

loop_variable = 1
while loop_variable == 1 :

	print("Enter the line that you want to analyse")
	line_no = raw_input()
	#just some sample print statements to check if everyhting's printing properly
	#print lines[int(line_no)]

	print("Enter the length limit that you want to analyse")
	index_no = raw_input()


	line_len = len(lines[int(line_no)])
	print ("Length of selected line is:- " + str(line_len))

	for x in range(0, int(index_no)):
		a = lines[int(line_no)][x]
		listify[x] = a

	##transform list back to string    
	myArray = ''.join(listify)
	count_comma = 0
	comma_indices = [0] * 20
	for x in range(0, int(index_no)):
		if str(lines[int(line_no)][x]) == "," :
		    comma_indices[count_comma] = x
		    count_comma += 1
	print(myArray)

	print ("no. of commas found " + str(count_comma))
	print "their indices are"
	print(comma_indices)

	var = 0
	first_index = 0
	second_index = comma_indices[var]
	for x in range(0, count_comma):
		if x == 1 :
		    print ('\x1b[5;30;43m' + "Parent Cell and it's parameters:" + '\x1b[0m')
		if x == 5 :
		    print ('\x1b[5;30;43m' + "Daughter Cell 1 and it's parameters:" + '\x1b[0m')
		if x == 9 :
		    print ('\x1b[5;30;43m' + "Daughter Cell 2 and it's parameters:" + '\x1b[0m')
		if x == 13 :
		    print ('\x1b[5;30;43m' + "Miscellaneous info:" + '\x1b[0m')
		print (myArray[first_index:second_index])
		var += 1
		first_index = second_index + 1
		second_index = comma_indices[var]

	##defining macros for table headers


	"""parent_cell = 1
	x_pc = 2
	y_pc = 3
	z_pc = 4
	daughter_1 = 5
	x_1 = 6
	y_1 = 7
	z_1 = 8
	daughter_2 = 9
	x_2 = 10
	y_2 = 11
	z_2 = 12"""

	print("Enter 1 if you want to keep running")
	loop_variable = raw_input()
	loop_variable = int(loop_variable)

print "Good bye!"
