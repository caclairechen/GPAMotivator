from course import Course
from assessment import Assessment

print ("Welcome to GPAMotivator!\n")

courses = []

while True:
	user_input = input("\nEnter your message (enter to exit): ")
	if user_input == "":
		break
	else:
		print("You entered: "+user_input)
		inputs = user_input.split( )

		if len(inputs) == 2:
			if inputs[0] == "add":
				if inputs[1] == "course":
					course_name = input("Course name: ")
					course_target_gpa = input("Course target GPA: ")
					new_course = Course(course_name, course_target_gpa)
					courses.append(new_course)

					print("\nCourse added! You current courses are: ")
					for course in courses:
						print(course.name+" "+course.target_gpa)

				elif inputs[1] == "assessment":
					assess_name = input("Assessment name: ")
					assess_portion = input("Assessment portion: ")
					new_assess = Assessment(assess_name, assess_portion)

					course_to_add = input("Add to course: ")
					for course in courses:
						if course.name == course_to_add:
							course.addAssessment(new_assess)

					print("\nAssessment added! You current courses are: ")
					for course in courses:
						print(course.name+" "+course.target_gpa)
						for assess in course.assessments:
							print("\t"+assess.name+" "+assess.portion)

			elif inputs[0] == "remove":
				if inputs[1] == "course":
					course_to_remove = input("Name of course to be removed: ")
					for course in courses:
						if course.name == course_to_remove:
							courses.remove(course)
					print("\nCourse removed! You current courses are: ")
					for course in courses:
						print(course.name+" "+course.target_gpa)

				elif inputs[1] == "assessment":
					assess_to_remove = input("Name of assessment to be removed: ")
					belonged_course = input("Under which course: ")

					for course in courses:
						if course.name == belonged_course:
							course.removeAssessment(assess_to_remove)

					print("\nAssessment removed! You current courses are: ")
					for course in courses:
						print(course.name+" "+course.target_gpa)
						for assess in course.assessments:
							print("\t"+assess.name+" "+assess.portion)