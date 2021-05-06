import pandas as pd

class Analyse:
    def __init__(self, path = "dataset/bestsellers with categories.csv"):
        self.booklist = pd.read_csv(path)
        self.changepricetoRupee()
        self.cleanData()

    def cleanData(self):
        self.booklist.set_index('Name', inplace=True)

    def viewDescription(self):
        return self.booklist.describe()
        
    def viewDescriptionCate(self):
        return self.booklist.describe(include = 'O') 
    def viewTop50(self):
        return self.booklist.head(50).sort_values('User Rating', ascending=False)

        
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

    #Find average rating of fiction over year
    def getFictionRate(self):
        fic = self.booklist[self.booklist['Genre']=='Fiction']
        return fic.groupby('Year').mean()['User Rating']

    def getFictionReview(self):
        fic = self.booklist[self.booklist['Genre']=='Fiction']
        return fic.groupby('Year').mean()['Reviews']

    def getFictionPrice(self):
        fic = self.booklist[self.booklist['Genre']=='Fiction']
        return fic.groupby('Year').mean()['Price']



#__________________________________Non Fiction book Per Year________________________________

    def getNonFictionPerYear(self):
        self.n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return self.n_fic.groupby('Year').count()['Genre']

    #Find Average Rating of Non Fiction Over Year
    def getNonFictionRate(self):
        n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return n_fic.groupby('Year').mean()['User Rating']

    def getNonFictionReview(self):
        n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return n_fic.groupby('Year').mean()['Reviews']

    def getNonFictionPrice(self):
        n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return n_fic.groupby('Year').mean()['Price']


#______________________________________NO oF BOOK PUBLISHED BY AN AUTHOR_____________________________

    def getBooksByAuth(self):
        self.auth = self.booklist.groupby('Author').count()['Price']
        return self.auth.head(50).sort_values(ascending = False)

#____________________________________Author wise Book rating

    def getAuthorList(self):
        return self.booklist['Author'].unique()

    def getTopRateAuth(self, n):
        ratingCount = self.booklist.groupby('Author').count()
        return ratingCount[ratingCount['User Rating'] > n].index
        
    def getTopReviewAuth(self):
        return self.booklist.groupby('Author').mean()['Reviews'].head(10).sort_values(ascending = False).index

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
        return self.booklist['Price'].head(100).sort_values(ascending = False)

    # def getpriceview(self):
    #     return self.booklist.groupby('Price')
    
    # def viewByPrice(self, n):
    #     priceCount = self.booklist.groupby('Author').count()
    #     return priceCount[priceCount['Price'] > n].index

    def ficAndNonFic(self):
        return self.booklist.groupby(['Year','Genre']).count().unstack()['Price']

    def freebooks(self):
        df=self.booklist[self.booklist['Price']==0]
        return df['Genre'].value_counts()
        


#__________________________________________ count Rating


    def getCountRate(self):
        return self.booklist['User Rating'].value_counts()
    def getCountRate2(self):
        return self.booklist['User Rating']

#_______________________________________________Year
    # Year Ranked on bestSeller
    def NoBookBestyear(self):
        return self.booklist['Year']

    def avgRevOverYear(self):
        return self.booklist.groupby('Year').mean()['Reviews']

    def avgPriceOverYear(self):
        return self.booklist.groupby('Year').mean()['Price']

    def avgRatingOverYear(self):
        return self.booklist.groupby('Year').mean()['User Rating']

    #AVG. PRICE-AVG. RATINGS RELATIONSHIP OF TOP 10 AUTHORS WITH HIGHEST AVG. PRICED BESTSELLERS
    def avgPrice_Ratingrelation(self):
        return self.booklist.groupby('Author').mean().sort_values('Price',ascending=False).reset_index().head(50)
    
    def avgPrice_Reviewrelation(self):
        return self.booklist.groupby('Author').mean().sort_values('Reviews',ascending=False).reset_index().head(50)
    
    def avgindex(self):
        return self.booklist.groupby('Author').mean().sort_values('Year',ascending=False).reset_index().head(50)
    
    def sctter(self):
        return self.booklist