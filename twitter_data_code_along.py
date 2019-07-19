'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
tweetFile.close()


tweets = []
for i in range(len(tweetData)):
	onetweet = tweetData[i]["text"]
	tweets.append(onetweet)

	tweetString = " "
	for tweet in tweets:
		tweet = tweet + " "
		tweetString += tweet
# print(len(tweets))

# print(tb.polarity)

polaritylist = []
for i in tweets:
	polaritylist.append(TextBlob(i).polarity)
# print(polaritylist)

def counterLetter(string, letter):
	counter = 0
	for let in string :
		if let.lower() == letter:
			counter += 1
		else:
			counter += 0
	return counter



counterLetter(tweetString, "a")
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = sorted(alpha)

occurences = []
for letter in letters:
	occurences.append(counterLetter(tweetString, letter))


def wordCount(stringOfTweet, string1):
	counter = 0
	string1 = string1.lower()
	wordList = stringOfTweet.split(' ')
	for item in wordList:
		if item == string1:
			counter += 1
	return counter
# print(tweetString)

# print(text)
# for item in tweet:
# 	long_string += item + " "

#
# wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetString)
# plt.figure(figsize = (10, 10), facecolor = None)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# plt.savefig("Etta'stwitterchart.png")

#histogram code
# print(polaritylist)
# print(min(polaritylist), max(polaritylist))

plt.xlabel("tweets")
plt.ylabel("occurences")
plt.hist(occurences)
plt.axis([min(occurences), max(occurences), 0, 10])
plt.show()
plt.savefig("Ettaschart.png")




# print(type(tweetData))
# print(type(tweetData[0]))

# print(type(tweetData[0].keys()))

# print(tweetData[0]["favorite_count"])
#
# favoriteCount = 0
# totalfavoriteCount = 0
#
# for i in range(0,len(tweetData)):
#
# 	if "favorite_count" in tweetData[i]:
# 		totalfavoriteCount += tweetData[i]['favorite_count']
#
# averagefavoriteCount = totalfavoriteCount/len(tweetData)
# print(len(tweetData))
# print(averagefavoriteCount)
#
# print(tweet[2])

			# nums[index] += numOfLetter(text, alpha[index])
# We can close the file now that we have locally stored the data.
# tweetFile.close()
