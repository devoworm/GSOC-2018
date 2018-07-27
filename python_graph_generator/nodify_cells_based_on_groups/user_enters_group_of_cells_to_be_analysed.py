##
my_list = []

start_index = 0
end_index = 0

print ("Four classes of cells are available :-\n")
print ("1. Anterior Deirid\n2. Amphid Neuron\n3. Amphid Interneuron\n4. Pharyngeal\n")

user_choice = raw_input()
user_choice = int(user_choice)

if user_choice == 1 :
    start_index = 1
    end_index = 6
elif user_choice == 2 :
    start_index = 7
    end_index = 10
elif user_choice == 3 :
    start_index = 11
    end_index = 18
elif user_choice == 4 :
    start_index = 19
    end_index = 26
else :
    start_index = 0
    end_index = 0
    
lf = open('python_graph_generator/nodify_cells_based_on_groups/test.csv','r')
line_lu=lf.readlines()

wf = open('python_graph_generator/nodify_cells_based_on_groups/lineage_name.txt','w+')

print "start index = " + str(start_index)
print "end index = " + str(end_index)

for i in range (start_index , end_index + 1) :
    col_1 = 0
    col_2 = 0
    col_3 = 0
    for j in range (0, int(len(line_lu[i]))) :
        if str(line_lu[i][j]) == ":" :
	    col_1 = j
	    break
    for j in range (col_1+1, int(len(line_lu[i]))) :
        if str(line_lu[i][j]) == ":" :
	    col_2 = j
	    break
    for j in range (col_2+1, int(len(line_lu[i]))) :
        if str(line_lu[i][j]) == ":" :
	    col_3 = j
	    break
    print "\nCell name : " + line_lu[i][col_1+1:col_2]
    print ("Lineage : " + line_lu[i][col_2+1:col_3])
    my_list.append(line_lu[i][col_2+1:col_3])
    print ("Description : " + line_lu[i][col_3+1:])
    
    print my_list

print len(my_list)
for i in range (0,len(my_list)) :
    wf.write(my_list[i] + "\n")
    
print "The lineages have been generated. Now they need to be split."

##call split_lineage_to_nodes.py
execfile("python_graph_generator/nodify_cells_based_on_groups/split_lineage_to_nodes.py")
