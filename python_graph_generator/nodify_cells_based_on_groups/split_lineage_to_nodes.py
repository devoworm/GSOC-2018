lf = open('lineage_name.txt','r')
wf = open('for_gephi.gml','w+')
line_lu=lf.readlines()
master_list = []

print "No. of lineages present :" + str(len(line_lu)) + "\n"

for var in range (len(line_lu)):
	s = line_lu[var][0:int(len(line_lu[var])-1)]
	list_of_nodes = []

	length = len(s)

	print "____________/  ----------- \____________"
	print "Length of lineage : " + str(length)
	print "The lineage is : " + s

	does_space_exist = 0

	for i in range (1,length) :
		if s[i] == ' ':
		    does_space_exist = i

	print "Does space exist?"
	if does_space_exist == 0 :
		print "No"
	else :
		print "Yes, at index no. " + str(does_space_exist)

	if does_space_exist > 0 :
		list_of_nodes.append(s[0:does_space_exist])
		for i in range ( 1,length - (does_space_exist) ) :
		    list_of_nodes.append( s[0:does_space_exist] + s[does_space_exist+1:does_space_exist+1+i] )
	else :
		print "\nError in input format"

	master_list = master_list + list_of_nodes
	print list_of_nodes
	print "\n"

master_list = list(set(master_list))
master_list.sort()
print master_list

for i in range (0,len(master_list)) :
    wf.write(master_list[i] + "\n")
