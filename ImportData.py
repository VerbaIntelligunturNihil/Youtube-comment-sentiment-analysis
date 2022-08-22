#Import needed tools
import pandas as pd
import numpy as np

#Create class for import data
class DataFrame:

    #Point the way to data
    def __init__(self):
        self.comments = pd.read_csv("Comments.csv",encoding='utf8',error_bad_lines=False)
