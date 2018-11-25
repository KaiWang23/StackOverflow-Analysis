import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import Select
from bokeh.palettes import Set3
from bokeh.plotting import curdoc, figure

df = pd.read_csv('final.csv')

COLORS = Set3


columns = sorted(df.columns[1:])

def create_figure():
    xs = df['Year']
    ys = df[y.value].values
    #x_title = xs.apply(lambda x:str(x)).values
    y_title = y.value.title()
    groups = pd.Categorical(df['Year'])
    c = [COLORS[10][xx] for xx in groups.codes]
    data = {'year' : xs,
        'value'   : ys,
        'c' : c
        }


    p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,hover,reset')
    p.xaxis.axis_label = 'Year'
    p.yaxis.axis_label = y_title


    sz = 9

    #    else:
    groups = pd.Categorical(df['Year'])
    c = [COLORS[10][xx] for xx in groups.codes]

    p.vbar(x='year', top='value', width= 0.9, color='c', line_color="white", alpha=0.6, source = data)
    p.hover.tooltips = [("Year", '@year'), ('Value', '@value')]
    return p


def update(attr, old, new):
    layout.children[1] = create_figure()



y = Select(title='Question', value='Percent_Questions_with_Answers', options=columns)
y.on_change('value', update)



controls = widgetbox([y], width=300)
layout = row(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "CS_516_proj"
