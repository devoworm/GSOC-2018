##initialize first file to be read(r) and other two to write(w+)

rf = open('lineage_name.txt','r')
of = open('lineage_1st.txt','w+')
sf = open('lineage_2nd.txt','w+')
line_lu=rf.readlines()

##for now, assuming lineage lenght is around 7 to 8 generations, for now slice into 3 events. After 1st, after 4th and last
##accrodingly the two raios are decided
r1 = 2
r2 = 7

##temporary string
t1 = ""
t2 = ""

##find no. of lineages present in input file
count = len(line_lu)

print "\nNo. of lineages present in input file is :- " + str(count) + "\n"

##loop/traverse through all the lineages and for EVERY lineage create the new lineage
for i in range ( 0 , count ) :
    j = len( line_lu[i] ) - 3 - 1
    j2 = j / r1
    j3 = j / r2
    print str(i+1) + ". Length after first 3 :- " + str(j) + ". After /2 = " + str(j2) + ". After /7 = " + str(j3)
    print line_lu[i][0:len(line_lu[i])-1]
    #print second one /2 and write in 1st lineage
    t1 =  line_lu[i][0:(3+j2)]
    print t1
    of.write( t1 + "\n" )
    #print third one /7 and write in 2nd lineage
    t2 =  line_lu[i][0:(3+j3)]
    print t2  + "\n"
    sf.write( t2 + "\n" )
    
"""wf = open('for_gephi_nodes.txt','w+')
rf = open('for_gephi_edges.txt','w+')
line_lu=lf.readlines()
master_list = []
master_list_with_reps = []
master_list_with_reps = master_list_with_reps + list(str(len(line_lu)))

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
	master_list_with_reps = master_list_with_reps + list(str(var)) + list_of_nodes
	print list_of_nodes
	print "\n"

master_list = list(set(master_list))
master_list.sort()
print "This list is master list without reps and sorted\n"
print master_list
print "\nThis is master list in order which will be used to make edge connections in GML file\n"
print master_list_with_reps

for i in range (0,len(master_list)) :
    wf.write(master_list[i] + "\n")

for i in range (0,len(master_list_with_reps)) :
    rf.write(master_list_with_reps[i] + "\n")"""
