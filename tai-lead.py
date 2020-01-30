# Tai-lead.py
# Score the lead of an essay, given a text version of the essay an an input on the command line


import nltk
import sys
import string
import operator
import collections
from nltk import FreqDist
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('punkt')


try:
   with open(sys.argv[1], 'r') as txt:
       paragraph = txt.read()
       print (paragraph)
except:
   print ("A text file must be used")
   sys.exit()

text = paragraph

#text = """ 
#Dogs
#Dogs are a great responsibility. "How you ask" Because you need to take care of your dog. I will be telling you things you need to do to have a healthy dog. The subjects I will be talking about are feeding you dog,cleaning up their mess,and playing with your dog.I hope you will like my edvis about being responsible withdogs. 
#
#Cleaning your dog's mess
#When you are cleaning your dog's mess you need things to help you.So I will tell you about what you need you need lots of tools to help you one tool you need is a pooper scooper yes you neet it to clean up your dog's mess. To add on, you also need a pepe pad so they can go pe.Another tool to help is you believe it or not you can potytran your dog with this tool that i just sid the pepe mat and the pooper scooper they can help you potytran your dog.

#Conclusion
#I talked about dogs because not a lot of people know about dogs also oyou need to know how to take care of your dog hope you liked my dog's story or anything.How do you take care of your dog.
#"""

personal_pronouns = ['I', 'we', 'you', 'he', 'she', 'him', 'her', 'we', 'us', 
                     'you', 'they', 'them']

words_tokenized = nltk.tokenize.word_tokenize(text)
words_tokenized = [''.join(c for c in s if c not in string.punctuation) for s in words_tokenized]

stopwords = nltk.corpus.stopwords.words('english')
non_stop = nltk.FreqDist(w.lower for w in words_tokenized if w not in stopwords)

filtered_words = []
for w in words_tokenized:
    if w not in stopwords and len(w) > 0 :
        filtered_words.append(w)


wordDist = FreqDist(filtered_words)
mostCommon = (wordDist).most_common(2)
top_word = []
for i in mostCommon:
    for j in i:
        top_word.append(j)
del top_word[1]
del top_word[2]
top1 = str(top_word[0])
top2 = str(top_word[1])


sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
paragraphs = [p.strip() for p in text.split("\n\n")]

# Only first paragraph, includes title because it splits by new lines
sentences_tokenized = str(sent_tokenizer.tokenize(paragraphs[0]))
words_tokenized = nltk.word_tokenize(sentences_tokenized)

count = 0
words_tokenized = list(words_tokenized)
if words_tokenized.__contains__(top1):  
    count = count + 1
if words_tokenized.__contains__(top2):
    count = count + 1


# Scoring
if count == 0:
    print('Scores for lead is 0')

if count == 1 or count == 2:
    print('Score for lead is 3')

if count >= 4:
    print('Scores for lead is 3.5')











