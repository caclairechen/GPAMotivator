from helper import * 
from commandMethod import *

print ("Welcome to GPAMotivator!\n")

courses = []

while True:
	user_input = input("\nEnter your message (enter to exit): ")
	if user_input == "":
		break
	else:
		inputs = user_input.split( )

		if len(inputs) == 2:
			if inputs[0] == "add":
				addCommand(inputs, courses)
			elif inputs[0] == "remove":
				removeCommand(inputs, courses)
			elif inputs[0] == "get":
				getCommand(inputs, courses)
			

		elif len(inputs) == 1 and (inputs[0] == "help" or inputs[0] == "-h"):
			print("Current support following command: 'add, remove, get', \nmore informaiton, use 'add help' or 'add -h'")

		elif inputs[0] == 'print' or inputs[0] == '-p':
			printCoursesList(courses)
		
		else:
			print("can not understand!!!")

