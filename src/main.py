from commandMethod import *
from helper import printCoursesList

print ("Welcome to GPAMotivator!\n")

courses = []

while True:
	user_input = input("\nEnter your message (enter to exit): ")
	if user_input == "":
		break
	else:
		inputs = user_input.split( )
		if len(inputs) == 2:
			subCommandType = inputs[1]
			if inputs[0] == "add":
				addCommand(subCommandType, courses)
			elif inputs[0] == "remove":
				removeCommand(subCommandType, courses)
			elif inputs[0] == "get":
				getCommand(subCommandType, courses)
			

		elif len(inputs) == 1 and (inputs[0] == "help" or inputs[0] == "-h"):
			print("\nUse 'add course' or 'add assessment' or 'add grade'")
			print("Use 'remove course' or 'remove assessment'")
			print("Use 'get finalGPA' or 'get currentGPA' or 'get neededGPA'")

		elif inputs[0] == 'print' or inputs[0] == '-p':
			printCoursesList(courses)

		else:
			print("can not understand!!!")

