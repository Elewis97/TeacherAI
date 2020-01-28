

import os, json

"""
key:  id
key:  plaintext
key:  doctitle
key:  grades

{'version': 1, 'comment': '', 'score': {'total':
"""


checkboxFile, docsFile = "tai-checkboxes-v3.json","tai-documents-v3.json"


with open(docsFile,'r') as myFile:
	data = myFile.read()

obj = json.loads(data)

for row in obj:
	print("\n")
	print("id: ", row['id'])
	print("title: ", row['doctitle'])
	print("plaintext:\n",row['plaintext'])
	grades = row['grades']
	#only printing the latest set for now, should be the best corrections
	gradeSet=grades[-1]
	print("graded version: ",gradeSet['version'])
	print("comment: ",gradeSet['comment'])
	print("score values: ")
	scores, total, average, comments = gradeSet['score']['criteria'], gradeSet['score']['total'], gradeSet['score']['average'], gradeSet['score']['comments']
	print("total score: ",total)
	print("average score: ",average)
	print("criteria scores: ")
	for key, value in scores.items():
		print("\t",key," = ",value)
	print("criteria comments: ")
	for key, value in comments.items():
		print("\t",key," = " ,value)
	markups = gradeSet['markup']
	print("Markups: ")
	for markup in markups:
		print("\n")
		for key, value in markup.items():
			print("\t",key," = ",value)
	checkboxes = gradeSet['checkboxes']
	print("Check Boxes: ",checkboxes['checked'])
	
		
