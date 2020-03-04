from helper import * 

print ("Welcome to GPAMotivator!\n")

courses = []

while True:
	user_input = input("\nEnter your message (enter to exit): ")
	if user_input == "":
		break
	else:
		print("You entered: {}".format(user_input))
		inputs = user_input.split( )

		if len(inputs) == 2:
			if inputs[0] == "add":
				if inputs[1] == "course":
					course_name = input("Course name: ")
					course_target_gpa = input("Course target GPA: ")

					addCourseToList(courses, course_name, course_target_gpa)

					print("\nCourse added! You current courses are: ")
					printCoursesList(courses)

				elif inputs[1] == "assessment":
					assess_name = input("Assessment name: ")
					assess_portion = input("Assessment portion: ")
					course_to_add = input("Add to course: ")

					course = findCourseFromList(courses, course_to_add)
					addAssessmentToCourse(course, assess_name, assess_portion)

					print("\nAssessment added! You current courses are: ")
					printCoursesList(courses, True)

				elif inputs[1] == "grade":
					grade = input("Grade is: ")
					assess_to_add = input("Add to which assessment: ")
					course_to_add = input("Under which course: ")

					course = findCourseFromList(courses, course_to_add)
					addGradeToAssessment(course, assess_to_add, grade)

					print("\nGrade added! You current courses are: ")
					printCoursesList(courses, True)

			elif inputs[0] == "remove":
				if inputs[1] == "course":
					course_to_remove = input("Name of course to be removed: ")

					removeCourseFromList(courses, course_to_remove)

					print("\nCourse removed! You current courses are: ")
					printCoursesList(courses)

				elif inputs[1] == "assessment":
					assess_to_remove = input("Name of assessment to be removed: ")
					belonged_course_name = input("Under which course: ")

					removeAssesssmentFromCourse(courses, belonged_course_name, assess_to_remove)

					print("\nAssessment removed! You current courses are: ")
					printCoursesList(courses, True)

			elif inputs[0] == "get":
				if inputs[1] == "finalGPA":
					course_name = input("Which course: ")

					course = findCourseFromList(courses, course_name)
					final_gpa = getFinalGPAFromCourse(course)

					print("Your final GPA is {}".format(final_gpa))

				elif inputs[1] == "currentGPA":
					course_name = input("Which course: ")

					course = findCourseFromList(courses, course_name)
					final_gpa = getCurrentGPAFromCourse(course)

					print("Your curretn GPA is {}".format(final_gpa))

				elif inputs[1] == "neededGPA":
					course_name = input("Which course: ")

					course = findCourseFromList(courses, course_name)
					final_gpa = getNeededGPAFromCourse(course)

					print("Your needed GPA is {}".format(final_gpa))