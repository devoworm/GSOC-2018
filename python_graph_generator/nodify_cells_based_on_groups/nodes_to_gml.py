lf = open('for_gephi.gml','w+')
lllf = open('for_gephi_nodes.txt','r')
f3 = open('for_gephi_edges.txt','r')
line_lu_lllf=lllf.readlines()
targ = ""

######defining function for 
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

######write up nodes

lf.write("graph\n[")
s1 = "\n  node\n  [\n    id"
s2 = "\n    label"
for i in range(len(line_lu_lllf)):
    lf.write("%s" % s1)
    lf.write(" %d" % i)
    lf.write("%s" % s2)
    lf.write(" %s" %line_lu_lllf[i])
    lf.write("\n  ]")
    
#######write up edges
line_lu=f3.readlines()
list_of_lines_to_skip = [0]
count = int(line_lu[0])
print "count = " + str(count) + "\nThe line numbers that need to be ignored while creating GML :"

for i in range(1,len(line_lu)):
    a = RepresentsInt(line_lu[i])
    if a == True :
        list_of_lines_to_skip.append(i)

print list_of_lines_to_skip

lf.write("\n")
lf.close()
