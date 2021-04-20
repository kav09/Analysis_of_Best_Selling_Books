import pandas as pd

class Analyse:
    def __init__(self, path = "dataset/bestsellers with categories.csv"):
        self.booklist = pd.read_csv(path)
        #self.cleanData()

    #def cleanData(self):
        #self.df

    def getCategories(self):
        self.fic = self.booklist[self.booklist['Genre']=='Fiction']
        self.fic_year = self.fic[['Genre', 'Year']].groupby('Year').count()
        return self.fic_year
       
        #self.t_genre = self.booklist.groupby('Genre').count()
        #return self.t_genre['Total'] 
