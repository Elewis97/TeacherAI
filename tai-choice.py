import sys

# Checking for transitions #

# These are words that frequently appear in essays with a score of 3
# If these words are not in the essay, give the essay a score of 2
# Never give a high score, which is rude but there aren't enough essays with
# a score of 3.5 or 4 on transitions to truly gain knowledge. So never giving a 
# 3.5 or 4 will have a high probability of correctness
allTransWords = ['first', 'second', 'also', 'finally', 'in conclusion', 'additon', 'reason', 'next', 'all']

# Get text from command line
try:
    with open(sys.argv[1], 'r') as txt:
        essay = txt.read()
    # print (paragraph)
except:
    print ("A text file must be used")
    sys.exit()


transWords = []
    # linewords = (line.split() for line in (essays[idx].lower().splitlines()))
for line in essay.lower().split("\n"):
    linewords = line.split()
    if len(linewords) > 1:
        transWords.append(" ".join([linewords[0], linewords[1]]))
    elif len(linewords) > 0:
        transWords.append(linewords[0])
hasTransition = False
for words in transWords:
    for tranWord in allTransWords:
        if tranWord in words:
            hasTransition = True

# print(hasTransition)
score = 0
if hasTransition:
    score = 3
else:
    score = 2

print ("Score:", score)