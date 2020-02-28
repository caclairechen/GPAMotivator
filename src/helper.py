from course import Course

def printCoursesList(courses, withAssessments = False):
	for course in courses:
		print("{} {}".format(course.name, course.target_gpa))
		if withAssessments:
			for assess in course.assessments:
				print("\t{} {} {}".format(assess.name, assess.portion, assess.grade))

def findCourseFromList(courses, course_name):
	for course in courses:
		if course.name == course_name:
			return course

def addCourseToList(courses, course_name, course_target_gpa):
	new_course = Course(course_name, course_target_gpa)
	courses.append(new_course)

def removeCourseFromList(courses, course_name):
	course = findCourseFromList(courses, course_name)
	if course:
		courses.remove(course)

def addAssessmentToCourse(course, assess_name, assess_portion):
 	course.addAssessment(assess_name, assess_portion)

def removeAssesssmentFromCourse(courses, course_name, assess_name):
	course = findCourseFromList(courses, course_name)
	if course:
		course.removeAssessment(assess_name)

def addGradeToAssessment(course, assess_name, grade):
	course.addGradeToAssessment(assess_name, grade)

def getFinalGPAFromCourse(course):
	return course.calculateFinalGPA()