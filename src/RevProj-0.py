#!/usr/bin/env python3
import json
'''
Project 0
Authors: Rufor Chen and Taylor Bartley
'''
def main():
    skills = []
    users  = []

    # Read Objective Comparison ranks
    '''
    with open('ranks.json') as data_file:
        ranks = json.load(data_file) # JSON file loaded into 'dict' 
    '''
    # Objective Comparison ranks; placeholder data
    ranks = {
    "Java":9,
    "Angular":4,
    "SOAP":2}
    
    # Read JSON file
    with open('grades.json') as data_file:
        grades = json.load(data_file) # JSON file loaded into 'dict'
    
    # Parse each value
    for name in grades:
        for lang in grades[name]:
            score = grades[name][lang]

    # Generate tables
    createOCT(ranks)    

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
        
if __name__ == '__main__':
    main()
