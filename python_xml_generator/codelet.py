##test code

f = open('sample_data.csv','r')
lines=f.readlines()
print lines[0][2]
#just some sample print statements to check if everyhting's printing properly
print lines[1]
print lines[2]
print lines[3]
#print the root element Cell
print ('\x1b[5;30;43m' + "<Cell>" + '\x1b[0m')

#tag name
print ('\x1b[6;30;41m' + "<name>" + '\x1b[0m')
#print content
print (lines[1][:4])
#end tag name
print ('\x1b[6;30;41m' + "</name>" + '\x1b[0m')

#tag parent
print ('\x1b[5;30;42m' + "<parent>" + '\x1b[0m')
#print content
print (lines[1][6:8])
#end tag parent
print ('\x1b[5;30;42m' + "</parent>" + '\x1b[0m')

#tag lineage
print ('\x1b[5;30;46m' + "<lineage>" + '\x1b[0m')
#print content
print (lines[1][9:18])
#end tag lineage
print ('\x1b[5;30;46m' + "</lineage>" + '\x1b[0m')

#tag description
print ('\x1b[5;30;47m' + "<description>" + '\x1b[0m')
#print content
print (lines[1][21:54])
#end tag description
print ('\x1b[5;30;47m' + "</description>" + '\x1b[0m')

#close the root element /Cell
print ('\x1b[5;30;43m' + "</Cell>" + '\x1b[0m')

#print ('\x1b[6;30;41m' + "<name>" + '\x1b[0m' + lines[1][1] + '\x1b[6;30;41m' + "</name>" + '\x1b[0m')

