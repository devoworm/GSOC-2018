lf = open('for_gephi.gml','w+')
lllf = open('for_gephi.txt','r')
line_lu_lllf=lllf.readlines()
targ = ""

lf.write("graph\n[")
s1 = "\n  node\n  [\n    id"
s2 = "\n    label"
for i in range(len(line_lu_lllf)):
    lf.write("%s" % s1)
    lf.write(" %d" % i)
    lf.write("%s" % s2)
    lf.write(" %s" %line_lu_lllf[i])
    lf.write("\n  ]")
    
lf.write("\n")
print"\n"
lf.close()
