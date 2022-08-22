#Import needed tools
from WorkingWithData import DataFrame
from SentimentEngine import SentimentAnalyzer

#Input path to the data
path = "Comments.csv"

#Create class for working with data
df = DataFrame(path)

#Create class for sentiment analysis
sa = SentimentAnalyzer()

#Get data from dataset
comments = df.comments

#Get polarity of the comments:
polarities = sa.get_polarity(comments)

#Add the polarities to the data
comments['polarity'] = polarities

#Convert the polarities to the categorical values
comments['polarity'][comments.polarity > 0] = 1
comments['polarity'][comments.polarity == 0] = 0
comments['polarity'][comments.polarity < 0] = -1
