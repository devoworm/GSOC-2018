lf = open('python_graph_generator/curled_lookup_pdc.csv','w+')
lllf = open('python_graph_generator/lookup_for_parent_daughter_cells.csv','r')
line_lu_lllf=lllf.readlines()
le = int(len(line_lu_lllf))

##take first line and print as it is
lf.write(line_lu_lllf[0])

##ask user for number of rotations to make around the file
print "Enter value of curl"
cur = raw_input()

##skip those many lines and start printing after that till end of file
j = int(cur)

for i in range ( j + 1 , le ) :
    print i
    lf.write(line_lu_lllf[i])

print "Done" + str(le)
