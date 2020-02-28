from assessment import Assessment

class Course:
	def __init__(self, name, target_gpa):
		self.name = name
		self.target_gpa = target_gpa
		self.assessments = []
		self.final_gpa = 0

	def addAssessment(self, assess_name, assess_portion):
		new_assess = Assessment(assess_name, assess_portion)
		self.assessments.append(new_assess)

	def findAssessment(self, assess_name):
		for assess in self.assessments:
			if assess.name == assess_name:
				return assess

	def removeAssessment(self, assess_name):
		assess = self.findAssessment(assess_name)
		if assess:
			self.assessments.remove(assess)

	def addGradeToAssessment(self, assess_name, grade):
		assess = self.findAssessment(assess_name)
		if assess:
			assess.addGrade(grade)

	def calculateFinalGPA(self):
		for assess in self.assessments:
			self.final_gpa += assess.calculateGradeToFinal()
		return self.final_gpa