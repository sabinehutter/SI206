# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk
import random
from nltk.book import *
from nltk.corpus import gutenberg
from nltk import word_tokenize,sent_tokenize


tagged_tokens = nltk.pos_tag(text2) # gives us a tagged list of tuples

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1, "RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

def new_spaced(list2):
	for words in list2:
		if words in [",", ".", "?", "!", ":"]:
			return words
		else:
			return " " + words
orig = []
final_words = []
print ("ORIGINAL TEXT")
s = tagged_tokens[:150]
for tup in s:
	orig.append(tup[0])
orig2 = new_spaced(orig)
print (orig2)

print("\n")
for (word, tag) in s:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


print("\n")
print("NEW TEXT")
print("\n")
print ("".join(final_words))

print("\n\nEND*******")

