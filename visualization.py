import plotly.graph_objects as go

#def plot():
    #fig = go.Figure()
    #fig.add_trace( go.Line(x = [i for i in range(10)], y = [i*i for i in range(10)]))
    #return fig

#-------------------------------------------Plot Pie Chart--------------------

def plotpie(labels,values,title):
    layout = go.Layout(title = title)
    fig = go.Figure(layout= layout)
    for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
        fig.update_layout(template=template)
    fig.add_trace(go.Pie(labels=labels,values=values))
    return fig

#--------------------------------Plot Bar Chart------------------------

def plotBar(x,y, title, xlabel, ylabel):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    for template in ["plotly_dark"]:
        fig.update_layout(template=template)
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
def plotLine(x,y,title):
    layout = go.Layout(title= title)
    fig = go.Figure(layout = layout)
    fig.add_trace(go.Line(x=x,y=y))
    return fig

#--------------------------------
def plotHistogram(x,y,title):
    layout = go.Layout(title =title)
    fig = go.Figure(layout = layout)
    fig.add_trace(go.Histogram(x=x,y=y))
    return fig