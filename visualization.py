import plotly.graph_objects as go
import plotly.express as px


#-------------------------------------------Plot Pie Chart--------------------


def plotpie(labels,values,title,template):
    layout = go.Layout(title = title, template= template) #color_continuous_scale='inferno'
    fig = go.Figure(layout= layout)
    #for template in [ "ggplot2"]:
        #fig.update_layout(template=template)
    fig.add_trace(go.Pie(labels=labels,values=values,title='Genre',textinfo='label+percent',hole=0.2,
                       marker=dict(colors=['#f7d468','#74cb35'], 
                                   line_color='Gray', 
                                   line_width=1),
                       textfont={'color': '#000', 'size': 12},
                       textfont_size=12))
    return fig

#--------------------------------Plot Bar Chart------------------------


def plotBar(x,y, title, xlabel, ylabel, width, height,template):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel),width = width, height= height,template= template)
    fig = go.Figure(layout = layout)
    #fig.add_trace( go.Bar(x = x,y= y, marker = dict(color = ['#ff6666','#f76e6e', '#f07575', '#e87d7d', '#e08585',
                                    # '#d98c8c', '#d19494', '#c99c9c','#c2a3a3', '#baabab'],
                            # )))
    fig.add_trace( go.Bar(x = x,y= y))
    return fig

#-------------------------------Plot GroupBAR Chart-----------------------


def plotGroupedBar(datapoints , categories, title, xlabel, ylabel, colors = ['indianred', 'lightsalmon']):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)

    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace( go.Bar(x = point.index,y= point.values, name = category, marker_color = color))
        
    return fig
#------------------------------------------
def plotLine(x,y,title,xlabel, ylabel,template= "plotly_dark"):
    layout = go.Layout(title= title, 
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel),template = template)
    fig = go.Figure(layout = layout)
    fig.add_trace(go.Line(x=x,y=y,line_color='#f63366'))
    return fig

#--------------------------------

def plotHistogram(datapoints, title, xlabel, ylabel):
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)

    fig.update_layout(template="plotly_dark")
    fig.add_trace(go.Histogram(
        x = datapoints.values,
        # xbins = {'start': 1, 'size': 0.1, 'end' : 5}
    ))

    return fig



# def plotSubplot(rows, cols, plots):

#     fig = make_subplots(rows=rows, cols=cols)
#     for row in range(rows):
#         for col in range(cols):
#             print(row*col+col+1)
#             fig.add_trace(plots[row*col+col+1], row=row+1, col=col+1)
#     return fig

# def plotScatter(x,y):
#     #fig = go.Figure()
#     trace=go.Scatter(x=x,y=y)
#     booklist = [trace]
#     return booklist




def plotScatter(data,x , y,color,title,template= "plotly_dark"): 
    fig = px.scatter(data_frame= data, x= x, y=y,color= color,title=title,trendline= "ols")

    fig.update_traces(marker=dict(symbol= "diamond",size=10,
                                line=dict(width=2,
                                        color='DarkSlateGrey')),
                    selector=dict(mode='markers'))
    fig.update_layout(width = 1000, height = 500,template = template)

    return fig

def plotScatter1(data,x , y,title,template= "plotly_dark"): 
    fig = px.scatter(data_frame= data, x= x, y=y,title=title)

    fig.update_traces( marker=dict(color = 'rgb(249, 6, 6)',
                             line=dict(color='rgb(0,0,0)',width=1.0)),mode='lines+markers')
    fig.update_layout(template = template)

    return fig
