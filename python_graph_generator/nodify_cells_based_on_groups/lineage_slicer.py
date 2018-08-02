##initialize first file to be read(r) and other two to write(w+)

rf = open('f_gephi_lineage_name.txt','r')
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
