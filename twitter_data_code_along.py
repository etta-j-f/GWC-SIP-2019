'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as pit
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
# print(len(tweets))

# print(tb.polarity)

# polaritylist = []
# for i in tweets:
# 	polaritylist.append(TextBlob(i).polarity)
# print(polaritylist)

tweetString = " "
for tweet in tweets:
	tweet = tweet + " "
	tweetString += tweet
print(tweetString)

# print(text)
# for item in tweet:
# 	long_string += item + " "

wordcloud = WordCloud().generate(tweetString)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig("Etta'stwitterchart.png")




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
#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
