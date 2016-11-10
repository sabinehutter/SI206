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
print("Part B")

import requests
from bs4 import BeautifulSoup

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url) #requesting information from the colleens website 
soup = BeautifulSoup(r.text, "html.parser")
var = soup.prettify()
# for lines in var:
# 	lines.replace('student', 'AMAZING student')
# print(var)

s = []
r = []
for img in soup.findAll("img"):
	# print (img)
	img_tags = img['src']
	if "logo2.png" not in img_tags:
		print(img)
		# print(img['src'].replace('logo2.png', '/Users/sabinehutter/Desktop/206class/rew-repo/SI206/HW3-StudentCopy/media'))
# 	else:
# 		img['src'].replace('logo2.png', '/Users/sabinehutter/Desktop/206class/rew-repo/SI206/HW3-StudentCopy/media')
# print(s)
# print(r)

# html_file = open("beautifulsoup.html", "w")
# html_file.write(var)
# html_file.close()

#logo2.hp
#href


# 
#.fml create html


print('\n')
print("--------------------------")
print("Part C")
# import tweepy
# import requests
# import os

# 


# 	#input("Please enter user access token secret: ")
# auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
# auth.set_access_token(Access_token, Access_token_secret)
# api_auth = tweepy.API(auth)
# message = "#UMSI-206 #Proj3"
# api_auth.updatej_with_media('puppy.jpg', status = message)


#http://stackoverflow.com/questions/19337672/post-tweet-with-tweepy
#Used code from here

#use open to write an html file
#create our own html file as the last step
#use tweepy

print('\n')
print("--------------------------")
print("Part D")

# import tweepy
# from textblob import TextBlob



# # Boilerplate code here
# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)

# api = tweepy.API(auth)
# #Now we can Create Tweets, Delete Tweets, and Find Twitter Users

# public_tweets = api.search('"Gilmore Girls" @netflix')

# for tweet in public_tweets:
# 	print(tweet.text)
# 	analysis = TextBlob(tweet.text)
# 	print(analysis.sentiment)
