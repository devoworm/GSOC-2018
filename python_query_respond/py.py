##test code

### master list that will track the order in which cells were visited
my_list = [""]

##code for generating lookup table
lf = open('lookup_for_parent_daughter_cells.csv','r')
line_lu=lf.readlines()
comma1_found = 0
comma2_found = 0
comma3_found = 0
comma4_found = 0
comma1_found_dc = 0
comma2_found_dc = 0

##code for generating lookup table ends here ______________________________

f = open('test_in_csv.csv','r')
lines=f.readlines()
a = ''
#define string and a list to help in character assignment
myArray = "\0" * 200
listify = list(myArray)

first_time_use_variable = 1
line_no = 0

loop_variable = 1
while loop_variable == 1 :


	if first_time_use_variable != 1 :
	    print("The current line no. being analysed is: " + str(line_no))
	    print("Would you like to analyse a daughter/parent cell of the current cell? Press 1 for daughter; 0 for starting fresh and 2 for parent cell")
	    choice_of_loop = raw_input()
	    
	    if int(choice_of_loop) == 0 :
	    	print("it has reached")
	    	##input which line to analyse
		print("Enter the line that you want to analyse")
		line_no = raw_input()
	
		##enter till which index to analyse
		print("Enter the length limit that you want to analyse")
		index_no = raw_input()

	    elif int(choice_of_loop) == 2 :
	    	print("user wants to analyse parent cell of current cell")
	    	
	    	for lvx in range(1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma1_found = lvx
		        break
		for lvx in range(comma1_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma2_found = lvx
		        break
		for lvx in range(comma2_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma3_found = lvx
		        break
		for lvx in range(comma3_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma4_found = lvx
		        break
	        print("the current cell that you just analysed was: " + line_lu[int(line_no)][comma1_found+1:comma2_found])
	        if (int(line_no) % 2 == 0) :
	            line_no = int(line_no) / 2
	        else :
	            if (int(line_no) != 1) :
	                line_no = (int(line_no) - 1) / 2
		    else :
		        print ("You've already reached the precursor cell P0")

		print("Enter the length limit that you want to analyse")
		index_no = raw_input()
		
	    else :
	    	for lvx in range(1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma1_found = lvx
		        break
		for lvx in range(comma1_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma2_found = lvx
		        break
		for lvx in range(comma2_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma3_found = lvx
		        break
		for lvx in range(comma3_found+1, 20):
		    if str(line_lu[int(line_no)][lvx]) == "," :
		        comma4_found = lvx
		        break
	        print("the current cell that you just analysed was: " + line_lu[int(line_no)][comma1_found+1:comma2_found])
	        print("the first daughter cell is: " + line_lu[int(line_no)][comma2_found+1:comma3_found])
		print("the second daughter cell is: " + line_lu[int(line_no)][comma3_found+1:comma4_found])
		print("Enter 1 if you want to query for first daughter cell and 2 for second daughter cell")
		dc_choice = raw_input()
		if dc_choice == "1" :
		    #code
		    print("user chose 1st daughter cell which is: " + line_lu[int(line_no)][comma2_found+1:comma3_found])
		    for cur_line_no in range(1,41):
			    for li_v in range(1, 20):
				if str(line_lu[int(cur_line_no)][li_v]) == "," :
				    comma1_found_dc = li_v
				    break
			    for li_v in range(comma1_found_dc+1, 20):
				if str(line_lu[int(cur_line_no)][li_v]) == "," :
				    comma2_found_dc = li_v
				    break
			    print ("in this line the main cell is: " + line_lu[int(cur_line_no)][comma1_found_dc+1:comma2_found_dc])
			    if line_lu[int(cur_line_no)][comma1_found_dc+1:comma2_found_dc] == line_lu[int(line_no)][comma2_found+1:comma3_found] :
			        print "match found"
			        print("the line no. of the said cell is : " + str(cur_line_no))
			        line_no = cur_line_no
			        print("Enter the length limit that you want to analyse")
		                index_no = raw_input()
			        break				    
		    
		else :
		    print("user chose 2nd daughter cell which is: " + line_lu[int(line_no)][comma3_found+1:comma4_found])
		    print("the length of this cell name is: " + str(len(line_lu[int(line_no)][comma3_found+1:comma4_found])))
		    for cur_line_no in range(1,41):
			    for li_v in range(1, 20):
				if str(line_lu[int(cur_line_no)][li_v]) == "," :
				    comma1_found_dc = li_v
				    break
			    for li_v in range(comma1_found_dc+1, 20):
				if str(line_lu[int(cur_line_no)][li_v]) == "," :
				    comma2_found_dc = li_v
				    break
			    print ("in this line the main cell is: " + line_lu[int(cur_line_no)][comma1_found_dc+1:comma2_found_dc])
			    print ("we need to compare this to th: " + line_lu[int(line_no)][comma3_found+1:comma4_found])
			    if str(line_lu[int(cur_line_no)][comma1_found_dc+1:comma2_found_dc]) == str(line_lu[int(line_no)][comma3_found+1:comma4_found]) :
			        print "match found"
			        print("the line no. of the said cell is : " + str(cur_line_no))
			        line_no = cur_line_no
			        print("Enter the length limit that you want to analyse")
		                index_no = raw_input()
			        break
	
	else :
		##input which line to analyse
		print("Enter the line that you want to analyse")
		line_no = raw_input()
	
		##enter till which index to analyse
		print("Enter the length limit that you want to analyse")
		index_no = raw_input()

	##find length of line
	line_len = len(lines[int(line_no)])
	print ("Length of selected line is:- " + str(line_len))

	##to copy the entire queried line into an array that has been converted to a list for ease of operations
	for x in range(0, int(index_no)):
		a = lines[int(line_no)][x]
		listify[x] = a

	##transform list back to string    
	myArray = ''.join(listify)
	count_comma = 0
	comma_indices = [0] * 20
	##finding indices of commas to help decide later the end points of the comma sep. values
	for x in range(0, int(index_no)):
		if str(lines[int(line_no)][x]) == "," :
		    comma_indices[count_comma] = x
		    count_comma += 1
	print(myArray)

	##print parameters about commas
	print ("no. of commas found " + str(count_comma))
	print "their indices are"
	print(comma_indices)

	#append query line number to list
	my_list.append(str(line_no))

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
	first_time_use_variable = 0

print ','.join(my_list)
print "Good bye!"
