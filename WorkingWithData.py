#Import needed tools
import pandas as pd

#Create class for working with data
class DataFrame:

    #Point the path to data
    def __init__(self, path):
        self.comments = pd.read_csv(path, encoding='utf8', error_bad_lines=False)
