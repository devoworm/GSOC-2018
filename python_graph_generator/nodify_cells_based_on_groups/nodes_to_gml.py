ntg_lf = open('python_graph_generator/nodify_cells_based_on_groups/for_gephi.gml','w+')
ntg_lllf = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_nodes.txt','r')
f3 = open('python_graph_generator/nodify_cells_based_on_groups/f_gephi_edges.txt','r')
##python_graph_generator/nodify_cells_based_on_groups/
line_lu_ntg_lllf=ntg_lllf.readlines()
targ = ""
major_break = 0

######defining function for 
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

######write up nodes

ntg_lf.write("graph\n[")
s1 = "\n  node\n  [\n    id"
s2 = "\n    label"
for i in range(len(line_lu_ntg_lllf)):
    ntg_lf.write("%s" % s1)
    ntg_lf.write(" %s" % line_lu_ntg_lllf[i][0:len(line_lu_ntg_lllf[i])-1])
    ntg_lf.write("%s" % s2)
    ntg_lf.write(" %s" %line_lu_ntg_lllf[i])
    ntg_lf.write("  ]")
ntg_lf.write("\n")    


s3 = "\n  edge\n  [\n    source"
s4 = "\n    target"
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

for i in range(len(line_lu)):
    major_break = 0
    #this nested loop is used to skip the lines that need to be skipped because it is present in the skip_list
    for j in range(len(list_of_lines_to_skip)):
        if i == list_of_lines_to_skip[j] :
            major_break = 1
            break
    #this nested loop is used to skip the lines that need to be skipped because the preceding line was in the skip_list
    for j in range(len(list_of_lines_to_skip)):
        if (i-1) == list_of_lines_to_skip[j] :
            major_break = 1
            break
            
    if major_break == 1 :
        print "break point encountered"
    else :
        ntg_lf.write("%s " % s3)
        ntg_lf.write(line_lu[i-1][ 0 : len(line_lu[i-1])-1 ])
        ntg_lf.write("%s " % s4)
        ntg_lf.write(line_lu[i][ 0 : len(line_lu[i])-1 ])
        ntg_lf.write("\n  ]")
        
print "Necessary file has been generated. Please do have a look at README to get started with the most useful layouts that you might need"
ntg_lf.write("\n]")
ntg_lf.close()

print "Now, the *.gml file has been created. Please check local folder"
