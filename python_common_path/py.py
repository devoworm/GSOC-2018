#These 2 variables store the input strings to be compared
str1 = raw_input()
str2 = raw_input()

#These 2 variables store their lenghts respectively
len1 = len(str1)
len2 = len(str2)

print "1st lineage: " + str1 + "  Length: " +str(len1)
print "2nd lineage: " + str2 + "  Length: " +str(len2)

count = 0

#Reason for doing this comparison is to find out which string we need to traverse. The shorter one saves time and memory
if len1 < len2 :
    len2 = len1
else :
    len1 = len2
    
#This just outputs what is the lowest common length irrespective of match or not, to find out till which index we need to compare
print "Common lowest absolute length is: " + str(len1) + "\n\n"

#Simple comparison algorithm
for i in range(len1) :
    if ( str1[i] == str2[i] ) :
        count = count + 1
    else :
        break

#These format specifiers are used to make things look better and in colour on screen
print '\x1b[5;30;43m' + "_________________________________________________________________________" + '\x1b[0m'
print "_________________________________________________________________________"

if count == 0 :
    print '\x1b[5;30;41m' + "CONCLUSION" + '\x1b[0m' + " : The given two lineages have no ancestor node in common"
else :
    print '\x1b[5;30;42m' + "CONCLUSION" + '\x1b[0m' + " : The given two lineages have a common ancestor node : " + '\x1b[5;30;46m' + str1[0:count] + '\x1b[0m'
    print "After the common node, the first  lineage splits in the following direction " + str1[count:]
    print "After the common node, the second lineage splits in the following direction " + str2[count:]
    print "Numbers of characters that are same: " + str(count)

print "_________________________________________________________________________"
print '\x1b[5;30;43m' + "_________________________________________________________________________" + '\x1b[0m'
