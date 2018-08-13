##give user choice for final lineage or phase I or phase II
print "Please enter 0 for final; 1 for Phase 1, 2 for phase II"
choi = raw_input()

##Depending on which lineage time-slice user wants to analyse, we will only read from that specific file to create the *.gml file
if int(choi) == 0 :
    print "You chose initial one. So reading file :- lineage_name.txt"
    spl_lf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_name.txt','r')
elif int(choi) == 1 :
    print "You chose Phase I. So reading file :- f_gephi_lineage_1.txt"
    spl_lf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_1.txt','r')
else :
    print "You chose Phase II. So reading file :- f_gephi_lineage_2.txt"
    spl_lf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_2.txt','r')


#spl_lf = open('lineage_name.txt','r')
spl_wf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_nodes.txt','w+')
spl_rf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_edges.txt','w+')
line_lu=spl_lf.readlines()
master_list = []
master_list_with_reps = []
master_list_with_reps = master_list_with_reps + list(str(len(line_lu)))

#A confirmation to check how many lineages present
print "No. of lineages present :" + str(len(line_lu)) + "\n"

#Loop through and for every loop instance, output lineage that was detected
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

        #If the format of input lineage is correct, then we extract it and append to the list_of_nodes
	if does_space_exist > 0 :
		list_of_nodes.append(s[0:does_space_exist])
		for i in range ( 1,length - (does_space_exist) ) :
		    list_of_nodes.append( s[0:does_space_exist] + s[does_space_exist+1:does_space_exist+1+i] )
	else :
		print "\nError in input format"

	master_list = master_list + list_of_nodes
	master_list_with_reps = master_list_with_reps + list(str(var)) + list_of_nodes
	print list_of_nodes
	print "\n"

master_list = list(set(master_list))
master_list.sort()
print "This list is master list without repetitions and sorted\n"
print master_list
print "\nThis is master list in order which will be used to make edge connections in GML file\n"
print master_list_with_reps

##For nodes, we won't allow reps because they cannot overlap.

for i in range (0,len(master_list)) :
    spl_wf.write(master_list[i] + "\n")

for i in range (0,len(master_list_with_reps)) :
    spl_rf.write(master_list_with_reps[i] + "\n")

##Inform about end of operation
print "Now the lineage has been split to nodes and edges. Proceeding with *.gml creation"
print "In local folder, run nodes_to_gml.py to create the gml"
