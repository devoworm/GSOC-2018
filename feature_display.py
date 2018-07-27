##Print the available features
print "The following features are available :"
print "_______________________________________"
print "1.Common Ancestor Detector"
print "2.Query Responder"

##Takes user's input to decide which script to run
print "\nEnter which feature you want to use?"
choice = ""
choice = raw_input()

if choice == "1" :
    print "Common Ancestor Module will run"
    execfile("python_common_path/py.py")
elif choice == "2" :
    print "no. 2"
    execfile("python_query_respond/py.py")
else :
    print "Doesn't exist"
