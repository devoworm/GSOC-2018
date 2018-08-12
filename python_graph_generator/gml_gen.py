##Setting the variables to files. 'lf' is used to write onto the result onto the new file, while lllf is used to read from input file

lf = open('python_graph_generator/aaa.gml','w+')
lllf = open('python_graph_generator/lookup_for_parent_daughter_cells.csv','r')
line_lu_lllf=lllf.readlines()

#used later to store the target line no. when a match is found when we look for a daughter cell
targ = ""

#First, write the basic structure and keep node and label ready in strings to use them in format specifiers later

lf.write("graph\n[")
s1 = "\n  node\n  [\n    id"
s2 = "\n    label"

#iterate in the first 20 elements and for every element find the index no. where the first and second comma appears
for i in range(20):
    lf.write("%s" % s1)
    lf.write(" %d" % i)
    lf.write("%s" % s2)
    for lvx in range(1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma1 = lvx
            break
    for lvx in range(comma1+1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma2 = lvx
            break
    lf.write(" \"%s\"" % line_lu_lllf[i+1][comma1+1:comma2])
    lf.write("\n  ]")

#repeat procedure for creation of the edge connections in *.gml file
for i in range(8):
    for lvx in range(1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma1 = lvx
            break
    for lvx in range(comma1+1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma2 = lvx
            break
    for lvx in range(comma2+1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma3 = lvx
            break
    for lvx in range(comma3+1,15):
        if str(line_lu_lllf[i+1][lvx]) == ",":
            comma4 = lvx
            break
    lf.write("\n  edge")
    lf.write("\n  [\n    source %s" % str(i) )
    
    #pa_cell is the parent cell and d_cell is the daughter cell. When we iterate, we find a match and set "targ = j"
    pa_cell = str(line_lu_lllf[i+1][comma1+1:comma2])
    d_cell1 = str(line_lu_lllf[i+1][comma2+1:comma3])
    
    for j in range(20):
        for va in range(1,15):
            if str(line_lu_lllf[j+1][va]) == ",":
                com1 = va
                break
        for va in range(com1+1,15):
            if str(line_lu_lllf[j+1][va]) == ",":
                com2 = va
                break
        cur_cell = str(line_lu_lllf[j+1][com1+1:com2])
        if (cur_cell == d_cell1) :
            targ = j
            break
            
    lf.write("\n    target %s" % targ)
    
    value = 8
    
    lf.write("\n    value %s" % value)
    lf.write("\n  ]")

lf.write("\n]")
    
lf.close()
#All done, program ends
print "New *.gml file has been created. Please check local folder"
