#an automation for the conventional 
# method of measuring the Stack
#
# Steps :
# 1. create su files for all c files 
#	-> add -fstack-usage to CFLAGS and build, su files will be generated in obj folder
#	-> concatenate all su files to single txt file : 
#		cd obj/
#		cat *.su > su.txt
#	-> use that txt file as first input
# 2. create a call graph using cflow:
#	-> in the main folder :
#		cflow `find . -name *.c` > callstack.txt
# 	-> use that file as second input.
# runnig this script will give the stack depth of every call path, find the largest of it 
# 

import string
d=[]
e=[]
calls = []
with open('su.txt') as f:
	for lines in f:
		c = lines.split(':')[-1]	# remove all text before function name
		d.append(c.split('\t')[0])	# function name
		e.append(c.split('\t')[1])	# stack size

stack_tab = dict(zip(d,e))
# print stack_tab

intend = 0
intend1 = -1
with open('callstack.txt') as log:
	fun=[]
	for lines in log:		
		intend=len(lines) - len(lines.lstrip())
		intend = intend/4
		if(intend1 < intend):
			fun.append(lines.lstrip().split(' ')[0].rstrip().split('()')[0])
			intend1 = intend
		elif intend1 == intend:			
			calls.append(fun[:])
			del fun[-1]
			fun.append(lines.lstrip().split(' ')[0].rstrip().split('()')[0])
			intend1 = intend
		else :
			calls.append(fun[:])
			for i in xrange (intend1, intend-1, -1):				
				del fun[i]
			fun.append(lines.lstrip().split(' ')[0].rstrip().split('()')[0])
			intend1 = intend

maxstack = 0;

for items in calls:
	stack = 0;
	for funcs in items:
		stack = stack + int(stack_tab.get(funcs,0))
	print items 
	print stack 	
			
			
			
			
		