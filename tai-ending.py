import sys




# Get text from command line
try:
    with open(sys.argv[1], 'r') as txt:
        essay = txt.read()
    # print (paragraph)
except:
    print ("A text file must be used")
    sys.exit()

# Check if the word conclusion is in the essay. If it is, there is a
# 80% chance that it has a grade of 2.5-3, for this project, we are
# okay with an error of 0.5 st dev

score = 0

if "conclusion" in essay:
    score = 3
else:
    #there is a 70% correlation between the score of the lead and the score of the ending
    # Due to this, if the word conclusion was not included, we will then default to giving
    # the same score as the lead assuming allowing for a 0.5 st dev for error

    #add in the check for lead
    print ("check for lead score here")

print ("Score:", score)