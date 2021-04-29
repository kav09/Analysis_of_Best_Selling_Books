import pandas as pd

class Analyse:
    def __init__(self, path = "dataset/bestsellers with categories.csv"):
        self.booklist = pd.read_csv(path)
        self.changepricetoRupee()
        self.cleanData()

    def cleanData(self):
        self.booklist.set_index('Name', inplace=True)
        
    def changepricetoRupee(self):
        self.booklist['Price'] = self.booklist['Price'].map(lambda price : price*75)
        
    #def getCategories(self):
        #self.fic = self.booklist[self.booklist['Genre']=='Fiction']
        #self.fic_year = self.fic[['Genre', 'Year']].groupby('Year').count()
        #return self.fic_year
       
        #self.t_genre = self.booklist.groupby('Genre').count()
        #return self.t_genre['Total'] 

#____________________________________Fiction Vs Non Fiction______________________________

    def getFicVsNonFic(self):
        return self.booklist.groupby('Genre').count()['Price']
        #return self.t_genre['Price']

#___________________________________Fiction Book per year_____________________________

    def getFictionPerYear(self):
        fic = self.booklist[self.booklist['Genre']=='Fiction']
        return fic.groupby('Year').count()['Genre']

#__________________________________Non Fiction book Per Year________________________________

    def getNonFictionPerYear(self):
        self.n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return self.n_fic.groupby('Year').count()['Genre']

#______________________________________NO oF BOOK PUBLISHED BY AN AUTHOR_____________________________

    def getBooksByAuth(self):
        self.auth = self.booklist.groupby('Author').count()['Price']
        return self.auth.head(20).sort_values(ascending = False)

#____________________________________Author wise Book rating

    def getAuthorList(self):
        return self.booklist['Author'].unique()

    def getTopRateAuth(self):
        return self.booklist.groupby('Author').mean()['User Rating'].sort_values(ascending = False)
        
    def getTopReviewAuth(self):
        return self.booklist.groupby('Author').mean()['Reviews'].head(10).sort_values(ascending = False)

    def getverRating(self, author):
        return self.booklist[self.booklist['Author']==author]['User Rating']
        #booklist.groupby('Author').mean()['User Rating'].sort_values(ascending= False)

#______________________________________Review
    
    def getReview(self):
        #return self.booklist[self.booklist['Price'] == index ]['Author']
        return self.booklist.groupby('Author').count()['Reviews'].head(50)

   # Author 's review
    def getverReview(self, author):
        
        return self.booklist[self.booklist['Author']== author]['Reviews']

#_______________________________________Price

    def getName(self):
        return self.booklist.index.unique()

    def getprice(self):
        return self.booklist['Price'].head(20).sort_values(ascending = False)
    