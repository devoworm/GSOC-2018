##test code

f = open('embryogenesis_datasets/cell-by-cell-data-v2.csv','r')
wf = open('python_xml_generator/output.xml','w+')
lines=f.readlines()

wf.write("<MasterDocument>"+"\n")

print "Welcome to XML generator. Please select the options carefully"
print "\n1. Generate .xml file for cells in a specific range"
print "\n2. Do the above plus echo the .xml structure for cells in a specific range on terminal itself"
choice = 0
choice = raw_input()

if int(choice) < 10 :
	colon1 = 0
	colon2 = 0
	par_ind = 0
	
	print "Enter first index starting in range 1 to 1000"
	first_index = raw_input()
	
	print "Enter second index less than 1300"
	second_index = raw_input()
	
	print "What value of indentation do you want for every layer of tab? In case you hate tabs, what number of spaces do you want ;)"
	tabs = raw_input()
	s = ""
	
	for i in range ( 0 , int(tabs) ):
	    s = s + " "

	for i in range ( int(first_index) , int(second_index) ) :
		for j in range ( 0 , 10 ) :
		    if lines[i][j] == ":" :
		        colon1 = j
		        break
		    
		for j in range ( colon1 + 1 , colon1 + 30 ) :
		    if lines[i][j] == ":" :
		        colon2 = j
		        break
		
		par_ind = colon1
		for j in range ( colon1 , colon2 ) :
		    if lines[i][j] == ".":
		        par_ind = j
		        break
		    if lines[i][j] == " ":
		        par_ind = j
		        break
		
		name = lines[i][:colon1]
		parent = lines[i][colon1+1:par_ind]
		lineage = lines[i][par_ind+1:colon2]
		description = lines[i][colon2+1:int(len(lines[i]))-1]
		
		wf.write(("%s<Cell>" % s)+"\n")
		wf.write(("%s%s<Name>" % (s,s)))
		wf.write(name)
		wf.write(("</Name>")+"\n")
		wf.write(("%s%s<Parent>" % (s,s)))
		wf.write(parent)
		wf.write(("</Parent>")+"\n")
		wf.write(("%s%s<Lineage>" % (s,s)))
		wf.write(lineage)
		wf.write(("</Lineage>")+"\n")
		wf.write(("%s%s<Description>" % (s,s)))
		wf.write(description)
		wf.write(("</Description>")+"\n")
		wf.write(("%s</Cell>" % s )+"\n")
		
		if int(choice) == 2 :
			print ('\x1b[5;30;43m' + "<Cell>" + '\x1b[0m')
			print ('\x1b[6;30;41m' + "<name>" + '\x1b[0m' + name + '\x1b[6;30;41m' + "</name>" + '\x1b[0m')
			print ('\x1b[5;30;42m' + "<parent>" + '\x1b[0m' + parent + '\x1b[5;30;42m' + "</parent>" + '\x1b[0m')
			print ('\x1b[5;30;46m' + "<lineage>" + '\x1b[0m' + lineage +'\x1b[5;30;46m' + "</lineage>" + '\x1b[0m')
			print ('\x1b[5;30;47m' + "<description>" + '\x1b[0m' + description  + '\x1b[5;30;47m' + "</description>" + '\x1b[0m')
			print ('\x1b[5;30;43m' + "</Cell>" + '\x1b[0m')

wf.write("</MasterDocument>"+"\n")
