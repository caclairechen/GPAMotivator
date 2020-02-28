class Assessment:
	def __init__(self, name, portion):
		self.name = name
		self.portion = portion
		self.grade = 0

	def addGrade(self, grade):
		self.grade = grade

	def calculateGradeToFinal(self):
		return float(float(self.portion) * float(self.grade))