##test code

f = open('test_in_csv.csv','r')
lines=f.readlines()

line_no = raw_input()
#just some sample print statements to check if everyhting's printing properly
#print lines[int(line_no)]

line_len = len(lines[int(line_no)])
print ("Length of selected line is:- " + str(line_len))

#for x in range(0, line_len - 1):
 #   print

##defining macros for table headers

parent_cell = 1
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
z_2 = 12



print ('\x1b[5;30;43m' + "Parent Cell and it's parameters:" + '\x1b[0m')
print ("Name = " + lines[int(line_no)][parent_cell] + lines[int(line_no)][parent_cell+1])

print ('\x1b[5;30;43m' + "Daughter Cell 1 and it's parameters:" + '\x1b[0m')


print ('\x1b[5;30;43m' + "Daughter Cell 2 and it's parameters:" + '\x1b[0m')












#print the root element Cell
#print ('\x1b[5;30;43m' + "<Cell>" + '\x1b[0m')
#close the root element /Cell
#print ('\x1b[5;30;43m' + "</Cell>" + '\x1b[0m')

#print ('\x1b[6;30;41m' + "<name>" + '\x1b[0m' + lines[1][1] + '\x1b[6;30;41m' + "</name>" + '\x1b[0m')
