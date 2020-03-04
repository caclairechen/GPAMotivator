from assessment import Assessment

class Course:
	def __init__(self, name, target_percent_gpa):
		self.name = name
		self.target_percent_gpa = target_percent_gpa
		self.assessments = []
		self.final_percent_gpa = 0

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

	def calculateFinalPercentGPA(self):
		for assess in self.assessments:
			self.final_percent_gpa += assess.calculateGradeToFinal()
		return self.final_percent_gpa

	def calculateCurrentPercentGPA(self):
		current_percent_gpa = 0
		current_portion = 0

		for assess in self.assessments:
			if assess.hasGrade():
				current_percent_gpa += assess.calculateGradeToFinal()
				current_portion += float(assess.portion)

		return current_percent_gpa, current_portion

	def percentGPANeededForTarget(self):
		current_percent_gpa, current_portion = self.calculateCurrentPercentGPA()
		percent_needed = (float(self.target_percent_gpa) - float(current_percent_gpa)) / (1 - current_portion)
		return percent_needed

