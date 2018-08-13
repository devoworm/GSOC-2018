echo "Welcome to the master script that runs the entire project"

python feature_display.py

: 'python python_common_path/py.py

if [ "$1" == "alphabet" ]; then				#$1 refers to the first argument of the command
	python code.py alphabet > res.txt		#this passes the argument to the URL constructor in python
	bash res.txt
elif [ "$1" == "one" ]; then
	python code.py one > res.txt
	bash res.txt
elif [ "$1" == "two" ]; then
	python code.py two > res.txt
	bash res.txt
else
	echo "Sorry, this does not exist in our database"	#default error statement in case of erroneous input
fi
'
