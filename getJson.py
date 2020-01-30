import os, json, nltk
import unicodedata 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize 
from nltk.corpus import stopwords

"""
key:  id
key:  plaintext
key:  doctitle
key:  grades

{'version': 1, 'comment': '', 'score': {'total':
"""

essays = []
leadGrades = []
transitionGrades = []
endingGrades = []
grades = []

checkboxFile, docsFile = "tai-checkboxes-v3.json","tai-documents-v3.json"


with open(docsFile,'r') as myFile:
	data = myFile.read()

obj = json.loads(data)

for row in obj:
    gs = row['grades']
    txt = row['plaintext']
    # essays.append(txt.splitlines())
    essays.append(txt)
    gradeSet = gs[-1]
    scores = gradeSet['score']
    # print ("criteria scores: ")
    for key, value in scores.items():
        # print ("---", key, "----\n", value, "****\n")
        if key == 'criteria':
            criteria = value
            grades.append(value)
    # print (criteria.items())
    for key, value in criteria.items():
        if key == 'lead':
            leadGrades.append(value)
        elif key == 'transitions':
            transitionGrades.append(value)
        elif key == 'ending':
            endingGrades.append(value)
essayNum = len(leadGrades)
# get all the essays with a grade of 3 ending
withConclusion = 0
withConcAnd3 = 0
ewith3 = 0
ewith2 = 0
ewith25 = 0
ewith35 = 0
ewith4 = 0

with3 = 0
with2 = 0
with25 = 0
with35 = 0
with4 = 0

total2 = 0
total25 = 0
total3 = 0
total35 = 0
total4 = 0

total = 0
bleh = 0
same = 0
under1 = 0

allTransWords = ['first', 'second', 'also', 'finally', 'in conclusion', 'additon', 'reason', 'next', 'all']
# word ['did you', 'do you', ]
#maybe add... um... next and all?????

for idx in range(essayNum - 10):
    transWords = []
    # linewords = (line.split() for line in (essays[idx].lower().splitlines()))
    paragraphNum = len(essays[idx].split("\n"))
    print(paragraphNum)
    for line in essays[idx].lower().splitlines():
        linewords = line.split()
        if len(linewords) > 1:
            transWords.append(" ".join([linewords[0], linewords[1]]))
        elif len(linewords) > 0:
            transWords.append(linewords[0])
    hasTransition = False
    hasYou = False
    for words in transWords:
        for tranWord in allTransWords:
            if tranWord in words:
                hasTransition = True
            if "you" in words:
                hasYou = True

    
    # print(transWords, "\n-------------------\n")
    
    splitEssay = essays[idx].lower().split()
    origLen = len(splitEssay)
    # stopwords = nltk.corpus.stopwords.words('english')
    # essay2 = [w for w in splitEssay if w not in stopwords]
    # englishVocab = set(w.lower() for w in nltk.corpus.words.words())
    # misspelledWords = [w for w in essay2 if w not in englishVocab]

        
    # changedLen = len(essayWOstopwords)
    changedLen = len(set(splitEssay))
    # print (origLen, changedLen, (changedLen / origLen) * 100)
    diffs = (changedLen / origLen) * 100

    if leadGrades[idx] != 0.0 or endingGrades != 0.0:
        bleh = bleh + 1
        if (leadGrades[idx] == endingGrades[idx]):
            same = same + 1
        if (abs(leadGrades[idx] - endingGrades[idx]) < 1):
            under1 = under1 + 1

    if transitionGrades[idx] > 0:
        total = total + 1
    
    if transitionGrades[idx] == 2.0:
        with2 = with2 + 1
        # total2 = total2 + origLen
        if paragraphNum < 8:
            total2 += 1
        # print (with2, origLen, changedLen, (changedLen / origLen) * 100)
        # print (misspelledWords)
        if not hasYou:
            ewith2 = ewith2 + 1
        # print("\n---------------------\n", transWords, "\n---------------------\n")
    if transitionGrades[idx] == 2.5:
        with25 = with25 + 1
        # total25 = total25 + origLen
        if paragraphNum < 8:
            total25 += 1
        if not hasYou:
            ewith25 = ewith25 + 1
    if transitionGrades[idx] == 3.0:
        with3 = with3 + 1
        # total3 = total3 + origLen
        if paragraphNum < 8:
            total3 += 1
        if not hasYou:
            ewith3 = ewith3 + 1
    if transitionGrades[idx] == 3.5:
        with35 = with35 + 1
        # total35 = total35 + origLen
        if paragraphNum < 8:
            total35 += 1
        if not hasYou:
            ewith35 = ewith35 + 1
    if transitionGrades[idx] == 4.0:
        with4 = with4 + 1
        # total4 = total4 + origLen
        if paragraphNum < 8:
            total4 += 1
        if not hasYou:
            ewith4 = ewith4 + 1
    

# print ("with conclusion:", withConclusion, "with a 3:", withConcAnd3)
# print ("percentage is: ", withConcAnd3/withConclusion)
print ("total 2s:", with2, "trans 2s:", ewith2)
print ("total 2.5s:", with25, "trans 2.5s:", ewith25)
print ("total 3s:", with3, "trans 3s:", ewith3)
print ("total 3.5s:", with35, "trans 3.5s:", ewith35)
print ("total 4s:", with4, "trans 4s:", ewith4)


print("total:", total)
print ("2: ", total2)
print ("2.5: ", total25)
print ("3: ", total3)
print ("3.5: ", total35)
print ("4: ", total4)

print ("equal:", ((same / bleh) * 100), "within 1:", (under1 / bleh) * 100)
