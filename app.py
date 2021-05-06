import streamlit as st
import pandas as pd
import numpy as np

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Report
from visualization import *
from AnalyseData import Analyse
import matplotlib as mpl
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse()

df = pd.read_csv('dataset/bestsellers with categories.csv')

#______________________________________________________________HEADER
col1 ,col2 = st.beta_columns(2)
with col1:
    st.image('bf.png')
with col2: 
    st.title(' Analysis of Best Selling Books')
st.markdown("---")
st.markdown("")

#________________________________________________

def viewDataset(pathlist):

    # if st.checkbox('View Dataset'):
    #     selDataset = st.selectbox(options=pathlist, label="Select Dataset to view")

    #     if selDataset:
    #         df = pd.read_csv(selDataset)
    #         st.dataframe(df)


    with st.spinner("Loading Data..."):
        st.dataframe(df)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {df.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {df.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(df.describe())
        st.markdown('---')

        types = {'object' : 'Categorical', 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], df.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(df.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {df[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")
            st.markdown("___")
    # if st.checkbox("View Description"):
    #     #if st.checkbox('Numerical Desciption'):
    #     st.subheader('Numerical Desciption')
    #     data = analysis.viewDescription()
    #     st.dataframe(data)
    #     #if st.checkbox('Categorical Description'):
        # st.subheader('Categorical Desciption')
        # data = analysis.viewDescriptionCate()
        # st.dataframe(data)

    # if st.checkbox("View Top Rated"):
    #      data = analysis.viewTop50()
    #      st.dataframe(data)

    

def ViewForm():

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button('Submit')

    if btn:
        report1 = Report(title= title, desc = desc , data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')


#--------------------------------------------------------------------
def analyseByGenre():
    #import seaborn as sns
    #sns.set_style('whitegrid')
    #data = analysis.ficAndNonFic()
    #st.plotly_chart(plotSubplot(data.index,data.values))


    if st.checkbox("Fiction Vs Non Fiction"):
        st.write("#### **NON-FICTION BESTSELLERS ARE MORE THAN FICTION**") 
        col1, col2= st.beta_columns(2)
        with col1:
            # Fiction vs Non Fiction
            data = analysis.getFicVsNonFic()
            st.plotly_chart(plotpie(data.index,data.values,'')) 
        with col2:
            data = analysis.getFicVsNonFic()
            st.plotly_chart(plotBar(data.index, data.values,"","Genre","No Of Books",350,450)) 
        

    
#--------------------------------------------------------------------
    st.markdown("___")
    if st.checkbox('View Number of Fiction and Non FIction Books Published Per Year'):
        #st.subheader('Number of Fiction and Non FIction Books Published Per Year')
        # fiction books per year
        col1,col2 = st.beta_columns(2)
        with col1:
            data = analysis.getFictionPerYear()
            st.plotly_chart(plotBar(data.index, data.values, "Number of Fiction Book published per Year.", "Years", 'No. of Books Published',550,400))

        # Non fiction book per year
        with col2:
            data = analysis.getNonFictionPerYear()
            st.plotly_chart(plotBar(data.index, data.values, "Number of Non Fiction Book published per Year.","Years","No.of Book Published",550,400))

    st.markdown("___")
    # fiction and non-fiction books per year
    if st.checkbox('Comparision of Genre'):
        col1 , col2 = st.beta_columns(2)
        with col1:
            fic_data1 = analysis.getFictionPerYear()
            nonfic_data1 = analysis.getNonFictionPerYear()
            st.plotly_chart(plotGroupedBar([ nonfic_data1, fic_data1 ], ['Non-Fiction Books', 'Fiction Books'], "Books Published Per Year By Gener", "Years", 'No. of Books Published'))
            st.markdown("___")

    # AVERAGE RATING BY GENRE OVER YEAR
        with col2:
            fic_data2 = analysis.getFictionRate()
            nonfic_data2 = analysis.getNonFictionRate()
            st.plotly_chart(plotGroupedBar([ nonfic_data2, fic_data2 ], ['Non-Fiction Books', 'Fiction Books'], "AVERAGE RATING BY GENRE OVER YEAR", "Years", 'Average Rating'))
            st.markdown("___")

    # AVERAGE RATING BY GENER OVER YEAR
        col3 , col4 = st.beta_columns(2)
        with col3:
            fic_data3 = analysis.getFictionReview()
            nonfic_data3 = analysis.getNonFictionReview()
            st.plotly_chart(plotGroupedBar([ nonfic_data3, fic_data3 ], ['Non-Fiction Books', 'Fiction Books'], "Average Reviews By Gener Over Year", "Years", 'Average Review'))
            st.markdown("___")

    # AVERAGE RATING BY GENER OVER YEAR
        with col4:
            fic_data4 = analysis.getFictionReview()
            nonfic_data4 = analysis.getNonFictionReview()
            st.plotly_chart(plotGroupedBar([ nonfic_data4, fic_data4 ], ['Non-Fiction Books', 'Fiction Books'], "Average Price By Gener Over Year", "Years", 'Average Review'))
            st.markdown("___")

def analysebyAuthor():

    # No of Books published By Authors
    data = analysis.getBooksByAuth()
    st.plotly_chart(plotBar(data.index, data.values, "Number of Book Published","Author","No of Books",1000,500))

    st.markdown("___")

    # Author List
    if st.checkbox("VIEW ALL AUTHORS lIST"):
        selAuthor = st.selectbox(options = analysis.getAuthorList(), label = "Select Author to analyse")

        with st.beta_container():
                col1 , col2 = st.beta_columns(2)
                with col1:
                    # Particular Author and its Review
                    data = analysis.getverReview(selAuthor)
                    st.plotly_chart(plotLine(data.index, data.values,"Reviews"))
                with col2:
                # Particular Name of Author and its User RAting
                    data = analysis.getverRating(selAuthor)
                    st.plotly_chart(plotLine(data.index, data.values,"User Rating"))

    if st.checkbox('View By Top Rated Authors'):
        n = st.select_slider(options = [5, 10, 15], label ='Author having No. of Rating')
        toprateauthor = st.selectbox(options = analysis.getTopRateAuth(n), label = "Select Author to analyse")
        

        with st.beta_container():
            col1 , col2 = st.beta_columns(2)
            with col1:
                    # Particular Author and its Review
                data = analysis.getverReview(toprateauthor)
                st.plotly_chart(plotLine(data.index, data.values,"Reviews"))
            with col2:
                # Particular Name of Author and its User RAting
                data = analysis.getverRating(toprateauthor)
                st.plotly_chart(plotLine(data.index, data.values,"User Rating"))


    if st.checkbox('View By Top Review Author'):
        #n = st.select_slider(options = [100,1500,2000], label ='Author having No. of Rating')
        toprevauthor = st.selectbox(options = analysis.getTopReviewAuth(),label = "Select Author")

        with st.beta_container():
            col1 , col2 = st.beta_columns(2)
            with col1:
                    # Particular Author and its Review
                data = analysis.getverReview(toprevauthor)
                st.plotly_chart(plotLine(data.index, data.values,"Reviews"))
            with col2:
                # Particular Name of Author and its User RAting
                data = analysis.getverRating(toprevauthor)
                st.plotly_chart(plotLine(data.index, data.values,"User Rating"))

    st.markdown("___")
    
    data =  analysis.avgPrice_Ratingrelation()
    st.plotly_chart(plotScatter(data,x='User Rating', y= 'Price',color= 'Author',title = 'Average Price & Average Rating Of Top 50 Authors With Average Price BestSellers'))
    
    st.markdown("___")

    data =  analysis.avgPrice_Reviewrelation()
    st.plotly_chart(plotScatter(data,x='User Rating', y= 'Reviews',color= 'Author',title = 'Average Review & Average Rating Of Top 50 Authors With Average Price BestSellers'))

    st.markdown("___")

    data =  analysis.avgindex()
    st.plotly_chart(plotScatter(data, x = 'Price', y='Reviews', color= 'Author',title = 'Average Price & Average Reviews Of Top 50 Authors With Average Price BestSellers'))
     
#---------------------------------------------------
    
    
    
def analysebyReview():


    data = analysis.getReview()
    st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    #booklist = st.selectbox(options = analysis.getName(), label = "Select Book Name to analyse")


    #data = analysis.getverReview(booklist)
    #st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    #data = analysis.getverReview(selAuthor)
    #st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    #data = analysis.getverRating(selAuthor)
    #st.plotly_chart(plotLine(data.index, data.values,"User Rating"))


#________________________________________________________


def analyseByPrice():
    
    data = analysis.getprice()
    st.plotly_chart(plotHistogram(data,"No of books having same price", 'Price', 'No Of Books'))
    
    st.markdown("___")

    data = analysis.sctter()
    st.plotly_chart(plotScatter(data,x='Price', y= 'User Rating',color = 'User Rating',title = ''))

    st.markdown("___")

    # data = analysis.getprice()
    # st.plotly_chart(plotBar(data.index,data.values,"Price of Books", '', '',600,800))

    data = analysis.getprice()
    st.plotly_chart(plotLine(data.index,data.values,"Price of Books"))

    st.markdown("___")

    #--------------------------------------FreeBooks
    st.subheader("Free BestSeller Books")
    cols = st.beta_columns(2)
    with cols[0]:
        st.subheader("Pie Chart")
        data = analysis.freebooks()
        st.plotly_chart(plotpie(data.index,data.values,'')) 
    with cols[1]:
        st.subheader("Bar Chart")
        data = analysis.freebooks()
        st.plotly_chart(plotBar(data.index,data.values,'','','',500,450)) 
    st.text('Maximum Number of Books Published Free Is Of Fiction Category, that is, 11 books.')
    
    

    st.markdown("___")
    
    rpt = st.checkbox('Generate Report')
    if rpt:
        ViewForm()
#----------------------------------------------------------------------

def analysebyYear():

    data =  analysis.NoBookBestyear()
    st.plotly_chart(plotHistogram(data,"Average Review Over Years", 'Year', 'Average Review'))

    st.subheader("Average Review Over Years")
    #if st.checkbox("Select Chart To View Average Review Over Years"):
    col1, col2 = st.beta_columns(2)
    with col1:
        data = analysis.avgRevOverYear()
        st.plotly_chart(plotBar(data.index,data.values,"Bar Chart", 'Year', 'Average Review',700,450))
    with col2:
        #if st.checkbox('Line Chart of Average Review Over Year'):
        data = analysis.avgRevOverYear()
        st.plotly_chart(plotLine(data.index,data.values,"Line Chart"))

    st.markdown("___")

    st.subheader("Average Price Over Years")
    #if st.checkbox("Select Chart To View Average Price Over Years"):
    col3, col4 = st.beta_columns(2)
    with col3:
        #if st.checkbox('Bar Chart of Average Price Over Years'):
        data = analysis.avgPriceOverYear()
        st.plotly_chart(plotBar(data.index,data.values,"Bar Chart", 'Year', 'Average Price',700,450))
    with col4:
        #if st.checkbox('Line Chart of Average Price Over Years'):
        data = analysis.avgPriceOverYear()
        st.plotly_chart(plotLine(data.index,data.values,":Line Chart"))
        
    st.markdown("___")

    st.subheader("Average Rating Over Years")
    #if st.checkbox("Select Charts To View Average Rating Over Years"):
    col5, col6 = st.beta_columns(2)
    with col5:
            #if st.checkbox('Bar Chart of Average Rating Over Years'):
        data = analysis.avgRatingOverYear()
        st.plotly_chart(plotBar(data.index,data.values,"Bar Chart", 'Year', 'Average Rating',700,450))
    with col6:
            #if st.checkbox('Line Chart of Average Rating Over Years'):
        data = analysis.avgRatingOverYear()
        st.plotly_chart(plotLine(data.index,data.values,"Line Chart"))
    

#-----------------------------------------------------------------------
def analysebyRating():

    data = analysis.getCountRate2()
    st.plotly_chart(plotHistogram(data,"Average Rating", 'Year', 'Average Review'))

    data = analysis.getCountRate()
    st.plotly_chart(plotBar(data.index, data.values, "Count Rating.","User Rating","Count(How many times apper)",550,400))
    st.write("***MOST OF THE RATINGS ARE IN THE RANGE OF 4.6 TO 4.8***")


def ViewReport():
    reports =sess.query(Report).all()
    titleslist = [report.title for report in reports]
    selReport = st.selectbox(options = titleslist , label = "Select Report")

    reportToView = sess.query(Report).filter_by(title = selReport).first()
    #st.header(reportToView.title)
    #st.text(report)

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
    """
    st.markdown(markdown)

sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyze By Genre','Analyze By Author','Analyze By Reviews','Analyse By Price','Analyse By Year','Analyse by Rating','View Report']
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == options[0]:
    viewDataset(['dataset/bestsellers with categories.csv'])
elif choice == options[1]:
    analyseByGenre()
elif choice == options[2]:
    analysebyAuthor()
elif choice == options[3]:
    analysebyReview()
elif choice == options[4]:
    analyseByPrice()
elif choice == options[5]:
    analysebyYear()
elif choice == options[6]:
    analysebyRating()
elif choice == options[7]:
    ViewReport()
    
