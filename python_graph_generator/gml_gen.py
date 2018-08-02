lf = open('python_graph_generator/aaa.gml','w+')
lllf = open('python_graph_generator/curled_lookup_pdc.csv','r')
line_lu_lllf=lllf.readlines()
targ = ""

#for i in range(10):
#     lf.write("This is %d\r\n" % (i+1))

lf.write("graph\n[")
s1 = "\n  node\n  [\n    id"
s2 = "\n    label"
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
    #lf.write("\n  [\n    source %s" % (str(i)+str(line_lu_lllf[i+1][comma1+1:comma2])) )
    
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

print "New *.gml file has been created. Please check local folder"
