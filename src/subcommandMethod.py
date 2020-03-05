from helper import *

# add subcommand
def addCourse(courses):
	course_name = input("Course name: ")
	course_target_gpa = input("Course target GPA: ")

	addCourseToList(courses, course_name, course_target_gpa)

	print("\nCourse added! You current courses are: ")
	printCoursesList(courses)

def addAssessment(courses):
	assess_name = input("Assessment name: ")
	assess_portion = input("Assessment portion: ")
	course_to_add = input("Add to course: ")

	course = findCourseFromList(courses, course_to_add)
	addAssessmentToCourse(course, assess_name, assess_portion)

	print("\nAssessment added! You current courses are: ")
	printCoursesList(courses, True)

def addGrade(courses):
	grade = input("Grade is: ")
	assess_to_add = input("Add to which assessment: ")
	course_to_add = input("Under which course: ")

	course = findCourseFromList(courses, course_to_add)
	addGradeToAssessment(course, assess_to_add, grade)

	print("\nGrade added! You current courses are: ")
	printCoursesList(courses, True)

def addHelp(courses):
	print("Your current course content is:")
	printCoursesList(courses, True)
	print("\nUse 'add course' or 'add assessment' or 'add grade'")

# remove subcommand

def removeCourse(courses):
	course_to_remove = input("Name of course to be removed: ")

	removeCourseFromList(courses, course_to_remove)

	print("\nCourse removed! You current courses are: ")
	printCoursesList(courses)

def removeAssessment(courses):
	assess_to_remove = input("Name of assessment to be removed: ")
	belonged_course_name = input("Under which course: ")

	removeAssesssmentFromCourse(courses, belonged_course_name, assess_to_remove)

	print("\nAssessment removed! You current courses are: ")
	printCoursesList(courses, True)

def removeHelp(courses):
	print("Your current course content is:")
	printCoursesList(courses, True)
	print("\nUse 'remove course' or 'remove assessment'")

# get subcommand

def getFinalGPA(courses):
	course_name = input("Which course: ")

	course = findCourseFromList(courses, course_name)
	final_gpa = getFinalGPAFromCourse(course)

	print("Your final GPA is {}".format(final_gpa))

def getCurrentGPA(courses):
	course_name = input("Which course: ")

	course = findCourseFromList(courses, course_name)
	final_gpa = getCurrentGPAFromCourse(course)

	print("Your curretn GPA is {}".format(final_gpa))

def getNeededGPA(courses):
	course_name = input("Which course: ")

	course = findCourseFromList(courses, course_name)
	final_gpa = getNeededGPAFromCourse(course)

	print("Your needed GPA is {}".format(final_gpa))

def getHelp(courses):
	print("Your current course content is:")
	printCoursesList(courses, True)
	print("\nUse 'get finalGPA' or 'get currentGPA' or 'get neededGPA'")


# error command
def noSuchSubCommand(courses):
	print("Can not understand!!")