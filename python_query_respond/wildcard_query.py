lf = open('lookup_for_parent_daughter_cells.csv','r')
line_lu=lf.readlines()

fl = open('../embryogenesis_datasets/cell-by-cell-data-v2.csv','r')
line_fu=fl.readlines()

com = 0
com2 = 0
line_no = 0

print "Enter search term"
search = raw_input()

for i in range ( 0 , int(len(line_fu)) ) :
    for j in range ( 0 , 12 ) :
        if str(line_fu[i][j]) == ':' :
            com = j
            break
    if search == str(line_fu[i][0:com]) :
        #print line_fu[i]
        line_no = i
        break

for j in range ( com+1 , int(len(line_fu[line_no])) ) :
    if str( line_fu[line_no][j] ) == ':' :
        com2 = j
        break

print "\nFirst-" + line_fu[line_no][0:com] + "\nSecond-" + line_fu[line_no][com:com2] + "\nThird-" + line_fu[line_no][com2+1:]
