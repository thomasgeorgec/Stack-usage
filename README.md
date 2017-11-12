 Steps :
 install cflow 
 
sudo apt-get update
sudo apt-get install cflow

1. create su files for all c files 
 -> add -fstack-usage to CFLAGS and build, su files will be generated in obj folder
 -> concatenate all su files to single txt file : 
 	cd obj/
 	cat *.su > su.txt
-> use that txt file as first input
2. create a call graph using cflow:
-> in the main folder :
	cflow `find . -name *.c` > callstack.txt
	-> use that file as second input.
runnig this script will give the stack depth of every call path, find the largest of it 
