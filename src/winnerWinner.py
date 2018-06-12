#!/usr/bin/env python3

import json



def getJSON(users, skills):
		# Read JSON file
	with open('../grades.json') as data_file:
		data_loaded = json.load(data_file)

	skills = []
	users = []
	
   # Print formatted JSON
   # print(json.dumps(data_loaded, sort_keys = True, indent = 4))
   
   # Parse each value
	for name in data_loaded:
		users.append(name)
		for language in data_loaded[name]:
			skills.append(language)
	print(skills)		
	
	yield users, skills

def formObjectiveComparison():
	return False
	
def normalizeObjectives():
	return False
	
def calcObjectWeight():
	return False
	
def convertCaliber():
	return False
	
def createPairwise():
	return False
	
def normalizePairwise():
	return False
	
def calcScores():
	return False
	
def sortUsers():
	return False
	



def main():
	skills = []
	users  = []

	#getJSON(users, skills)
	
	
	
		# Read JSON file
	with open('../grades/potter.json') as data_file:
		data_loaded = json.load(data_file)

	skills = []
	users = []
	
   # Print formatted JSON
   # print(json.dumps(data_loaded, sort_keys = True, indent = 4))
   
   # Parse each value
	for name in data_loaded:
		users.append(name)
		for language in data_loaded[name]:
			skills.append(language)
	
	skillsSet = set(skills)
	print(users)
	print(skills)
	print(skillsSet)
	

	
	






if __name__ == '__main__':
	main()