##Print the available features
print "The following features are available :"
print "_______________________________________"
print "1. Common Ancestor Detector"
print "2. Cross generation query responder"
print "3. Wildcard Query for lineage"
print "4. Exploratory search"
print "5. XML Generator"
print "6. GML tree generator"
print "7. GML cell group generator"

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
elif choice == "4" :
    print "Exploratory Search Module will run"
    print "_______________________________________\n"
    execfile("python_query_respond/explore/exploratory.py")
elif choice == "5" :
    print "XML Generator will run"
    print "_______________________________________\n"
    execfile("python_xml_generator/codelet.py")
elif choice == "6" :
    print "GML tree generator will run"
    print "_______________________________________\n"
    execfile("python_graph_generator/gml_gen.py")
elif choice == "7" :
    print "GML cell group generator will run"
    print "_______________________________________\n"
    execfile("python_graph_generator/nodify_cells_based_on_groups/user_enters_group_of_cells_to_be_analysed.py")
else :
    print "Doesn't exist"
