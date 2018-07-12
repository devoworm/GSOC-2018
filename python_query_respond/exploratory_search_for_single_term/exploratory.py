lf = open('all_cells.csv','r')
line_lu=lf.readlines()

com = 0
com2 = 0
st = ""
len_st = 0
line_no = 0

print "Enter search term"
search = raw_input()

for i in range ( 0 , int(len(line_lu)) ) :
    for j in range ( 0 , 17 ) :
        if str(line_lu[i][j]) == ':' :
            com = j
            break
	
	st = str(line_lu[i][0:com])
	len_st = len(st)
	
	for z in range ( 1 , len_st + 1 ) :
	    if search == st[0:j] :
	        print str(i) + " " + line_lu[i]
	        break
