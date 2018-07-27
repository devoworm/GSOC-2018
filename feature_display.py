##Print the available features
print "The following features are available :"
print "_______________________________________"
print "1. Common Ancestor Detector"
print "2. Query Responder"
print "3. Wildcard Query for lineage"

##Takes user's input to decide which script to run
print "\nEnter which feature you want to use?"
choice = ""
choice = raw_input()

if choice == "1" :
    print "Common Ancestor Module will run"
    print "_______________________________________\n"
    execfile("python_common_path/py.py")
elif choice == "2" :
    print "Query Responder will run"
    print "_______________________________________\n"
    execfile("python_query_respond/py.py")
elif choice == "3" :
    print "Wildcard Query Search Module will run"
    print "_______________________________________\n"
    execfile("python_query_respond/wildcard_query.py")
else :
    print "Doesn't exist"
