fl = open('../embryogenesis_datasets/cell-by-cell-data-v2.csv','r')
line_fu=fl.readlines()

com = 0
com2 = 0
line_no = 0
first = ""
second = ""
third = ""

print "Enter search term"
search = raw_input()
print "\n\n"


##for every line
#find first colon
#if key = first element, then print

for i in range ( 0 , int(len(line_fu)) ) :
    for j in range ( 0 , 12 ) :
        if str(line_fu[i][j]) == ':' :
            com = j
            break
            
    if search == str(line_fu[i][0:com]) :
        
        flag = 0
        first = ""
        second = ""
        third = ""
        
        for l in range ( 0 , int(len(line_fu[i])) ) :
            if line_fu[i][l] == ':' :
                if flag == 0 :
                    flag = 1
                else :
                    flag = 2
            if flag == 0 :
                first = first + line_fu[i][l]
            elif flag == 1 :
                second = second + line_fu[i][l]
            else :
                third = third + line_fu[i][l]
                
        print "NAME OF CELL : " + first
        print "LINEAGE CELL : " + second[1:]
        print "DESCRIPTION  : " + third[1:]
