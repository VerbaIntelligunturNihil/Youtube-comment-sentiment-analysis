#Import needed tools
from textblob import TextBlob

#Create class for sentiment analysis
class SentimentAnalyzer:

    #Create list for polarity of the comments
    def __init__(self):
        self.polarities = []

    #Get polarity of comments:
    def get_polarity(self,data):
        polarities = self.polarities
        for element in data.comment_text.values:

            try:
                rating = TextBlob(element)
                polarities.append(rating.sentiment.polarity)

            except:
                polarities.append(0)

        #Add the polarities to the data
        data['polarity'] = polarities

        #Convert the polarities to the categorical values
        data['polarity'][data.polarity > 0] = 1
        data['polarity'][data.polarity == 0] = 0
        data['polarity'][data.polarity < 0] = -1

        return data
