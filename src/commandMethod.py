from subcommandMethod import *
from helper import *

def addCommand(subCommandType, courses):
	subCommand = {
		"course": addCourse,
		"assessment": addAssessment,
		"grade": addGrade,
		"help": addHelp,
		"-h": addHelp,
	}
	addSubCommand = subCommand.get(subCommandType, noSuchSubCommand)
	addSubCommand(courses)

def removeCommand(subCommandType, courses):
	subCommand = {
		"course": removeCourse,
		"assessment": removeAssessment,
		"help": removeHelp,
		"-h": removeHelp,
	}
	removeSubCommand = subCommand.get(subCommandType, noSuchSubCommand)
	removeSubCommand(courses)

def getCommand(subCommandType, courses):
	subCommand = {
		"finalGPA": getFinalGPA,
		"currentGPA": getCurrentGPA,
		"neededGPA": getNeededGPA,
		"help": getHelp,
		"-h": getHelp
	}
	getSubCommand = subCommand.get(subCommandType, noSuchSubCommand)
	getSubCommand(courses)