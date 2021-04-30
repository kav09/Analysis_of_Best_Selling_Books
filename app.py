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


st.title('Analysis of Best Selling Books')

# from PIL import Image
#img = Image.open('bf.png')
#st.image(img)
# st.markdown('![](data:image/jpeg;base64,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)')
#st.markdown('![Analysis of book](https://st2.depositphotos.com/1105977/5461/i/600/depositphotos_54615585-stock-photo-old-books-on-wooden-table.jpg)')

def viewDataset(pathlist):
    selDataset = st.selectbox(options=pathlist, label="Select Dataset to view")
    if selDataset:
        df = pd.read_csv(selDataset)
        st.dataframe(df)
    

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
    import seaborn as sns
    sns.set_style('whitegrid')

    # data = analysis.ficAndNonFic()
    # plot1 = plotBar(data.index, data.values, 'Plot 1', 'xlabel', 'ylabel')
    # plot2 = plotBar(data.index, data.values, 'Plot 2', 'xlabel', 'ylabel')
    
    # st.plotly_chart(plotSubplot(1, 2, [plot1, plot2]))

    st.header('Fiction Vs Non Fiction')
    col1, col2= st.beta_columns(2)
    with col1:
    # Fiction vs Non Fiction
        data = analysis.getFicVsNonFic()
        st.plotly_chart(plotpie(data.index,data.values,''))
    with col2:
        data = analysis.getFicVsNonFic()
        st.plotly_chart(plotBar(data.index, data.values,"","Genre","No Of Books",350,450))    
#--------------------------------------------------------------------
    st.header('Number of Fiction and Non FIction Books Published Per Year')
    col1, col2= st.beta_columns(2)
    # fiction books per year
    with col1:
        data = analysis.getFictionPerYear()
        st.plotly_chart(plotBar(data.index, data.values, "Number of Fiction Book published per Year.", "Years", 'No. of Books Published',550,400))

    # Non fiction book per year
    with col2:
        data = analysis.getNonFictionPerYear()
        st.plotly_chart(plotBar(data.index, data.values, "Number of Non Fiction Book published per Year.","Years","No.of Book Published",550,400))

    # fiction and non-fiction books per year
    st.header('Comparision of Number of Fiction and Non FIction Books Published Per Year')
    fic_data = analysis.getFictionPerYear()
    nonfic_data = analysis.getNonFictionPerYear()
    st.plotly_chart(plotGroupedBar([ nonfic_data, fic_data ], ['Non-Fiction Books', 'Fiction Books'], "", "Years", 'No. of Books Published'))


def analysebyAuthor():

    # No of Books published By Authors
    data = analysis.getBooksByAuth()
    st.plotly_chart(plotBar(data.index, data.values, "Number of Book Published","Author","No of Books",800,500))

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
    
#---------------------------------------------------
    
    
    
def analysebyReview():

    data = analysis.getReview()
    st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    booklist = st.selectbox(options = analysis.getName(), label = "Select Book Name to analyse")


    #data = analysis.getverReview(booklist)
    #st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    #data = analysis.getverReview(selAuthor)
    #st.plotly_chart(plotLine(data.index, data.values,"Reviews"))

    #data = analysis.getverRating(selAuthor)
    #st.plotly_chart(plotLine(data.index, data.values,"User Rating"))


#________________________________________________________


def analyseByPrice():
    data = analysis.getprice()
    st.plotly_chart(plotHistogram(data,"Price of Books", '', ''))

    data = analysis.getprice()
    st.plotly_chart(plotBar(data.index,data.values,"Price of Books", '', '',700,900))


    rpt = st.checkbox('Generate Report')
    if rpt:
        ViewForm()
#----------------------------------------------------------------------
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
options = ['View Dataset', 'Analyze By Genre','Analyze By Author','Analyze By Reviews','Analyse By Price','View Report']
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
    ViewReport()
    
