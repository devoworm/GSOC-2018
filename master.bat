echo "The following features are available :"
echo "_______________________________________"
echo "1. Common Ancestor Detector"
echo "2. Cross generation query responder"
echo "3. Wildcard Query for lineage"
echo "4. Exploratory search"
echo "5. XML Generator"
echo "6. GML tree generator"
echo "7. GML cell group generator"
echo " "
echo "Enter which feature you want to use?"

read varname

if [ "$varname" == "1" ]; then
	echo "Common Ancestor Module will run"
	echo "_______________________________________"
	echo " "
	python python_common_path/py.py
elif [ "$varname" == "2" ]; then
	echo "Query Responder will run"
	echo "_______________________________________"
	echo " "
	python python_query_respond/py.py
elif [ "$varname" == "3" ]; then
	echo "Wildcard Query Search Module will run"
	echo "_______________________________________"
	echo " "
	python python_query_respond/wildcard_query.py
elif [ "$varname" == "4" ]; then
	echo "Exploratory Search Module will run"
	echo "_______________________________________"
	echo " "
	python python_query_respond/explore/exploratory.py
elif [ "$varname" == "5" ]; then
	echo "XML Generator will run"
	echo "_______________________________________"
	echo " "
	python python_xml_generator/codelet.py
elif [ "$varname" == "6" ]; then
	echo "GML tree generator will run"
	echo "_______________________________________"
	echo " "
	python python_graph_generator/gml_gen.py
elif [ "$varname" == "7" ]; then
	echo "GML cell group generator will run"
	echo "_______________________________________"
	echo " "
	python python_graph_generator/nodify_cells_based_on_groups/user_enters_group_of_cells_to_be_analysed.py
	python python_graph_generator/nodify_cells_based_on_groups/lineage_slicer.py
	python python_graph_generator/nodify_cells_based_on_groups/split_lineage_to_nodes.py
	python python_graph_generator/nodify_cells_based_on_groups/nodes_to_gml.py
else
	echo "Sorry, this does not exist in our database"	#default error statement in case of erroneous input
fi
