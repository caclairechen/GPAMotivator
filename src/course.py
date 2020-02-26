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

	def removeAssessment(self, assess_name):
		for assess in self.assessments:
			if assess.name == assess_name:
				self.assessments.remove(assess)