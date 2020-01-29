# TeacherAI
# Parsing file


import os, json, re
import unicodedata 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize 

with open('tai-documents-v3.json') as my_file:
    document = json.load(my_file)

my_file.close()


paragraphs = []
for data in document:
    plain_text = data['plaintext']
    plain_text = unicodedata.normalize('NFKD', plain_text).encode('ascii', 'ignore')
    plain_text = plain_text.replace('\r\n', ' ')
    plain_text = plain_text.replace('\t', ' ')
    plain_text = plain_text.replace('\'', "")
    paragraphs.append(plain_text)

print(paragraphs[1:2])

