class Assessment:
	def __init__(self, name, portion):
		self.name = name
		self.portion = portion
		self.grade = -1

	def addGrade(self, grade):
		self.grade = grade
	
	def hasGrade(self):
		return self.grade != -1

	def calculateGradeToFinal(self):
		return float(self.portion) * float(self.grade)