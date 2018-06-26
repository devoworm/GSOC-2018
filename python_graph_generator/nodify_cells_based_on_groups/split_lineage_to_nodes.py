lf = open('lineage_name.txt','r')
line_lu=lf.readlines()

s = line_lu[0][0:int(len(line_lu[0])-1)]
list_of_nodes = []

length = len(s)

print "Length of lineage : " + str(length)

does_space_exist = 0

for i in range (1,length) :
    if s[i] == ' ':
        does_space_exist = i

print "\nDoes space exist?"
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

print list_of_nodes
