print("Project 3")
print("\n")
print("-------------------------")
print("Part A)")

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
#Sources
#https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
#http://stackoverflow.com/questions/32238616/git-push-fatal-origin-does-not-appear-to-be-a-git-repository-fatal-could-n/32700354
#



# print("START*******")
# import nltk
# import random
# from nltk.book import *
# from nltk.corpus import gutenberg
# from nltk import word_tokenize,sent_tokenize


# tagged_tokens = nltk.pos_tag(text2) # gives us a tagged list of tuples

# tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB":"an adverb"}
# substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1, "RB":.1}

# def spaced(word):
# 	if word in [",", ".", "?", "!", ":"]:
# 		return word
# 	else:
# 		return " " + word

# final_words = []
# s = tagged_tokens[:150]

# for (word, tag) in s:
# 	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
# 		final_words.append(spaced(word))
# 	else:
# 		new_word = input("Please enter %s:\n" % (tagmap[tag]))
# 		final_words.append(spaced(new_word))


# print("\n")
# print("NEW TEXT")
# print("\n")
# print ("".join(final_words))

# def new_spaced(list2):
# 	lst=[]
# 	for words in list2:
# 		if words in [",", ".", "?", "!", ":"]:
# 			lst.append(words)
# 		else:
# 			lst.append(" " + words)
# 	print ("".join(lst))

# orig = []
# print ("\n")
# print ("ORIGINAL TEXT")
# s = tagged_tokens[:150]
# for tup in s:
# 	orig.append(tup[0])
# orig2 = new_spaced(orig)


print("\n\nEND*******")
print("--------------------------")
# print("Part B")

# import requests
# from bs4 import BeautifulSoup

# base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
# r = requests.get(base_url) #requesting information from the colleens website 
# soup = BeautifulSoup(r.text, "html.parser")
# text_word_soup= soup.prettify()
# print (text_word_soup)

print("--------------------------")
# print("Part C")
import tweepy

Consumer_key = "OFo7efosfPpH131PK7YB4nmjn"
#input("Please enter user consumer key: ")
Consumer_secret = "XbUKINvf1um6ZBlsIlsclSBycrrHDLAzLJNQUIMpP7I14UtcDE"
#input("Please enter user comsumer secret: ")
Access_token = "395599302-ULYQLV4AbbogaAN8XhJEQmXWIbuxnD3YVjITrIgr"
#input("Please enter user access token: ")
Access_token_secret = "BJ4vXcXbjvdm8NimvegZhi7i3AfZ21bFVFEaHmHyXavbD"
#input("Please enter user access token secret: ")

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_token_secret)
api_authorization = tweepy.API(auth)
api_authorization.update_status(input("Enter what you would like to tweet: "))

#http://stackoverflow.com/questions/19337672/post-tweet-with-tweepy
#Used code from here

#use open to write an html file
#create our own html file as the last step
#use tweepy



