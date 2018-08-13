##initialize first file to be read(r) and other two to write(w+)

rf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_name.txt','r')
of = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_1.txt','w+')
sf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_lineage_2.txt','w+')
line_lu=rf.readlines()


##traverse through input file to find shortest length lineage
count = 0
low_count = 100
high_count = 0
for loop_var in range ( 0 , int( len(line_lu) ) ) :
    count = int(len(line_lu[loop_var]))
    if count < low_count :
        low_count = count
    if count > high_count :
        high_count = count

print "Lowest count = " + str(low_count) + ". Highest count = " + str(high_count)


##for now, assuming lineage lenght is around 7 to 8 generations, for now slice into 3 events. After 1st, after (r/2)th and last
##accrodingly the two raios are decided
r1 = 2
r2 = (low_count / 2) - 1

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
    print str(i+1) + ". Length after first 3 :- " + str(j) + ". After /" + str(r1) + " = " + str(j2) + ". After /" + str(r2) + " = " + str(j3)
    print line_lu[i][0:len(line_lu[i])-1]
    #print second one /r1 and write in 1st lineage
    t1 =  line_lu[i][0:(3+j2)]
    print t1
    of.write( t1 + "\n" )
    #print third one /r2 and write in 2nd lineage
    t2 =  line_lu[i][0:(3+j3)]
    print t2  + "\n"
    sf.write( t2 + "\n" )
