#Import needed tools
from youtube_comment_scraper_python import *
import pandas as pd


#Create class for parcing data
class Parser:

    def __init__(self, link):
        youtube.open(link)
        self.current_page_source = youtube.get_page_source()
        self.last_page_source = ""
        self.response = youtube.video_comments()

    def GetData(self):
        data = []

        while(True):

            if (self.last_page_source == self.current_page_source):
                df = pd.DataFrame(data)
                df = df[['user', 'Comment']].drop_duplicates(keep = "first")
                return df[['user', 'Comment']]
                break

            self.last_page_source = self.current_page_source

            for element in self.response['body']:
                data.append(element)

            self.current_page_source = youtube.get_page_source()
