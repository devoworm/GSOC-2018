lf = open('all_cells.csv','r')
line_lu=lf.readlines()

com = 0
flag = 0
st = ""
len_st = 0
line_no = 0
stl = 0
match = 0

print "Enter search term"
search = raw_input()

for i in range ( 0 , int(len(line_lu)) ) :
    
    match = 0
    stl = 0
    flag = 0
    
    #find first colon
    for j in range ( 0 , 17 ) :
        if str(line_lu[i][j]) == ':' :
            if ( flag == 0 ) :
                com = j
                flag = 1
    
    #extract string till colon
    st = line_lu[i][0:com]
    
    #print "Line no = " + str(i) + " colon no = " + str(com) + " string = " + st
    #find whether search term is longer or extracted string is longer
    if len(search) > len(st) :
        stl = 1
    
    #if search term is shorter or equal, then only check
    if ( stl == 0 ) :
        if ( search == st[0:len(search)] ) :
            match = 1

    #if there's a match, then output
    if match == 1 :
        print str(i+1) + " " + line_lu[i]

"""for i in range ( 0 , int(len(line_lu)) ) :
    
    if i == 642 :
        print line_lu[i][0:7]
    
    for j in range ( 0 , 17 ) :
        if str(line_lu[i][j]) == ':' :
            com = j
            break
	
	st = str(line_lu[i][0:com])
	len_st = len(st)
	
	for z in range ( 1 , len_st + 1 ) :
	    if search == st[0:j] :
	        print str(i+1) + " " + line_lu[i]
	        break"""
