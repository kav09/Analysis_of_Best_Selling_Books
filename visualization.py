import plotly.graph_objects as go

#def plot():
    #fig = go.Figure()
    #fig.add_trace( go.Line(x = [i for i in range(10)], y = [i*i for i in range(10)]))
    #return fig

#-------------------------------------------FICTION VS NON FICTION BOOKS--------------------

def plotpie(labels,values):
    layout = go.Layout(title = "Fiction Vs Non Fiction")
    fig = go.Figure(layout= layout)
    fig.add_trace(go.Pie(labels=labels,values=values))
    return fig

#--------------------------------No Of FICTION BOOK PUBLISHED PER YAER------------------------

def plotBar(x,y, title, xlabel, ylabel):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    fig.add_trace( go.Bar(x = x,y= y))
    return fig

def plotGroupedBar(datapoints , categories, title, xlabel, ylabel, colors = ['indianred', 'lightsalmon']):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)

    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace( go.Bar(x = point.index,y= point.values, name = category, marker_color = color))
        
    return fig
#------------------------------------------No OF NON FICTION BOOK PUBLISHED PER YEAR

def plotBar2(x,y):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))
    
    layout = go.Layout(title= "Number of Non Fiction Book published per Year.",
                    xaxis=dict(title='Years'),
                    yaxis=dict(title='Number of Books Published'))
    fig = go.Figure(layout = layout)
    fig.add_trace( go.Bar(x = x,y= y))
    return fig

#----------------------------------------NO oF BOOK PUBLISHED BY AN AUTHOR

def plotBar3(x,y):
    layout = go.Layout(title= "Number of Books Published By an Author.",
                    xaxis=dict(title='Authors'),
                    yaxis=dict(title='Number of Books'))
    fig = go.Figure(layout = layout)
    fig.add_trace( go.Bar(x = x,y= y))
    return fig